from d4sqlarchemy1 import Session , Departments , Employees

session=Session()
#qset1=session.query(Departments)
#print(qset1)
#print(list(qset1))
#for dep in qset1:
#  print("部门ID：%s，部门名称：%s"%(dep.dep_id,dep.dep_name))

#qset2=session.query(Employees.emp_name,Employees.email)
#print(qset2)
#print(list(qset2))

#qset3=session.query(Departments).order_by(Departments.dep_id)
#for dep in qset3:
#  print(dep.dep_id,dep.dep_name)

#qset4=session.query(Departments).order_by(Departments.dep_id)[2:4]
#for dep in qset4:
#  print(dep.dep_id,dep.dep_name)

#qset5=session.query(Departments).filter(Departments.dep_id==2)
#for emp in qset5:
#  print(emp.dep_name)

#qset6=session.query(Departments).filter(Departments.dep_id>=2).filter(Departments.dep_name.like('c%'))
#for emp in qset6:
#  print(emp.dep_name)

#all fanhui liebiao

#qset7=session.query(Departments).filter(Departments.dep_id>=2).filter(Departments.dep_name.like('c%'))
#print(qset7.all())
#print(qset7.first())
#dep=qset7.first()
#print(dep.dep_id,dep.dep_name)

#qset8 = session.query(Employees.emp_name,Departments.dep_name)\
#    .join(Departments)
#for item in qset8:
#    print(item)

#qset8 = session.query(Departments.dep_name,Employees.emp_name)\
#    .join(Employees)
#for item in qset8:
#    print(item)

#qset10 = session.query(Departments).filter(Departments.dep_name=='renshibu')
#hr=qset10[0]
#hr.dep_name='renliziyuanbu'
#session.commit() # insert , update , delete need it.

qset11 = session.query(Departments).filter(Departments.dep_id==7)
sales=qset11[0]
session.delete(sales)
session.commit()

session.close()


