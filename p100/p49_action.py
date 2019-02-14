import time
import os

length=19
count=0

while True:
  os.system('clear')
  print('\r%s@%s'%("#"*count,"#"*(length-count)))
  try:
    time.sleep(0.3)
  except KeyboardInterrupt:
    print('\nBye-bye')
    break
  if count == length:
    count=0
  count+=1

