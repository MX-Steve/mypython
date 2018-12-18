# no1
# import re
# from collections import Counter
# class PattCount:
#     def __init__(self,patt):
#         self.patt=re.compile(patt)
#
#     def countPatt(self,fname):
#         result=Counter()
#         with open(fname) as fobj:
#             for line in fobj:
#                 m=self.patt.search(line)
#                 if m:
#                     result.update([m.group()])
#         return result
#
# if __name__ == '__main__':
#     fname="access_log"
#     ip='(\d+\.){3}\d+'
#     br="Firefox|Chrome|MSIE"
#     pc=PattCount(ip)
#     access=pc.countPatt(fname)
#     print(access)
#     print(access.most_common(3))

# no2

# import re
# from collections import Counter
#
# class PattCount:
#     def __init__(self,patt):
#         self.cpatt=re.compile(patt)
#
#     def Count(self,fname):
#         result=Counter()
#         with open(fname) as fobj:
#             for line in fobj:
#                 m=self.cpatt.search(line)
#                 if m:
#                     result.update([m.group()])
#         return result
#
# if __name__ == '__main__':
#     fname="access_log"
#     ip="^(\d+\.){3}\d+"
#     br="Chrome|Firefox|MSIE"
#     pc=PattCount(ip)
#     print(pc.Count(fname))
#     print(pc.Count(fname).most_common(3))

# # no3
# import re
# from collections import Counter
#
# class CountPatt:
#     def __init__(self,patt):
#         self.cpatt=re.compile(patt)
#
#     def count(self,fname):
#         result=Counter()
#         with open(fname) as fobj:
#             for line in fobj:
#                 m=self.cpatt.search(line)
#                 if m:
#                     result.update([m.group()])
#         return result
#
# if __name__ == '__main__':
#     fname="access_log"
#     ip="^(\d+\.){3}\d+"
#     cp=CountPatt(ip)
#     aa=cp.count(fname)
#     print(aa)
#     print(aa.most_common(3))

