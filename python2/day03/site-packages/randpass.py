from string import ascii_letters,digits
from random import  choice

def randpass(n=8):
    all_chs=ascii_letters + digits
    result = [choice(all_chs) for i in range(n)]
    return ''.join(result)

#sys.path
# site-packages , huo zhe shi yong sys.path dingyi
#PYTHONPATH



if __name__ == '__main__':
    print(randpass())
    print(randpass(10))
    print(randpass(12))