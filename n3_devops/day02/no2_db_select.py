from no2_db_connect import Departments , Session

session = Session()
query1 = session.query(Departments)
# print(query1)
# for dep in query1:
#     print("%s -> %s"%(dep.dep_id,dep.dep_name))

query2 = session.query(Departments.dep_id,Departments.dep_name)
# print(query2)
# for dep in query2:
#     print(dep)
#
# for dep_id,dep_name in query2:
#     print("%s -> %s"%(dep_id,dep_name))

query3 = session.query(Departments.dep_name.label('bumen')) #bie ming
# print(query3)
# for dep in query3:
#     print(dep.bumen)

query4 = session.query(Departments).order_by(Departments.dep_id)
# print(query4)
# for dep in query4:
#     print(dep)
#     print('%s -> %s' %(dep.dep_id,dep.dep_name))

query5=session.query(Departments).order_by(Departments.dep_id)[1:3] # qie pian , ta bu shi sql yu ju
# for dep in query5:
#     print(dep)
#     print('%s -> %s' %(dep.dep_id,dep.dep_name))

query6 = session.query(Departments).filter(Departments.dep_id == 3)
# print(query6)
# for dep in query6:
#     print(dep.dep_id, dep.dep_name)

query7 = session.query(Departments).filter(Departments.dep_id >=2).filter(Departments.dep_id<=4)
# print(query7)

query8 = session.query(Departments).filter(Departments.dep_name.in_(['caiwu','renshi'])) # zai ... li
# print(query8)
# for dep in query8:
#     print(dep.dep_id,dep.dep_name)

query9 = session.query(Departments).filter(~Departments.dep_name.in_(['caiwu','renshi']))  #qufan ~
# print(query9)
# for dep in query9:
#     print(dep.dep_id,dep.dep_name)

from sqlalchemy import and_, or_
from no2_db_connect import Employees

query10 = session.query(Departments).filter(and_(Departments.dep_id >=2 , Departments.dep_id <=4))

# for dep in query10:
#     print(dep.dep_id,dep.dep_name)

query11 = session.query(Departments).filter(or_(Departments.dep_id ==2 , Departments.dep_id ==4))
# for dep in query11:
#     print(dep.dep_id,dep.dep_name)

query12 = session.query(Departments)
# print(query12.all())
# print(query12.first())

query13 = session.query(Departments.dep_id,Departments.dep_name).filter(Departments.dep_id>4)
# print(query13.one())
# print(query13.scalar())

query14 = session.query(Departments)
print(query14.count())

#==================================== duo biao cha xun ===========================================
query15 = session.query(Employees.emp_name, Departments.dep_name).join(Departments, Employees.dep_id == Departments.dep_id)
print(query15.all())