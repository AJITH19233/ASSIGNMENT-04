#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install mysql-connector-python')


# In[2]:


import mysql.connector


# In[3]:


con=mysql.connector.connect(
host="localhost",
user="root",
password="",
database="ems"
)
def insertion(emp_id,emp_name,emp_salary,emp_department,email):
    res=con.cursor()
    sql="insert into employee(emp_id,emp_name,emp_salary,emp_department,email)values(%s,%s,%s,%s,%s)"
    user=(emp_id,emp_name,emp_salary,emp_department,email)
    res.execute(sql,user)
    con.commit()
    print("=====INSERTED SUCCESFUL======")
def update(emp_name,emp_salary,emp_department,email,emp_id):
    res=con.cursor()
    sql="update employee set emp_name = %s,emp_salary = %s,emp_department = %s,email = %s where emp_id=%s"
    data=(emp_name,emp_salary,emp_department,email,emp_id)
    res.execute(sql,data)
    con.commit()
    print("==========UPDATED SUCCESFUL===========")
def display():
    res=con.cursor()
    sql="select * from employee"
    res.execute(sql)
    rows=res.fetchall()
    for row in rows:
        print(row)
def deletion(emp_id):
    res=con.cursor()
    sql="delete from employee where emp_id=%s"
    value=(emp_id,)
    res.execute(sql,value)
    con.commit()
    print("======DELETED SUCCESSFUL=======")
while True:
    print("1.INSERT DATA")
    print("2.UPDATE")
    print("3.DISPLAY")
    print("4.DELETE")
    print("5.QUIT")
    ch=int(input("ENTER YOUR CHOICE="))
    if ch==1:
        emp_id=int(input("ENTER ID="))
        emp_name=input("ENTER NAME=")
        emp_salary=float(input("SALARY="))
        emp_department=input("DEPARTMENT=")
        email=input("EMAIL=")
        insertion(emp_id,emp_name,emp_salary,emp_department,email)
    elif ch==2:
        emp_name=input("NAME=")
        emp_name=float(input("SALARY="))
        emp_department=input("DEPARTMENT=")
        email=input("ENTER EMAIL=")
        emp_id=int(input("ENTER ID="))
        update(emp_id,emp_name,emp_salary,emp_department,email)
    elif ch==3:
        display()
    elif ch==4:
        emp_id=input("ENTER ID TO BE DELETED=")
        deletion(emp_id)
    elif ch==5:
        break
    else:
        print("invalid selection")
print("=======================Thankyou========================================")
        


# In[ ]:





# In[ ]:




