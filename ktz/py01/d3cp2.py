import sys


def copy(f1,f2):
    with open(f1,'rb') as f1:
        with open(f2,'wb') as f2:
            while True:
                data=f1.read(4096)
                if not data:
                    break
                f2.write(data)

if __name__ == '__main__':
    copy(sys.argv[1],sys.argv[2])