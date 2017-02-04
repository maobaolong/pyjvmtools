#!/usr/bin/python
#coding:utf-8

import os
import re
import argparse

class ThreadInfo:
    tName = None
    daemon = None
    prio = None
    tid = None
    nid = None
    line = None
    lockId = None

class LockInfo:
    lockid = None
    waiterTheadList = []

verbose = True
def getLogFromPid(pid):
    command = 'jstack -l '+ str(pid)
    r = os.popen(command)
    lines = r.readlines()
    return lines

def getLogFromFile(file):
    text_file = open(file, "r")
    lines = text_file.readlines()
    text_file.close()
    return lines

def plockInfo(lines,lockid):
    lockMap = {}
    lockHolderMap = {}

    threadInfo = None
    for line in lines:
        searchObj = re.search(
            r'"(.*)"\s?'
            r'(?:#[0-9]+)?\s?'
            r'(daemon)?\s?'
            r'prio=([0-9]+)\s?'
            r'(?:os_prio=[0-9]+)?\s?'
            r'tid=(0[xX][A-Fa-f0-9]+)\s?'
            r'nid=(0[xX][A-Fa-f0-9]+).*', line, re.M | re.I)
        if searchObj:
            threadInfo = ThreadInfo()
            threadInfo.tName = searchObj.group(1)
            threadInfo.line = line.strip()
            threadInfo.daemon = searchObj.group(2)
            threadInfo.prio = searchObj.group(3)
            threadInfo.tid = searchObj.group(4)
            threadInfo.nid = searchObj.group(5)
        else:
            searchObj = re.search(r'- parking to wait for  <(.*)> .*', line, re.M | re.I)
            if searchObj:
                lockInfo = LockInfo()
                lockInfo.waiterTheadList = []
                if searchObj.group(1) in lockMap:
                    lockInfo = lockMap[searchObj.group(1)]
                else:
                    lockMap[searchObj.group(1)] = lockInfo
                lockInfo.lockid = searchObj.group(1)
                threadInfo.lockId = lockInfo.lockid
                lockInfo.waiterTheadList.append(threadInfo)
            else:
                searchObj = re.search(r'- (?:locked )?<(0[xX][A-Fa-f0-9]+)> .*', line, re.M | re.I)
                if searchObj:
                    runCount = 0
                    if searchObj.group(1) in lockHolderMap:
                        runCount = lockHolderMap[searchObj.group(1)]
                    runCount += 1
                    lockHolderMap[searchObj.group(1)] = runCount

    print "total log line count = %d" % len(lines) ,", total lockCount = " , len(lockMap)

    if lockid in lockMap:
        plockinfobyid(lockid, 0, lockHolderMap, lockMap[lockid])
    else:
        lockCount = 0
        for k, v in lockMap.iteritems():
            plockinfobyid(k, lockCount, lockHolderMap, v)
            lockCount += 1

def plockinfobyid(k, lockCount, lockHolderMap, v):
    runNum = 0;
    msg = ""
    if k in lockHolderMap:
        runNum = lockHolderMap[k]
    if runNum == 0:
        msg = "There had unlocked lock and make deadlock."
    print  "<%-5d> %18s waited num %5d , run num %5d. %s" % (
        lockCount, k, len(v.waiterTheadList), runNum, msg)
    if verbose:
        plockedtheadinfo(v)

def plockedtheadinfo(v):
    print "\t_____________________________________________________________________________________________ "
    print  "\t%-7s    %7s   %18s   %6s   %s " % (
        "| index", "daemon", "Tid", "Nid", "ThreadName")
    print "\t--------------------------------------------------------------------------------------------- "
    for index in range(len(v.waiterTheadList)):
        curWT = v.waiterTheadList[index]
        print "\t", "[   %2d] | %7s | %18s | %6s | %s" % (
            index, "N0" if curWT.daemon == None else "YES", curWT.tid, curWT.nid, curWT.tName)
    print ""

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="A tool to print jvm lock info.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-pid",  type=int, required=False,
                        help="specify a jvm process id which you want to print lock info.")
    group.add_argument("-file",  type=str, required=False,
                        help="specify a thread dump file path which you want to print lock info.")
    parser.add_argument("-lockid",  type=str,
                        help="specify a lockid to filter information. ")
    parser.add_argument("-v", "--verbose", help="increase output verbosity",
                        action="store_true")
    args = parser.parse_args()

    verbose = args.verbose

    lines = None
    if args.pid != None:
        lines = getLogFromPid(args.pid)
    else:
        lines = getLogFromFile(args.file)
    # print "lines = " , lines
    plockInfo(lines,args.lockid)
    # plockInfo(1212,None)
