#!/usr/bin/python
#coding:utf-8
import os
import re
import argparse
class ThreadInfo:
    tName = ""
    daemon = ""
    prio = "0"
    tid = "0x0"
    nid = "0x0"
    cid = "0x0"
    line = ""
    lockId = "0x0"


class LockInfo:
    lockid = "0x0"
    waiterTheadList = []

    def LockInfo(self):
        print self

verbose = True
def getLog(pid):
    # text_file = open("/home/mbl/a.txt", "r")
    # lines = text_file.readlines()
    # text_file.close()
    command = 'jstack -l '+ str(pid)
    r = os.popen(command)
    lines = r.readlines()

    return lines

def plockInfo(pid,lockid):
    lockMap = {}
    lockHolderMap = {}
    lines = getLog(pid)

    # print "lines = " , lines

    threadInfo = None
    for line in lines:
        searchObj = re.search(r'"(.*)"( daemon)? prio=([0-9]+) tid=(0[xX][A-Fa-f0-9]+) nid=(0[xX][A-Fa-f0-9]+) waiting on condition \[(0[xX][A-Fa-f0-9]+)\].*', line, re.M | re.I)
        if searchObj:
            # print "searchObj.group() : ", searchObj.group()
            threadInfo = ThreadInfo()
            threadInfo.tName = searchObj.group(1)
            threadInfo.line = line.strip()
            threadInfo.daemon = searchObj.group(2)
            threadInfo.prio = searchObj.group(3)
            threadInfo.tid = searchObj.group(4)
            threadInfo.nid = searchObj.group(5)
            threadInfo.cid = searchObj.group(6)
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
                searchObj = re.search(r'- <(0[xX][A-Fa-f0-9]+)> .*', line, re.M | re.I)

                if searchObj is None:
                     searchObj = re.search(r'- locked <(0[xX][A-Fa-f0-9]+)> .*', line, re.M | re.I)
                if searchObj:
                    runCount = 0
                    if searchObj.group(1) in lockHolderMap:
                        runCount = lockHolderMap[searchObj.group(1)]
                    runCount += 1
                    lockHolderMap[searchObj.group(1)] = runCount




    print "total log line count = %d" % len(lines) ,", total lockCount = " , len(lockMap)

    # print "\t", "[%5s] %18s %7s %18s %6s %18s %s" % (
    # "index", "", "daemon", "Tid", "Nid", "Condtion", "ThreadName")
    # print "\t--------------------------------------------------------------------------------------------------------- "
    if lockid in lockMap:
        plockinfobyid(lockid, 0, lockHolderMap, lockMap[lockid])
    else:
        lockCount = 0
        for k, v in lockMap.iteritems():
            plockinfobyid(k, lockCount, lockHolderMap, v)
            lockCount += 1
    # print lockMap


def plockinfobyid(k, lockCount, lockHolderMap, v):
    runNum = 0;
    msg = ""
    if k in lockHolderMap:
        runNum = lockHolderMap[k]
    if runNum == 0:
        msg = "There had unlocked lock and make deadlock."
    print "\t", "<%-5d> %18s waited num %5d , run num %5d. %s" % (
        lockCount, k, len(v.waiterTheadList), runNum, msg)
    if verbose:
        plockedtheadinfo(v)


def plockedtheadinfo(v):
    print "\t", "%7s %18s %7s %18s %6s %18s %s" % (
        "index", "", "daemon", "Tid", "Nid", "Condtion", "ThreadName")
    print "\t--------------------------------------------------------------------------------------------------------- "
    for index in range(len(v.waiterTheadList)):
        curWT = v.waiterTheadList[index]
        print "\t", "[   %2d] %18s %7s %18s %6s %18s %s" % (
            index, "", "" if curWT.daemon == None else curWT.daemon, curWT.tid, curWT.nid,
            curWT.cid, curWT.tName)
    print ""


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="A tool to print jvm lock info.")

    parser.add_argument("-pid",  type=int, required=True,
                        help="specify a jvm process id which you want to print lock info. ")
    parser.add_argument("-lockid",  type=str,
                        help="specify a lockid to filter information. ")
    parser.add_argument("-v", "--verbose", help="increase output verbosity",
                        action="store_true")
    args = parser.parse_args()

    verbose = args.verbose
    plockInfo(args.pid,args.lockid)
