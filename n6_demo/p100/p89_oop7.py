class Date:
  def __init__(self,year,month,date):
    self.year=year
    self.month=month
    self.date=date

  @classmethod #类方法，不用创建实例即可调用
  def create(cls,dstr): # cls表示类本身，class的缩写
    y,m,d=map(int,dstr.split('-')) #map(init,['2000','5','4'])
    dt=cls(y,m,d) # 即Date(y,m,d)
  
  @staticmethod #静态方法，写在类的外面，可以独立成为一个函数，硬把他放在类中
  def is_date_valid(dstr):
    y,m,d = map(int,dstr.split('-'))
    return 1<=d<=31 and 1<=m<=12 and y < 4000

if __name__=="__main__":
  birth_date=Date(1995,12,3)
  print(Date.is_date_valid('2000-5-4'))
  day=Date.create('2000-5-4')
  print(day)
