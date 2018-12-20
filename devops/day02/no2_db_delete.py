from no2_db_connect import  Departments, Session

session = Session()

q1=session.query(Departments).filter(Departments.dep_name=="caiwu")
dep=q1.one()
print(dep)
session.delete(dep)
session.commit()
session.close()