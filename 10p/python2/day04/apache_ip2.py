#!/usr/bin/env python3
"patt->ip/br"
import re
# import collections

class CountPatt:
    def __init__(self,patt,fname):
        self.fname=fname
        self.cpatt=re.compile(patt)
    def count_patt(self):
        result={}
        with open(self.fname,'r') as fobj:
            for line in fobj:
                m = self.cpatt.search(line)
                if m:
                    key=m.group()
                    result[key]=result.get(key,0)+1
        return result

if __name__ == '__main__':
    ip = "^(\d+\.){3}\d+"
    br = "Chrome|MSIE|Firefox"
    log = "access_log"
    cp1=CountPatt(ip,log)
    print(cp1.count_patt())
    cp2=CountPatt(br,log)
    print(cp2.count_patt())
