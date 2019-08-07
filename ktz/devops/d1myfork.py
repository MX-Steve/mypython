import os

#print('starting....')
#os.fork()
#print('hello world')

#print('staring...')
#retval=os.fork()
#if retval:
#    print('in parent')
#else:
#    print('in child')
#print('hello from both')


#print('staring...')
#retval=os.fork()
#if retval:
#    print('in parent')
#else:
#    print('in child')
#    exit(0)
#print('hello from both')

print('starting...')
for i in range(3):
  retval=os.fork()
  if not retval:
    print('hello world!')
    exit(0)

print('Done')
