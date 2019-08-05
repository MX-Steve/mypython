import re
# import collections

class CountPatt:
    def __init__(self,fname):
        self.fname=fname

    def get_nums(self,patt):
        cpatt=re.compile(patt)
        # counter=collections.Counter()
        patt_dict={}
        with open(self.fname) as fobj:
            for item in fobj:
                p=cpatt.search(item)
                if p:
                    key=p.group()
                    patt_dict[key]=patt_dict.get(key,0)+1
                    # counter.update([p.group()])
                    # counter.most_common(3)
        return patt_dict



if __name__ == '__main__':
    fname='/opt/ktz/py02/2019071012.log'
    ip='(\d+\.){3}\d+'
    br='Firefox|MSIE|Chrome'
    cp=CountPatt(fname)
    ip_count=cp.get_nums(ip)
    # ip_count=get_nums(fname,ip)
    # br_count=get_nums(fname,br)
    print(ip_count)
    # print(br_count)
    userfile='/etc/passwd'
    shell='bash$'
    cp2=CountPatt(userfile)
    print(cp2.get_nums(shell))

