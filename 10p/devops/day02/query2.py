from sqlalchemy_usage import Departments,Employees , Salary, Session
from sqlalchemy import and_, or_

session = Session()

# qset = session.query(Employees.name).filter(and_(Employees.dep_id==2,Employees.gender=='girl'))
# print(qset)
# for name in qset:
#     print(name)
################################################################
# qset = session.query(Employees.name).filter(or_(Employees.dep_id==2,Employees.gender=='girl'))
# print(qset)
# for name in qset:
#     print(name)
################################################################
# qset = session.query(Employees.name,Employees.phone)
# print(qset.all())
#
# qset = session.query(Employees.name,Employees.phone).filter(Employees.emp_id==1)
# print(qset.one())
# print(qset.scalar())
################################################################
qset = session.query(Employees).count()
print(qset)

qset = session.query(Employees.name,Departments.dep_name).join(Employees,Departments.dep_id==Employees.dep_id)
print(qset.all())



session.close()