#importing tkinter and pyodbc

import tkinter as tk 
from tkinter import *
# from tkinter import ttk
from tkinter import messagebox
# from tkinter.messagebox import showinfo

import pyodbc

#Connecting Database
connection = pyodbc.connect('Driver={SQL Server};' 'Server=DESKTOP-QNA2V5M\SQLEXPRESS;' 
'Database=projectTTMS;' 'Trusted_connection=yes;')
cursor = connection.cursor()

#Main Menu
root = Tk()
root.wm_title("TOUR MANAGEMENT SYSTEM")
root['background']='#75142B'
Label(root,text="Tour Management System", font=('{Times New Roman} 30 bold underline '), fg='#ffffff', bg= '#75142B').grid()

#main menu text
Label(root,text="\nWelcome to the Tour Management System!\nWe are glad to have you here and we are\nexcited to help you in planning your tour.\n", 
font=('Montserrat 20 '), fg='#ffffff', bg= '#75142B').grid(row=3,column=0, padx=10, pady=10,sticky=E)
root.geometry('620x450')

def fun1():
    root.destroy()
    root1=Tk()
    root1.title("TOUR PACKAGES")
    root1.geometry('900x630')
    root1['background']='#75142B'
    Label(root1,text="Tour Packages", font=('{Times New Roman}  30 bold underline'),fg='#ffffff', bg= '#75142B').grid(columnspan=2)
    Label(root1,text="\nThese are the available tour packages:\n", font=('Montserrat 15 italic '), fg='#ffffff', bg= '#75142B').grid(sticky=NSEW, columnspan=2)
    cur = connection.cursor()

    Label(root1,text="PACKAGE 1", font=('Montserrat 15 bold '), fg='#ffffff', bg= '#75142B').grid(sticky=NSEW)
    cur.execute("select package_name from Tour_Package where package_id = 1")
    m1 = cur.fetchall()
    cur.execute("select package_description from Tour_Package where package_id = 1")
    m2 = cur.fetchall()
    cur.execute("select convert(varchar(20),package_price) from Tour_Package where package_id = 1")
    m3 = cur.fetchall()
    cur.execute("select package_duration  from Tour_Package where package_id = 1")
    m4 = cur.fetchall()
    M = "Package Name: {s1} \nPackage Description: {s2} \nPackage Price: {s3} \nPackage Duration: {s4}".format(s1=m1,s2=m2,s3=m3,s4=m4)
    T = tk.Text(root1, height=5, width=55, wrap=WORD)
    T.grid(row=3,column=0)
    T.insert(tk.END, M)

    Label(root1,text="\nPACKAGE 2", font=('Montserrat 15 bold '), fg='#ffffff', bg= '#75142B').grid(row=4,column=0,sticky=NSEW)
    cur.execute("select package_name from Tour_Package where package_id = 2")
    n1 = cur.fetchall()
    cur.execute("select package_description from Tour_Package where package_id = 2")
    n2 = cur.fetchall()
    cur.execute("select convert(varchar(20),package_price) from Tour_Package where package_id = 2")
    n3 = cur.fetchall()
    cur.execute("select package_duration  from Tour_Package where package_id = 2")
    n4 = cur.fetchall()
    Na = "Package Name: {s1} \nPackage Description: {s2} \nPackage Price: {s3} \nPackage Duration: {s4}".format(s1=n1,s2=n2,s3=n3,s4=n4)
    T = tk.Text(root1, height=5, width=55, wrap=WORD)
    T.grid(row=5,column=0)
    T.insert(tk.END, Na)


    Label(root1,text="\nPACKAGE 3", font=('Montserrat 15 bold '), fg='#ffffff', bg= '#75142B').grid(row=6,column=0,sticky=NSEW)
    cur.execute("select package_name from Tour_Package where package_id = 3")
    l1 = cur.fetchall()
    cur.execute("select package_description from Tour_Package where package_id = 3")
    l2 = cur.fetchall()
    cur.execute("select convert(varchar(20),package_price) from Tour_Package where package_id = 3")
    l3 = cur.fetchall()
    cur.execute("select package_duration  from Tour_Package where package_id = 3")
    l4 = cur.fetchall()
    L = "Package Name: {s1} \nPackage Description: {s2} \nPackage Price: {s3} \nPackage Duration: {s4}".format(s1=l1,s2=l2,s3=l3,s4=l4)
    T = tk.Text(root1, height=5, width=55, wrap=WORD)
    T.grid(row=7,column=0)
    T.insert(tk.END, L)


    Label(root1,text="PACKAGE 4", font=('Montserrat 15 bold '), fg='#ffffff', bg= '#75142B').grid(sticky=NSEW, row=2,column=1)
    cur.execute("select package_name from Tour_Package where package_id = 4")
    o1 = cur.fetchall()
    cur.execute("select package_description from Tour_Package where package_id = 4")
    o2 = cur.fetchall()
    cur.execute("select convert(varchar(20),package_price) from Tour_Package where package_id = 4")
    o3 = cur.fetchall()
    cur.execute("select package_duration  from Tour_Package where package_id = 4")
    o4 = cur.fetchall()
    O = "Package Name: {s1} \nPackage Description: {s2} \nPackage Price: {s3} \nPackage Duration: {s4}".format(s1=o1,s2=o2,s3=o3,s4=o4)
    T = tk.Text(root1, height=5, width=55, wrap=WORD)
    T.grid(row=3,column=1)
    T.insert(tk.END, O)

    Label(root1,text="\nPACKAGE 5", font=('Montserrat 15 bold '), fg='#ffffff', bg= '#75142B').grid(row=4,column=1,sticky=NSEW)
    cur.execute("select package_name from Tour_Package where package_id = 5")
    p1 = cur.fetchall()
    cur.execute("select package_description from Tour_Package where package_id = 5")
    p2 = cur.fetchall()
    cur.execute("select convert(varchar(20),package_price) from Tour_Package where package_id = 5")
    p3 = cur.fetchall()
    cur.execute("select package_duration  from Tour_Package where package_id = 5")
    p4 = cur.fetchall()
    P = "Package Name: {s1} \nPackage Description: {s2} \nPackage Price: {s3} \nPackage Duration: {s4}".format(s1=p1,s2=p2,s3=p3,s4=p4)
    T = tk.Text(root1, height=5, width=55, wrap=WORD)
    T.grid(row=5,column=1)
    T.insert(tk.END, P)


    Label(root1,text="\nPACKAGE 6", font=('Montserrat 15 bold '), fg='#ffffff', bg= '#75142B').grid(row=6,column=1,sticky=NSEW)
    cur.execute("select package_name from Tour_Package where package_id = 6")
    q1 = cur.fetchall()
    cur.execute("select package_description from Tour_Package where package_id = 6")
    q2 = cur.fetchall()
    cur.execute("select convert(varchar(20),package_price) from Tour_Package where package_id = 6")
    q3 = cur.fetchall()
    cur.execute("select package_duration  from Tour_Package where package_id = 6")
    q4 = cur.fetchall()
    Q = "Package Name: {s1} \nPackage Description: {s2} \nPackage Price: {s3} \nPackage Duration: {s4}".format(s1=q1,s2=q2,s3=q3,s4=q4)
    T = tk.Text(root1, height=5, width=55, wrap=WORD)
    T.grid(row=7,column=1)
    T.insert(tk.END, Q)

    #Book Button
    BB=Button(root1,text="Book Tour", font=('Montserrat 10 bold'), height=0,width=10,fg='#75142B', borderwidth=3, relief="flat",
    bg='#ffffff', activebackground='#75142B',activeforeground='#ffffff', command=fun2).grid(row=8,column=0,padx=5, pady=5,sticky=N, columnspan= 2)
    root1.mainloop()

