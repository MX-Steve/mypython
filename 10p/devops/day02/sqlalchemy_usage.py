from  sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,Date,ForeignKey
from sqlalchemy.orm import sessionmaker


engine = create_engine(
    'mysql+pymysql://root:123456@176.4.16.101/tarena?charset=utf8',
    encoding='utf8',
    echo=True
)

Base=declarative_base()
Session = sessionmaker(bind=engine)

class Departments(Base):
    __tablename__="departments"
    dep_id = Column(Integer,primary_key=True)
    dep_name = Column(String(20),nullable=False,unique=True)

    def __str__(self):
        return "department id :%s, department name : %s"%(self.dep_id,self.dep_name)

class Employees(Base):
    __tablename__="employees"
    emp_id=Column(Integer,primary_key=True)
    name=Column(String(20),nullable=False,unique=True)
    gender=Column(String(6))
    # birth_date=Column(Date)
    phone=Column(String(11),nullable=False,unique=True)
    email = Column(String(30),nullable=False,unique=True)
    dep_id = Column(Integer,ForeignKey('departments.dep_id'))

    def __str__(self):
        return "dep_name: %s"%self.name

class Salary(Base):
    __tablename__="salary"
    auto_id = Column(Integer,primary_key=True)
    date = Column(Date)
    emp_id=Column(Integer,ForeignKey('employees.emp_id'))
    basic = Column(Integer)
    awards=Column(Integer)
    def __str__(self):
        return "emp_id: %s : %s"%(self.emp_id,self.basic)


if __name__ == '__main__':
    Base.metadata.create_all(engine)