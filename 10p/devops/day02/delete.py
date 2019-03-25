from sqlalchemy_usage import Session,Departments

session = Session()

# xz = Departments(dep_id=6,dep_name='xingzheng')
# session.add(xz)

xz = session.query(Departments).get(6)
session.delete(xz)


session.commit()
session.close()