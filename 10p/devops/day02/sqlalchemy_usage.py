from  sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
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


if __name__ == '__main__':
    Base.metadata.create_all(engine)