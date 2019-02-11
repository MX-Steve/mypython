#计算100以内偶数的和
sum100=0
counter=0
while counter <=100:
  counter +=1
  if counter % 2 == 1:
    continue
  sum100+=counter

print(sum100)
