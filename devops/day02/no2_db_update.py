from no2_db_connect import  Departments, Session

session = Session()

q1=session.query(Departments).filter(Departments.dep_name=="renshi")
dep=q1.one()
print(dep)
dep.dep_name="renliziyuanbu"
session.commit()
session.close()