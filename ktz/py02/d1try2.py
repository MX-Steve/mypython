"make error myself"

# def set_age(name,age):
#     if not 0 < age < 120:
#         raise ValueError("out of range")
#         # print("out of range")
#     print("%s:%s"%(name,age))
#
# if __name__ == '__main__':
#     set_age('tom',29)
#     set_age('tom1',219)


def set_age2(name,age):
    assert 0<age<120,"out of range"
    print("%s:%s"%(name,age))

if __name__ == '__main__':
    set_age2('tom',20)
    set_age2('tom',220)

# sys , os , getpass , string , random , subprocess , shutil , shutil