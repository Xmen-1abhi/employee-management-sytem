import streamlit as st
import pandas as pd
import mysql.connector
st.set_page_config(page_title="Employee Management System",page_icon="https://as2.ftcdn.net/jpg/02/40/77/87/1000_F_240778787_MCHAVaEKiDZcMmMsgElqSiGmgXrQ2l7F.jpg")
st.title("EMPLOYEE MANAGEMENT SYSTEM")
choice=st.sidebar.selectbox("My Menu",("Home","Admin","View Employees"))
if(choice=="Home"):
    st.image("https://www.pngitem.com/pimgs/m/523-5233379_employee-management-system-logo-hd-png-download.png",width=400)
    st.markdown("<center><h1>WELCOME</h1><center>",unsafe_allow_html=True)
    st.write("This is an web application made by Abhishek as a part of training project.")
elif(choice=="Admin"):
    if 'login' not in st.session_state:
        st.session_state['login']=False
    aid=st.text_input("Enter Admin ID")
    an=st.text_input("Enter Admin Password")
    btn=st.button("Login")
    if btn:
        mydb=mysql.connector.connect(host="localhost",user="root",password="abhi12345678",database="employees")
        c=mydb.cursor()
        c.execute("select*from admin_")
        for r in c:
            if(r[0]==aid and r[1]==an):
                st.session_state['login']=True
                break
        if(not st.session_state['login']):
            st.write("Incorrect ID or name")
    if(st.session_state['login']):
        st.write("Login successfull")
        choice2=st.selectbox("Feature",("None","Add Employee","Remove Employee"))
        if(choice2=="Add Employee"):
            eid=st.text_input("Employement id")
            en=st.text_input("Employement name")
            em=st.text_input("Employemnt mail")
            jd=st.text_input("Joining Date")
            ep=st.text_input("Position")
            es=st.text_input("Salary")
            btn2=st.button("Add")
            if btn2:
                mydb=mysql.connector.connect(host="localhost",user="root",password="abhi12345678",database="employees")
                c=mydb.cursor()
                c.execute("insert into employee values(%s,%s,%s,%s,%s,%s)",(eid,en,em,jd,ep,es))
                mydb.commit()
                st.header("Employee added successfully")
        elif(choice2=="Remove Employee"):
            eid=st.text_input("Employement id")
            btn3=st.button("Remove Employee")
            if btn3:
                mydb=mysql.connector.connect(host="localhost",user="root",password="abhi12345678",database="employees")
                c=mydb.cursor()
                c.execute("delete from employee where Id=%s",(eid,))
                mydb.commit()
                st.header("Employee Deleted successfully")
elif(choice=="View Employees"):
     mydb=mysql.connector.connect(host="localhost",user="root",password="abhi12345678",database="employees")
     df=pd.read_sql("select*from employee",mydb)
     st.dataframe(df)
    
