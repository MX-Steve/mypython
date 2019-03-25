from sqlalchemy_usage import Employees, Session

zs= Employees(emp_id=1,name="zhangsan",gender='boy',phone='18262629780',email='zhangsan@163.com',dep_id=1)
ls= Employees(emp_id=2,name="lisi",gender='girl',phone='18262629781',email='lisi@163.com',dep_id=1)
ww= Employees(emp_id=3,name="wangwu",gender='boy',phone='18262629782',email='wangwu@163.com',dep_id=2)
zl= Employees(emp_id=4,name="zhaoliu",gender='boy',phone='18262629783',email='zhaoliu@163.com',dep_id=3)
bb= Employees(emp_id=5,name="benben",gender='girl',phone='18262629784',email='benben@163.com',dep_id=4)
shis= Employees(emp_id=6,name="shisong",gender='boy',phone='18262629785',email='shisong@163.com',dep_id=5)
session = Session()
# session.add(zs)
ops=[ls,ww,zl,bb,shis]
session.add_all(ops)





session.commit()
session.close()