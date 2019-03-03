#!/usr/bin/env python3

# 引入相关模块
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String , Date, ForeignKey, Enum
from sqlalchemy.orm import sessionmaker


# 创建连接数据的引擎
engine=create_engine(
    'mysql+pymysql://ktzlh:lihanqqq12345@localhost/kaituozhe?charset=utf8',
    encoding='utf8'
    # echo=True # 关闭测试日志
)

# 创建会话对象，用来对数据进行增删改查
Session=sessionmaker(bind=engine)

# 创建orm基建,对象关系映射  class ==> table
Base=declarative_base() #ORM

# 创建数据库中表，以类形式展示
#===================  departments  =============================
class Departments(Base):
    __tablename__="departments"
    dep_id = Column(Integer,primary_key=True)
    dep_name = Column(String(20),unique=True,nullable=True)

    def __str__(self):
        return '<dep:%s>'%self.dep_name

# data of departments
# session=Session()
kf=Departments(dep_id=1,dep_name='开发部')
yw=Departments(dep_id=2,dep_name='运维部')
cs=Departments(dep_id=3,dep_name='测试部')
xs=Departments(dep_id=4,dep_name='销售部')
xz=Departments(dep_id=5,dep_name='行政部')
rs=Departments(dep_id=6,dep_name='人事部')
sc=Departments(dep_id=7,dep_name='市场部')
deps=[kf,yw,cs,xs,xz,rs,sc]
# session.add_all(deps)
# session.commit()
# session.close()

#===================  employees  =============================
class Employees(Base):
    __tablename__="employees"
    emp_id      = Column(Integer,primary_key=True)
    emp_name    = Column(String(20),nullable=True)
    gender      = Column(Enum('M','W'),nullable=True)
    birthday    = Column(Date,nullable=True)
    phone       = Column(String(11),unique=True,nullable=True)
    email       = Column(String(20),unique=True,nullable=True)
    dep_id      = Column(Integer, ForeignKey('departments.dep_id'))

    def __str__(self):
        return "<emp:%s>"%self.emp_name

# data of employees
emps=[
    Employees(emp_id=1,emp_name='张杰',gender='M',birthday='1991-01-27',phone='18251985630',email='njzj@ktz.cn',dep_id=1),
    Employees(emp_id=2,emp_name='石松',gender='M',birthday='1990-11-02',phone='13252985367',email='njss@ktz.cn',dep_id=1),
    Employees(emp_id=3,emp_name='石腾腾',gender='W',birthday='1987-11-27',phone='18262625689',email='stt@ktz.cn',dep_id=3),
    Employees(emp_id=4,emp_name='蒋荣',gender='W',birthday='1995-12-02',phone='15259985358',email='njjr@ktz.cn',dep_id=3),
    Employees(emp_id=5,emp_name='李韩',gender='M',birthday='1991-06-02',phone='15259989610',email='njlh@ktz.cn',dep_id=2),
    Employees(emp_id=6,emp_name='徐文锦',gender='M',birthday='1997-10-12',phone='13289875315',email='xwj@ktz.cn',dep_id=2),
    Employees(emp_id=7,emp_name='壬秦',gender='M', birthday='1991-01-27',phone='18252985685',email='renqin@ktz.cn',dep_id=4),
    Employees(emp_id=8,emp_name='杨孝南',gender='M',birthday='1993-11-02',phone='13252985369',email='yangxn@ktz.cn',dep_id=4),
    Employees(emp_id=9,emp_name='王国柱',gender='W',birthday='1988-11-15',phone='18262925679',email='wanggz@ktz.cn',dep_id=5),
    Employees(emp_id=10,emp_name='宋朝',gender='W',birthday='1993-5-17',phone='18259985368',email='njsc@ktz.cn',dep_id=6),
    Employees(emp_id=11,emp_name='王菲',gender='W',birthday='1995-4-22',phone='18262629870',email='wangfei@ktz.cn',dep_id=6),
    Employees(emp_id=12,emp_name='钱莉',gender='W',birthday='1993-1-12',phone='19262628970',email='qianli@ktz.cn',dep_id=7)
]

#===================  servers groups  ======================
class ServerGroup(Base):
    __tablename__   =  "sergrps"
    sergrp_id       = Column(Integer,primary_key=True)
    sergrp_name     = Column(String(35),unique=True,nullable=True)

# data of servers groups

sgs = [
    ServerGroup(sergrp_id=1,sergrp_name='zabbixs'),
    ServerGroup(sergrp_id=2,sergrp_name='webs'),
    ServerGroup(sergrp_id=3,sergrp_name='dbs'),
    ServerGroup(sergrp_id=4,sergrp_name='proxys'),
    ServerGroup(sergrp_id=5,sergrp_name='storages')
]


#===================  servers  =============================
class Servers(Base):
    __tablename__="servers"
    server_id   = Column(Integer, primary_key=True)
    server_name = Column(String(35),unique=True,nullable=True)
    cpus        = Column(Integer,nullable=True)
    memery      = Column(Integer,nullable=True)
    storage     = Column(Integer,nullable=True)
    sergrp_id   = Column(Integer,ForeignKey('sergrps.sergrp_id'))

# data of Servers
servers = [
    Servers(server_id=1,server_name='zabbix01',cpus=4,memery=8,storage=500,sergrp_id=1),
    Servers(server_id=2,server_name='zabbix02',cpus=4,memery=8,storage=500,sergrp_id=1),
    Servers(server_id=3,server_name='nginx01',cpus=2,memery=8,storage=500,sergrp_id=2),
    Servers(server_id=4,server_name='nginx02',cpus=2,memery=8,storage=500,sergrp_id=2),
    Servers(server_id=5,server_name='nginx03',cpus=2,memery=4,storage=500,sergrp_id=2),
    Servers(server_id=6,server_name='nginx04',cpus=2,memery=4,storage=500,sergrp_id=2),
    Servers(server_id=7,server_name='mm01',cpus=2,memery=4,storage=2000,sergrp_id=3),
    Servers(server_id=8,server_name='mm02',cpus=2,memery=4,storage=2000,sergrp_id=3),
    Servers(server_id=9,server_name='mm03',cpus=2,memery=4,storage=2000,sergrp_id=3),
    Servers(server_id=10,server_name='ms01',cpus=2,memery=4,storage=2000,sergrp_id=3),
    Servers(server_id=11,server_name='ms02',cpus=2,memery=4,storage=2000,sergrp_id=3),
    Servers(server_id=12,server_name='pro01',cpus=4,memery=8,storage=500,sergrp_id=4),
    Servers(server_id=13,server_name='pro02',cpus=4,memery=8,storage=500,sergrp_id=4),
    Servers(server_id=14,server_name='st01',cpus=2,memery=4,storage=10000,sergrp_id=5),
    Servers(server_id=15,server_name='st02',cpus=2,memery=4,storage=10000,sergrp_id=5)
]

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    session=Session()
    # session.add_all(deps)
    # # session.commit()
    # session.add_all(emps)

    session.add_all(sgs)
    session.commit()
    session.add_all(servers)

    session.commit()
    session.close()