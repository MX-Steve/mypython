# no1
# import re
#
# def count_patt(fname,patt):
#     patt_adict={}
#     cpatt=re.compile(patt)
#     with open(fname) as fobj:
#         for line in fobj:
#             m = cpatt.search(line)
#             if m:
#                 key = m.group()
#                 patt_adict[key]=patt_adict.get(key,0)+1
#     return patt_adict
#
# if __name__ == '__main__':
#     fname="access_log"
#     ip='^(\d+\.){3}\d+'
#     print(count_patt(fname,ip))
#     br='Chrome|Firefox|MSIE'
#     print(count_patt(fname,br))

# no2
# import re
# def count_patt(fname,patt):
#     patt_dict={}
#     cpatt=re.compile(patt)
#     with open(fname) as fobj:
#         for line in fobj:
#             m=cpatt.search(line)
#             if m:
#                 key=m.group()
#                 patt_dict[key]=patt_dict.get(key,0)+1
#     return patt_dict
#
# if __name__ == '__main__':
#     fname="access_log"
#     ip='^(\d+\.){3}\d+'
#     print(count_patt(fname,ip))
#     br='Chrome|MSIE|Firefox'
#     print(count_patt(fname,br))

# no3
#
# import re
# def count_patt(fname,patt):
#     cpatt=re.compile(patt)
#     patt_dict={}
#     with open(fname) as fobj:
#         for line in fobj:
#             m=cpatt.search(line)
#             if m:
#                 key = m.group()
#                 patt_dict[key]=patt_dict.get(key,0)+1
#     return patt_dict
#
#
# if __name__ == '__main__':
#     fname="access_log"
#     ip='^(\d+\.){3}\d+'
#     print(count_patt(fname,ip))
#     br="Chrome|MSIE|Firefox"
#     print(count_patt(fname,br))

# no4
# import re
# def count_patt(fname,patt):
#     cpatt=re.compile(patt)
#     patt_dict={}
#     with open(fname) as fobj:
#         for line in fobj:
#             m=cpatt.search(line)
#             if m:
#                 key=m.group()
#                 patt_dict[key]=patt_dict.get(key,0) +1
#     return patt_dict
#
# if __name__ == '__main__':
#     fname="access_log"
#     ip='^(\d+\.){3}\d+'
#     print(count_patt(fname,ip))
#     br="Chrome|Firefox|MSIE"
#     print(count_patt(fname,br))

# no5

import re
def count_patt(fname,patt):
    cpatt=re.compile(patt)
    patt_dict={}
    with open(fname) as fobj:
        for line in fobj:
            m=cpatt.search(line)
            if m:
                key=m.group()
                patt_dict[key]=patt_dict.get(key,0) +1
    return patt_dict

if __name__ == '__main__':
    fname="access_log"
    ip='^(\d+\.){3}\d+'
    print(count_patt(fname,ip))
    br="Firefox|Chrome|MSIE"
    print(count_patt(fname,br))
