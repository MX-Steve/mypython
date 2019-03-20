#!/usr/bin/env python3
"patt->ip/br"
import re
def count_patt(patt,log):
    cpatt = re.compile(patt)
    result={}
    with open(log,'r') as fobj:
        for item in fobj:
            m=cpatt.search(item)
            # print(type(key))
            if not m:
                break
            key=m.group()
            # if key not in result:
            #     result[key]=1
            # else:
            #     result[key]=result.get(key) + 1
            result[key]=result.get(key,0)+1
    return result

if __name__ == '__main__':
    ip="^(\d+\.){3}\d+"
    br="Chrome|MSIE|FireFox"
    log="access_log"
    print(count_patt(ip,log))