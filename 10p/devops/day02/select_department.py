from sqlalchemy_usage import Departments, Session, Employees



session=Session()

for instance in session.query(Departments).order_by(Departments.dep_id):
    print(instance.dep_id,instance.dep_name)

for name,phone in session.query(Employees.name,Employees.phone):
    print("%s:%s"%(name,phone))

for raw  in session.query(Departments.dep_name.label('depname')):
    print(raw.depname)

qset = session.query(Employees.name,Employees.email).order_by(Employees.emp_id)[3:5]
print(qset)

qset = session.query(Employees.name).filter(Employees.emp_id<=3).filter(Employees.gender=='girl')
for i in qset:
    print(i)

qset = session.query(Employees.name).filter(Employees.name.like('%i%'))
for i in qset:
    print(i)

qset = session.query(Employees.name).filter(Employees.name.in_(['lisi','zhangsan']))
for i in qset:
    print(i.name)

qset = session.query(Employees.name).filter(~Employees.name.in_(['lisi','zhangsan']))
for i in qset:
    print(i.name)

qset = session.query(Employees.name).filter(Employees.name.isnot(None))
print(qset)
for name in qset:
    print(name)

session.commit()
session.close()