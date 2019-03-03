#生成器也是函数,只是常规函数通过return返回一个值,而生成器可以通过yield返回很多中间结果

def mygen():
    yield 'hello'
    a = 10+20
    yield a
    yield [1,2,3]

if __name__=='__main__':
  m=mygen()
  for i in m:
    print(i)

  for i in m:
    print(i)  # 无值，因为生成器对象只能用一次
