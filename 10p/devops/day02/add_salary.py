from sqlalchemy_usage import Salary, Session


session = Session()
# session.add(zs)
# ops=[ls,ww,zl,bb,shis]
# session.add_all(ops)

a1 = Salary(auto_id=1,date='20180910',emp_id=1,basic=5000,awards=2000)
a2 = Salary(auto_id=2,date='20180910',emp_id=2,basic=10000,awards=4000)
a3 = Salary(auto_id=3,date='20180910',emp_id=3,basic=5500,awards=1200)
a4 = Salary(auto_id=4,date='20180910',emp_id=4,basic=4500,awards=3000)
a5 = Salary(auto_id=5,date='20180910',emp_id=5,basic=3000,awards=5000)
a6 = Salary(auto_id=6,date='20180910',emp_id=6,basic=8000,awards=1000)

ops=[a1,a2,a3,a4,a5,a6]
session.add_all(ops)

session.commit()
session.close()