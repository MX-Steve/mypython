import re
import collections


def get_nums(file,patt):
    cpatt=re.compile(patt)
    counter=collections.Counter()
    with open(file) as fobj:
        for item in fobj:
            p=cpatt.search(item)
            if p:
                counter.update([p.group()])
                # counter.most_common(3)
    return counter

def main():
    file='/opt/ktz/py02/2019071012.log'
    ip='(\d+.){3}\d+'
    result=get_nums(file,ip)
    # result=result.most_common(3)
    br_patt = "Firefox|MSIE|Chrome"
    brs=get_nums(file,br_patt)
    for item in brs:
        print(item,brs[item])
    for item in result:
        print(item,result[item])



if __name__ == '__main__':
    main()
    # os , sys , subprocess , getpass , string , time , datetime , shutil , functools , re , collections , random