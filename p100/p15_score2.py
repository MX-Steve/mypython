score=int(input("分数："))

if score >=60 and score <=70:
  print("一般")
elif score >70 and score <=90:
  print("良好")
elif score >90 and score <=100:
  print("优秀")
elif score >=0 and score <60:
  print("差")
else:
  print("请输入正确分数")
