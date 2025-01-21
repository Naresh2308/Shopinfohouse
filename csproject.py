# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 10:09:30 2021

@author: tnare
"""
import random
import csv
import datetime
import pickle
#from tkinter import*
from tkinter import messagebox
from matplotlib import pyplot as plt


def user_password():
    file=open('password.dat','ab+')
    user_id=input('Enter email id :')
    name=input('Enter name :')
    a=0
    while a==0:
        password=input('Enter a password :')
        if len(password)<=8 and password.isalnum==False:
            print('Weak Password! Try another combination')
            password=input('Enter password :')
        else:
            a=1
        
    l=[user_id,name,password]
    pickle.dump(l,file)
    
    
def check_password():
    file=open('password.dat','rb')
    list1=[]
    user_id=input('Enter username to verify :')
    password=input('Enter password  :')

    try:
        while True:          
            list1.append(pickle.load(file))
    except EOFError:
        pass
    for i in list1:
        if i[0]==user_id and i[2]==password:
            print('Hi',i[1])
            message_box()
            cust_accreminder()
            
            cont='N'
            while cont=='N':  
                main_menu()
                cont=input('Do You Want to Quit(N/Y)').upper()
            print('THANK YOU!!')
            
        
        else:
           print('ERROR! wrong password or user id')
           print('ACCESS DENIED!!!')
            
            
def employee_info(numberofemployees):
    f=open('employee_list.csv','a+')
    for i in range(1,(numberofemployees+1)):
        print('Enter employee',i , 'details')
        employee_name=input('Enter employees name  :').upper()
        employee_id=input('Enter employee id :')
        employee_designation=input('Enter employee designation :').upper()
        employee_address=input('Enter employee address :')
        employee_email=input('Enter employee email :')
        employee_mob=int(input('Enter employee mobile number :'))
        employee_salary=float(input('Enter employees basic salary per month :'))
        #join_date=input('enter date of joining (DD/MM/YYYY)')
        today = datetime.date.today()
        today=today.strftime('%d/%m/%Y')
        csv_w=csv.writer(f) 
        list1=[employee_id,employee_name,employee_designation,employee_salary,today,employee_address,employee_email,employee_mob]
        csv_w.writerow(list1)
        print('Information Added')
        
        

def employee_salary():
    d={'01':'31','02':'28','03':'31','04':'30','05':'31','06':'30','07':'31','08':'31','09':'30','10':'31','11':'30','12':'31'}
    f=open('employee_list.csv','r')
    file1=open('employee_salary.csv','a+')
    date=input('Enter date :')
    for i in d.keys():
        if date[3:5]==i:
            m=d[i]
            m=int(m)
    id_emp=input('Enter employee id :')
    present_days=int(input('Enter present day of employee :'))
    #absent_days=int(input('Enter absent days of employee :'))
    paid_holiday=int(input('Enter paid holidays sanctioned :'))
    absent_days=m-(present_days+paid_holiday)
    over_time=int(input('Enter number of hours of overtime :'))
    bonus_g=input('Enter if bonus have to be given (N/Y) :').upper()
    if bonus_g=='Y':
        bonus=int(input('Enter bonus amount :'))
    else:
        bonus=0
    csv_r=csv.reader(f)
    c=0
    while c==0:
        for i in csv_r:
            if i[0]==id_emp:
                salary=i[3]
                salary=float(salary)
                employee=i[1]
                c=1
                break
    da=(28/100)*salary
    day_salary=salary//30
    hour_salary=day_salary//8
    salary=(present_days*day_salary)+(over_time*hour_salary)+da
    print('Salary of the Employee is',salary)
    total_amount=salary+bonus
    l=[date,id_emp,employee,present_days,absent_days,paid_holiday,salary,bonus,da,total_amount]
    
    csv_w=csv.writer(file1 ,delimiter=',')
    csv_w.writerow(l)
    
    
def add_products():
    date=input('Enter date :')
    product_id=input('Enter product id :')
    product_name=input('Enter product name :')
    product_brand=input('Enter product brand :')
    product_cost=int(input('Enter cost price of one product :'))
    product_quant=int(input('Enter total number of products purchased'))
    target=int(input('Enter a target number to be sold'))
    total_cost=product_cost*product_quant
    f=open('product_list.csv','a+')
    csv_w=csv.writer(f,delimiter=',')
    l=[date,product_id,product_brand,product_name,product_cost,product_quant,total_cost,target]
    csv_w.writerow(l)


    
def sold_product():
    date=input('Enter Date :')
    product_id=input('Enter Product ID :')
    product_name=input('Enter Product Name :')
    product_brand=input('Enter Product Brand :')
    product_cost=int(input('Enter Selling price of One Product :'))
    product_quant=int(input('Enter Total number of Products Sold'))
    amt_gained=(product_cost*product_quant)
    #print(amt_gained)
    f=open('sold_list.csv','a+')
    f1=open('product_list.csv','r')
    csv_r=csv.reader(f1)
    for i in csv_r:
        #print(i)
        if i!=[] and product_id==i[1]:
            #print(i[5])
            stock=int(i[5])-product_quant
            if stock<=10:
                l1=['Buy More stock of this Product',product_name]
                messagebox.showinfo('Stock Almost finished',l1)
            boughtprice=int(i[4])*product_quant
            #print(boughtprice)
            target=int(i[7])
            #print(i[6:8])
            break
    profit=amt_gained-boughtprice
    csv_w=csv.writer(f)
    l=[date,product_id,product_name,product_brand,product_cost,product_quant,amt_gained,profit,stock]
    csv_w.writerow(l)
    if profit>0:
        print('Your Profit for this Product is',profit)
    else:
        print('Your Loss for this Product is',profit)
    
    
    if target>product_quant:
        print('You couldnt complete the Target of Selling this product')
    else :
        print('You have completed the Target of selling this product')
    

    
      


    
    
    
def cust_acc():
    f=open('customeraccount.csv','a+')
    c_name=input('enter customer name').upper()
    amount=int(input('enter amount to be paid'))
    reply=input('if to be paid by end of month(N/Y)').upper()
    if reply=='Y':
        today=datetime.date.today()
        date=today.strftime('30/%m/%Y')
        #print(today)
    else:
        date=input('Enter date (DD/MM/YYYY)')
    csv_w=csv.writer(f)
    l=[c_name,amount,date]
    csv_w.writerow(l)





def cust_accreminder():
    f=open('customeraccount.csv','r')
    csv_r=csv.reader(f)
    today=datetime.date.today()
    today=today.strftime('%d/%m/%Y')
    for i in csv_r:
        if i!=[] and i[2]==today:
            l=('Customer name',i[0],'Amount',i[1])
            messagebox.showinfo('Reminder',l)
            
        
    


def message_box():
    today=datetime.date.today()
    today=today.strftime('%d/%m/%Y')
    #print(today)
    #print(today[0:2])
    d={'01':'31','02':'28','03':'31','04':'30','05':'31','06':'30','07':'31','08':'31','09':'30','10':'31','11':'30','12':'31'}
    for i in d.keys():
        if today[3:5]==i and today[0:2]==d[i]:
           # print('y')
            messagebox.showinfo('Reminder','Salary Payment')
        else:
           # print('n')
           continue



def show_prod_stock():
    f=open('sold_list.csv','r')
    csv_r=csv.reader(f)
    for i in csv_r:
        if i!=[]:
            print(i[1],i[2],i[8])



def profit_graph():
    f=open('sold_list.csv','r')
    csv_r=csv.reader(f)
    l=[]
    d=[]
    for i in csv_r:
        if i!=[]:
            l.append(i[7])
            d.append(i[0])
        
    plt.plot(l,d ,label='line one')
    plt.grid()
    plt.title('Profit')
    plt.xlabel('Profit')
    plt.ylabel('Date')
    plt.legend()
    plt.show()


def total_profit():
    f=open('sold_list.csv','r')
    tp=0
    csvr=csv.reader(f)
    #print(csvr)
    month=input('Enter Month Number to show Profit :')
    if len(month)==1:
        month='0'+month
              
    for i in csvr:
        if i!=[] and (i[0][3:5])==month:
            tp+=int(i[7])       
          
    print('Total profit of this Month is ',tp)
            
def show_sold():
    f=open('sold_list.csv','r+')
    csv_r=csv.reader(f)
    for i in csv_r:
        if i!=[]:
            print(i)
    

def show_emp():
    f=open('employee_list.csv','r')
    csv_r=csv.reader(f)
    for i in csv_r:
        if i!=[]:
            print(i)


def show_pemp():
    f=open('employee_list.csv','r')
    csv_r=csv.reader(f)
    name=input('enter employee name').upper()
    for i in csv_r:
        if i!=[] and i[1]==name:
            print(i)
            
            

def main_menu():
    print('*'*70)
    print(' '*25,'MAIN MENU')
    print(' '*10,'1. Enter a Employees Record')
    print(' '*10,'2. Calculate Salary of a Employee')
    print(' '*10,'3. Add products to your Store')
    print(' '*10,'4. Add sold products')
    print(' '*10,'5. Show Stocks of Product')
    print(' '*10,'6. Show Sold Product List')
    print(' '*10,'7. Show Profit Graph')
    print(' '*10,'8. Show Employee Record')
    print(' '*10,'9. Show Employee by name')
    print(' '*10,'10. Show Profit of Particular Month')
    print(' '*10,'11. Add Customers Account')
    
    
    print('*'*70)
    
    opt=int(input('Enter your Option from main menu'))
    check=0
    while check==0:
        if opt>11:
           # print('enter valid option')
            opt=int(input('Enter Valid Option'))
        else:
            check=1
    
    print('You Selected option',opt)
     
    if opt==1:
        a=int(input('Enter number of Employee'))
        employee_info(a)
    elif opt==2:
        employee_salary()
    elif opt==3:
        add_products()
    elif opt==4:
        sold_product()
    elif opt==5:
        show_prod_stock()
    elif opt==6:
        show_sold()
    elif opt==7:
        profit_graph()
    elif opt==8:
        show_emp()
    elif opt==9:
        show_pemp()
    elif opt==10:
        #print('choose other option')
        total_profit()
    elif opt==11:
        cust_acc()






'''
cont='N'
while cont=='N':  
    main_menu()
    cont=input('Do You Want to Quit(N/Y)').upper()
'''


print('1.Sign in')
print('2. Log In')
option=int(input('Enter Your option(1,2)'))
if option==1:
    user_password()
elif option==2:
    check_password()
else:
    print('Wrong Option Entered')

