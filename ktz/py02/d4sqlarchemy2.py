from d4sqlarchemy1 import Session , Departments, Employees , Salary

session=Session()

hr=Departments(dep_id=1,dep_name='renshibu')
yunwei=Departments(dep_id=2,dep_name='yunweibu')
kaifa=Departments(dep_id=3,dep_name='kaifabu')
ceshi=Departments(dep_id=4,dep_name='ceshibu')
caiwu=Departments(dep_id=5,dep_name='caiwubu')
shichang=Departments(dep_id=6,dep_name='shichangbu')
xiaoshou=Departments(dep_id=7,dep_name='xiaoshoubu')

deps=[hr,yunwei,kaifa,ceshi,caiwu,shichang,xiaoshou]
session.add_all(deps)
session.commit()

session.close()


