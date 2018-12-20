from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String , Date, ForeignKey

engine=create_engine(
    'mysql+pymysql://root:123456@localhost/tedu?charset=utf8',
    encoding='utf8',
    echo=True
)
Base=declarative_base() #ORM

class Departments(Base):
    __tablename__="departments"
    dep_id = Column(Integer, primary_key=True)
    dep_name = Column(String(20),unique=True, nullable=False)


    def __str__(self):
        return "<dep:%s>" % self.dep_name

class Employees(Base):
    __tablename__="employees"
    emp_id=Column(Integer,primary_key=True)
    emp_name=Column(String(20),unique=True,nullable=False)
    gender = Column(String(6))
    birth_date = Column(Date)
    phone = Column(String(11))
    email = Column(String(50))
    dep_id = Column(Integer, ForeignKey('departments.dep_id'))

    def __str__(self):
        return "<emp:%s>" % self.emp_name

class Salary(Base):
    __tablename__="salary"
    auto_id = Column(Integer, primary_key=True)
    emp_id = Column(Integer,ForeignKey("employees.emp_id"))
    salary_date = Column(Date)
    basic = Column(Integer)
    awards = Column(Integer)

if __name__ == '__main__':
    Base.metadata.create_all(engine)