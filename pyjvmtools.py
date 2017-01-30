#!/usr/bin/python
#coding:utf-8

import re
class ThreadInfo:
    tName = ""
    prio = "0"
    tid = "0x0"
    nid = "0x0"
    line = ""
class LockInfo:
    lockid = "0x0"
    waiterThead = []

def helloWorld():
    lockMap = {}
    print "hello world!"
    text_file = open("/home/mbl/a.txt", "r")
    lines = text_file.readlines()
    print lines
    print len(lines)
    tName = ""

    for line in lines:
        searchObj = re.search(r'"(.*).*".*prio=.*', line, re.M | re.I)
        if searchObj:
            # print "searchObj.group() : ", searchObj.group()
            tName = searchObj.group(1)
            # print "searchObj.group(1) : ", searchObj.group(1)
        else:
            searchObj = re.search(r'- parking to wait for  <(.*)> .*', line, re.M | re.I)
            if searchObj:
                # print "thread name : " + tName
                # print "searchObj.group() : ", searchObj.group()
                # print "lockId : ", searchObj.group(1)
                if searchObj.group(1) in lockMap:
                    print "exist " + searchObj.group(1) +" " + tName
                else:
                    lockMap[searchObj.group(1)] = tName

        # print line
    text_file.close()
    print lockMap
if __name__ == '__main__':
    helloWorld()