from sqlalchemy_usage import Session,Departments

session = Session()
q1 = session.query(Departments).filter(Departments.dep_id==2)
print(q1.all())
q1.update({Departments.dep_name:"yunweibu"})

dev = session.query(Departments).get(4)
dev.dep_name="money bu"

session.commit()
session.close()