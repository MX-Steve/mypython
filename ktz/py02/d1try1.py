# try:
#     num=int(input("number: "))
#     result = 100/num
#     print(result)
#     print("Done")
# except ValueError:
#     print("value error")
# except ZeroDivisionError:
#     print("value not right")
# except KeyboardInterrupt:
#     print("\nBye-bye")
# except EOFError:
#     print('\nBye-bye')
#
# try:
#     num=int(input("number: "))
#     result = 100/num
#     print(result)
#     print("Done")
# except (ValueError, ZeroDivisionError):
#     print("value error")
# except (KeyboardInterrupt,EOFError):
#     print('\nBye-bye')
#

# try:
#     num=int(input("number: "))
#     result = 100/num
# except (ValueError, ZeroDivisionError):
#     print("value error")
# except (KeyboardInterrupt,EOFError):
#     print('\nBye-bye')
#     exit(1)
# else:
#     print(result)
# finally:
#     print("finally")
#
# print("normal funished")

try:
    num=int(input("number: "))
    result = 100/num
except (ValueError, ZeroDivisionError) as e:
    print("value error: ",e)
except (KeyboardInterrupt,EOFError):
    print('\nBye-bye')
    exit(1)
else:
    print(result)
finally:
    print("finally")

print("normal funished")