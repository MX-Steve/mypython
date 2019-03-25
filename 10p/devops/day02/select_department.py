from sqlalchemy_usage import Departments, Session



session=Session()

for instance in session.query(Departments).order_by(Departments.dep_id):
    print(instance.dep_id,instance.dep_name)


session.commit()
session.close()