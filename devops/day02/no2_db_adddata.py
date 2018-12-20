from no2_db_connect import Departments , Session , Employees

session = Session()
# hr = Departments(dep_id=1, dep_name='renshi')
# # session.add(hr)
# ops=Departments(dep_id=2,dep_name="yunwei")
# dev=Departments(dep_id=3,dep_name="kaifa")
# devops=Departments(dep_id=4,dep_name="devops")
# finance=Departments(dep_id=5,dep_name="caiwu")
# deps = [ops,dev]
# # session.add_all(deps)
# deps1 = [devops,finance]
# session.add_all(deps1)

zjh=Employees(
    emp_id=15,
    emp_name='lisi',
    gender="nan",
    birth_date='1991-05-16',
    phone='18262628888',
    email='zjh@163.com',
    dep_id=5
)
zs=Employees(
    emp_id=16,
    emp_name='z3',
    gender="nan",
    birth_date='1991-08-16',
    phone='13262628888',
    email='zjh@163.com',
    dep_id=3
)
session.add_all([zjh,zs])


session.commit()
session.close()
