try:
  n = int(input('number:'))
  result=100/n
  print(result)
except ValueError:
  print('\033[31;1minvalid number\033[0m')
except ZeroDivisionError:
  print('\033[31;1m0 not allowed\033[0m')
except EOFError:
  print('\033[33;1mBye-Bye\033[0m')
except KeyboardInterrupt:
  print('\033[33;1mBye-Bye\033[0m')
print('\033[32mDone\033[0m')
