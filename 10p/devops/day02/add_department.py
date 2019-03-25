from sqlalchemy_usage import Departments, Session


hr = Departments(dep_id=1,dep_name='hr')
print(hr.dep_id,hr.dep_name)
ops=Departments(dep_id=2,dep_name="operations")
dev = Departments(dep_id=3,dep_name="developments")
finance=Departments(dep_id=4,dep_name="caiwubu")
jiaoxue=Departments(dep_id=5,dep_name="教学")
devops=[ops,dev]
session=Session()
# session.add(hr)
# session.add_all(devops)
session.add(jiaoxue)
session.commit()
session.close()