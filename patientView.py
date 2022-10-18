from tkinter import *
from tkinter import messagebox, ttk
from tkinter.simpledialog import askstring
from tkinter.ttk import Treeview
import tkinter as tk
import databaseConnection as conn
import mainView


mycursor=conn.mydb.cursor()

def update3(rows,trv):
    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert('','end',values=i)

def search3(q,trv):
    q2=q.get()
    print(q2)
    query="SELECT * FROM patient_table WHERE patient_reg LIKE '%"+q2+"%' OR patient_reg LIKE '%"+q2+"%'"
    mycursor.execute(query)
    rows=mycursor.fetchall()
    update3(rows,trv)

def clear3(trv):
    query="SELECT * FROM patient_table"
    mycursor.execute(query)
    rows=mycursor.fetchall()
    update3(rows,trv)

def getrow2(event,trv,t1,t2,t3,t4,t5,t6,pNo,pName,pSex,pAge,pAdd,pTel):

   # rowid = trv.identify_row(event.y)
    item = trv.item(trv.focus())

    t1.set(item['values'][0])
    t2.set(item['values'][1])
    t3.set(item['values'][2])
    t4.set(item['values'][3])
    t5.set(item['values'][4])
    t6.set(item['values'][5])


    pNo.set(item['values'][0])
    pName.set(item['values'][1])
    pAge.set(item['values'][2])
    pSex.set(item['values'][3])
    pAdd.set(item['values'][4])
    pTel.set(item['values'][5])



def update_patient(trv,pNo,pName,pSex,pAge,pAdd,pTel):

    if messagebox.askyesno("Confirm Update?", "Are you Sure you want to Update?"):
        query="UPDATE patient_table SET patient_reg=%s,patient_name=%s,patient_sex=%s,patient_age=%s,patient_address=%s,patient_tel=%s WHERE patient_reg=%s "
        mycursor.execute(query,[pNo,pName,pSex,pAge,pAdd,pTel,pNo])
        conn.mydb.commit()
        clear3(trv)


def add_patient(trv,pNo,pName,pSex,pAge,pAdd,pTel):
    if messagebox.askyesno("Confirm Insert?", "Are you Sure you want to Insert Data?"):
        query="INSERT INTO patient_table(patient_reg,patient_name,patient_sex,patient_age,patient_address,patient_tel) VALUES(%s,%s,%s,%s,%s,%s) "
        mycursor.execute(query,[pNo,pName,pSex,pAge,pAdd,pTel])
        conn.mydb.commit()
        clear3(trv)

def delete_patient(trv4,pNo):
    if messagebox.askyesno("Confirm Delete?", "Are you Sure you want to Delete Data?"):
        query = "DELETE FROM patient_table WHERE patient_reg=%s "
        mycursor.execute(query, [pNo])
        conn.mydb.commit()
        clear3(trv4)

