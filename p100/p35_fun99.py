def fun99(n):
  for i in range(1,n+1):
    for j in range(1,i+1):
      print("%s*%s=%s"%(j,i,j*i), end="  ")
    print()

fun99(5)
fun99(6)
fun99(7)
fun99(9)
