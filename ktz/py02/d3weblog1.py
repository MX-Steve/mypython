import re
# import collections


def get_nums(file,patt):
    cpatt=re.compile(patt)
    # counter=collections.Counter()
    patt_dict={}
    with open(file) as fobj:
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
    ip_count=get_nums(fname,ip)
    br_count=get_nums(fname,br)
    print(ip_count)
    print(br_count)