def fun2():
    root2=Tk()
    root2.title("BOOKING")
    root2.geometry('450x450')
    root2['background']='#75142B'
    Label(root2,text="Book Tour", font=('{Times New Roman}  30 bold underline'),fg='#ffffff', bg= '#75142B').grid()
    Label(root2,text="\nPlease enter the details to book your tour.\n", font=('Montserrat 15 italic '), fg='#ffffff', bg= '#75142B').grid(sticky=NSEW)
    cur = connection.cursor()

    #Name
    Label(root2,text="Name: ",font=('Montserrat 15 bold '), fg='#ffffff', bg= '#75142B').grid(row=2,column=0,sticky=W)
    def namedropdown():
        cur = connection.cursor()
        cur.execute("select customer_name from Customer")
        data = []
        for i in cur.fetchall():
            data.append(i[0])
        return data
    q1 = StringVar()
    w1=ttk.Combobox(root2, height=10,width=20,textvariable=q1, state = 'readonly')
    w1['values'] = namedropdown()
    w1.grid(row=2,column=0)

    #Hotel
    Label(root2,text="Hotel: ",font=('Montserrat 15 bold '), fg='#ffffff', bg= '#75142B').grid(row=3,column=0,sticky=W)
    def hoteldropdown():
        cur = connection.cursor()
        cur.execute("select hotel_name from Hotel")
        data = []
        for i in cur.fetchall():
            data.append(i[0])
        return data
    q2 = StringVar()
    w2=ttk.Combobox(root2, height=10,width=20,textvariable=q2, state = 'readonly')
    w2['values'] = hoteldropdown()
    w2.grid(row=3,column=0)

    #Booking date
    Label(root2,text="Booking Date: ",font=('Montserrat 13 bold '), fg='#ffffff', bg= '#75142B').grid(row=4,column=0,sticky=W)
    bd = Entry(root2, width=23)
    bd.grid(row=4, column=0)
    Label(root2,text="(YYYY-MM-DD)", font=('{Times New Roman} 10'), fg='#ffffff', bg= '#75142B').grid(row=4,column=0,sticky=E)

    #Package
    Label(root2,text="Package: ",font=('Montserrat 15 bold '), fg='#ffffff', bg= '#75142B').grid(row=5,column=0,sticky=W)
    def packagedropdown():
        cur = connection.cursor()
        cur.execute("select package_name from Tour_Package")
        data = []
        for i in cur.fetchall():
            data.append(i[0])
        return data
    q3 = StringVar()
    w3=ttk.Combobox(root2, height=10,width=20,textvariable=q3, state = 'readonly')
    w3['values'] = packagedropdown()
    w3.grid(row=5,column=0)

    #Place
    Label(root2,text="Place: ",font=('Montserrat 15 bold '), fg='#ffffff', bg= '#75142B').grid(row=6,column=0,sticky=W)
    def placedropdown():
        cur = connection.cursor()
        cur.execute("select place_name from Tourism_Place")
        data = []
        for i in cur.fetchall():
            data.append(i[0])
        return data
    q4 = StringVar()
    w4=ttk.Combobox(root2, height=10,width=20,textvariable=q4, state = 'readonly')
    w4['values'] = placedropdown()
    w4.grid(row=6,column=0)

    #Transport
    Label(root2,text="Transport: ",font=('Montserrat 15 bold '), fg='#ffffff', bg= '#75142B').grid(row=7,column=0,sticky=W)
    def transportdropdown():
        cur = connection.cursor()
        cur.execute("select transport_description from Transport")
        data = []
        for i in cur.fetchall():
            data.append(i[0])
        return data
    q5 = StringVar()
    w5=ttk.Combobox(root2, height=10,width=20,textvariable=q5, state = 'readonly')
    w5['values'] = transportdropdown()
    w5.grid(row=7,column=0)

    def  book_function():
        a=w1.get()
        b=w2.get()
        c=bd.get()
        d=w3.get()
        e=w4.get()
        f=w5.get()
        cur=connection.cursor()
        if a=='' or b=='' or c=='' or d=='' or e=='' or f=='':
            messagebox.showerror("Error","Cant leave any field empty")
        else:
            def PackageFunc(connection):
                cursor = connection.cursor()
                cursor.execute(f"SELECT package_id FROM Tour_Package where package_name = '{d}'")
                for row in cursor:
                    row = row[0]
                    return row
                connection.commit()
            
            def CustomerFunc(connection):
                cursor = connection.cursor()
                cursor.execute(f"SELECT customer_id FROM Customer where customer_name = '{a}'")
                for row in cursor:
                    row = row[0]
                    return row
                connection.commit()

            def TransportFunc(connection):
                cursor = connection.cursor()
                cursor.execute(f"SELECT transport_id FROM Transport where transport_description like '{f}'")
                for row in cursor:
                    row = row[0]
                    return row
                connection.commit()

            def HotelFunc(connection):
                cursor = connection.cursor()
                cursor.execute(f"SELECT hotel_id FROM Hotel where hotel_name = '{b}'")
                for row in cursor:
                    row = row[0]
                    return row
                connection.commit()

            def PlaceFunc(connection):
                cursor = connection.cursor()
                cursor.execute(f"SELECT place_id FROM Tourism_Place where place_name = '{e}'")
                for row in cursor:
                    row = row[0]
                    return row
                connection.commit()

            def PriceFunc(connection):
                cursor = connection.cursor()
                cursor.execute(f"SELECT package_price FROM Tour_Package where package_name = '{d}'")
                for row in cursor:
                    row = row[0]
                    return row
                connection.commit()

            package = PackageFunc(connection)
            customer = CustomerFunc(connection)
            transport = TransportFunc(connection)
            hotel = HotelFunc(connection)
            place = PlaceFunc(connection)
            price = PriceFunc(connection)

            cur.execute("insert into Tour_Booking (package_id,customer_id,transport_id,hotel_id,place_id,booking_date,booking_total_price,booking_status) values(?,?,?,?,?,?,?,?)",(package,customer,transport,hotel,place,c,price,"Confirmed"))
            connection.commit()

            messagebox.showinfo("BOOKING SUCCESSFUL","Your Tour has been booked! THANK YOU FOR CHOOSING US")

    

    #Book Button
    BB=Button(root2,text="Book Tour", font=('Montserrat 10 bold'), height=0,width=10,fg='#75142B', borderwidth=3, relief="flat",
    bg='#ffffff', activebackground='#75142B',activeforeground='#ffffff', command=book_function).grid(row=8,column=0,padx=5, pady=5,sticky=N)
    root2.mainloop()



#Button Of Search Flight in Main Menu
B1=Button(root,text="Tour Packages", font=('Montserrat 15 bold'),height=0,width=15,fg='#75142B', borderwidth=3, relief="flat",
bg='#ffffff', activebackground='#75142B',activeforeground='#ffffff', command=fun1).grid(row=4,column=0, padx=10, pady=10,sticky=N)

#Button Of Book Flight in Main Menu
B2=Button(root,text="Book Tour", font=('Montserrat 15 bold'),height=0,width=15,fg='#75142B', borderwidth=3, relief="flat",
bg='#ffffff', activebackground='#75142B',activeforeground='#ffffff', command=fun2).grid(row=5,column=0, padx=10, pady=10,sticky=N)


root.mainloop()