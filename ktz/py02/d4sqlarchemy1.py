from sqlalchemy import create_engine , Column , Integer, String , Date , ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine=create_engine(
    'mysql+pymysql://lihan:123456@192.168.4.14/tedu1903?charset=utf8',
    encoding='utf8',
    #echo=True
)

Base=declarative_base()
Session=sessionmaker(bind=engine)


class Departments(Base):
    __tablename__='departments'
    dep_id=Column(Integer,primary_key=True)
    dep_name=Column(String(20),unique=True)

class Employees(Base):
    __tablename__='employees'
    emp_id=Column(Integer,primary_key=True)
    emp_name=Column(String(20))
    birth_date=Column(Date)
    email=Column(String(30))
    dep_id=Column(Integer,ForeignKey('departments.dep_id'))

class Salary(Base):
    __tablename__="salary"
    id=Column(Integer,primary_key=True)
    date = Column(Date)
    emp_id = Column(Integer,ForeignKey('employees.emp_id'))
    basic=Column(Integer)
    awards=Column(Integer)



if __name__ == '__main__':
    Base.metadata.create_all(engine)