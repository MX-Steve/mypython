import pymysql

conn=pymysql.connect(
    host='192.168.4.14',
    port=3306,
    user='lihan',
    passwd='123456',
    db='nsd1903',
    charset='utf8'
)

cursor=conn.cursor()

create_dep="""CREATE TABLE department(
dep_id INT,
dep_name VARCHAR(20),
PRIMARY KEY(dep_id)

)"""

create_emp="""CREATE TABLE employees(
emp_id INT,
emp_name VARCHAR(20),
birth_date DATE,
phone VARCHAR(11),
email VARCHAR(50),
dep_id INT,
PRIMARY  KEY(emp_id),
FOREIGN KEY(dep_id) REFERENCES department(dep_id)
)"""

create_sal="""CREATE TABLE salary(
id INT,
date DATE,
emp_id INT,
basic INT,
awards INT,
PRIMARY KEY(id),
FOREIGN KEY(emp_id) REFERENCES employees(emp_id)
)"""

cursor.execute(create_dep)
cursor.execute(create_emp)
cursor.execute(create_sal)

conn.commit()

cursor.close()
conn.close()