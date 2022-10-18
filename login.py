from tkinter import *
from tkinter import messagebox
import databaseConnection as conn
import mainView as mainwindow

mycursor=conn.mydb.cursor()

def login():
    username = entry1.get()
    password = entry2.get()

    # "SELECT *FROM users WHERE first_name ='%s' AND password ='%s'" % (username, password)
    mycursor.execute("SELECT * FROM login_table WHERE username='%s' and password='%s'" % (username, password))
    result = mycursor.fetchone()

    if(username=="" or password==""):
        messagebox.showinfo("Error","Blank Not Allowed")
    else:
        if result != None:

                #(username==result[0][1] or password==result[0][2]):
            messagebox.showinfo("Success", "Login Success")
            cancel()
            mainwindow.mainWindow()




        else:
            messagebox.showinfo("Error", "Incorrect username and password!!")
def cancel():
    root3.destroy()


root3=Tk()
tusername=StringVar()
tpassword=StringVar()



global entry1
global entry2

Label(root3,text="Username").place(x=20,y=20)
Label(root3,text="Password").place(x=20,y=70)


entry1=Entry(root3,bd=3,width=28,textvariable=tusername)
entry1.place(x=140,y=20)

entry2=Entry(root3,bd=3,show="*",width=28,textvariable=tpassword)
entry2.place(x=140,y=70)

Button(root3,text="Login",command=login,height=1,width=10,bd=2).place(x=235,y=120)
Button(root3,text="Cancel",command=cancel,height=1,width=10,bd=2).place(x=150,y=120)

#root.bind('<Return>', login)

root3.title("Login")
root3.geometry("350x170")
root3.mainloop()