def patientDetails(t1,t2,t3,t4,t5,t6):
    root2 = Toplevel()
    q = StringVar()

    pNo = StringVar()
    pName = StringVar()
    pAge = StringVar()
    pSex = StringVar()
    pAdd = StringVar()
    pTel = StringVar()

    root2.title("Patient Details")
    root2.resizable(width=False, height=False)
    root2.geometry("900x600")
    style2 = ttk.Style()
    style2.theme_use('clam')

    wrapper1 = LabelFrame(root2, text="Patient Details")
    wrapper1.pack(fill="both", expand="no", padx=10, pady=10, ipady=5, ipadx=5)
    trv4 = Treeview(wrapper1, columns=(1, 2, 3, 4, 5, 6), show="headings", height="6")

    trv4.column("# 1", anchor=CENTER, stretch=NO, width=110)
    trv4.column("# 2", anchor=CENTER, stretch=NO, width=180)
    trv4.column("# 3", anchor=CENTER, stretch=NO, width=110)
    trv4.column("# 4", anchor=CENTER, stretch=NO, width=110)
    trv4.column("# 5", anchor=CENTER, stretch=NO, width=180)
    trv4.column("# 6", anchor=CENTER, stretch=NO, width=180)

    treeScroll4 = ttk.Scrollbar(wrapper1)
    treeScroll4.configure(command=trv4.yview)
    trv4.configure(yscrollcommand=treeScroll4.set)
    treeScroll4.pack(side=RIGHT, fill=BOTH)

    trv4.pack()

    trv4.heading(1, text=" Doc Reg No")
    trv4.heading(2, text="Name")
    trv4.heading(3, text="Sex")
    trv4.heading(4, text="Age")
    trv4.heading(5, text="Address")
    trv4.heading(6, text="Telephone No")

    trv4.bind('<Double 1>', lambda event:getrow2(event, trv4, t1, t2,t3,t4, t5,t6,pNo,pName,pSex,pAge,pAdd,pTel))

    query = "SELECT * FROM patient_table "
    mycursor.execute(query)
    rows = mycursor.fetchall()

    update3(rows, trv4)

    wrapper2 = LabelFrame(root2, text="Search Patient")
    wrapper2.pack(fill="both", expand="no", padx=10, pady=10)

    lbl12 = Label(wrapper2, text="Search in List")
    lbl12.grid(row=0, column=0, padx=5, pady=3, sticky='w')
    ent12 = Entry(wrapper2, textvariable=q)
    ent12.grid(row=0, column=1, padx=5, pady=3)

    btn12 = Button(wrapper2, text="Searach", command=lambda: search3(q, trv4))
    btn12.grid(row=0, column=2, padx=5, pady=3)

    cbtn12 = Button(wrapper2, text="Clear" , command=lambda: clear3(trv4))
    cbtn12.grid(row=0, column=3, padx=5, pady=3)

    wrapper4 = LabelFrame(root2, text="Patient Details")
    wrapper4.pack(fill="both", expand="no", padx=10, pady=10, ipady=5, ipadx=5)

    lbl1 = Label(wrapper4, text="Patient Reg No")
    lbl1.grid(row=3, column=0, padx=5, pady=3, sticky='w')
    ent1 = Entry(wrapper4, textvariable=pNo)
    ent1.grid(row=3, column=1, padx=5, pady=3)

    lbl2 = Label(wrapper4, text="Name", justify=LEFT)
    lbl2.grid(row=4, column=0, padx=5, pady=3, sticky='w')
    ent2 = Entry(wrapper4, textvariable=pName)
    ent2.grid(row=4, column=1, padx=5, pady=3)

    lbl3 = Label(wrapper4, text="Sex")
    lbl3.grid(row=5, column=0, padx=5, pady=3, sticky='w')
    ent3 = Entry(wrapper4, textvariable=pSex)
    ent3.grid(row=5, column=1, padx=5, pady=3)

    lbl4 = Label(wrapper4, text="Age")
    lbl4.grid(row=6, column=0, padx=5, pady=3, sticky='w')
    ent4 = Entry(wrapper4, textvariable=pAge)
    ent4.grid(row=6, column=1, padx=5, pady=3)

    lbl5 = Label(wrapper4, text="Address")
    lbl5.grid(row=7, column=0, padx=5, pady=3, sticky='w')
    ent5 = Entry(wrapper4, textvariable=pAdd)
    ent5.grid(row=7, column=1, padx=5, pady=3)

    lbl6 = Label(wrapper4, text="Telephone No")
    lbl6.grid(row=8, column=0, padx=5, pady=3, sticky='w')
    ent6 = Entry(wrapper4, textvariable=pTel)
    ent6.grid(row=8, column=1, padx=5, pady=3)

    patient_update_btn = Button(wrapper4, text="Update",command=lambda:update_patient(trv4,pNo.get(),pName.get(),pSex.get(),pAge.get(),pAdd.get(),pTel.get()))
    patient_add_btn = Button(wrapper4, text="Add New",command=lambda :add_patient(trv4,pNo.get(),pName.get(),pSex.get(),pAge.get(),pAdd.get(),pTel.get()))
    patient_delete_btn = Button(wrapper4, text="Delete",command=lambda:delete_patient(trv4,pNo.get()))

    patient_add_btn.grid(row=9, column=0,sticky='w' )
    patient_delete_btn.grid(row=9, column=1,sticky='w')
    patient_update_btn.grid(row=9, column=2,sticky='w')


    root2.mainloop()

