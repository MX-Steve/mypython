#!/usr/bin/env python3
"100/x"
#num=int(input('num:'))
#result=100/num
#'ValueError --> not a num'
#KeyboardInterrupt --> ctrl + c
#EOFError --> ctrl + d
# ZeroDivisionError --> 0

try:
    num=int(input('num>'))
    result=100/num
except (KeyboardInterrupt, EOFError):
    print('Bye-Bye')
except ZeroDivisionError:
    print('not 0')
except ValueError:
    print('input a num')
else:
    print(result)
finally:
    print('Done')

print('end of file')