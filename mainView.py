from tkinter import *
from tkinter import messagebox, ttk
from tkinter.simpledialog import askstring
from tkinter.ttk import Treeview
import tkinter as tk
import databaseConnection as conn


import patientView as pDetails


mycursor=conn.mydb.cursor()

def update(rows,trv):
    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert('','end',values=i)

def search(q,trv):
    q2=q.get()
    print(q2)
    query="SELECT doctor_reg,doctor_name,doctor_sex,doctor_age,doctor_add,doctor_tel FROM doctor_table WHERE doctor_name LIKE '%"+q2+"%' OR doctor_reg LIKE '%"+q2+"%'"
    mycursor.execute(query)
    rows=mycursor.fetchall()
    update(rows,trv)

def search2(q2,trv2):
    q22=q2.get()
    print(q2)
    query="SELECT doctor_reg,slot1,slot2,slot3,slot4,slot5,slot6,slot7,slot8,slot9,slot10,slot11,slot12,slot13,slot14,slot15,slot16 FROM schedule_table WHERE doctor_reg LIKE '%"+q22+"%' "
    mycursor.execute(query)
    rows=mycursor.fetchall()
    update(rows,trv2)

def clear(trv):
    query="SELECT doctor_reg,doctor_name,doctor_sex,doctor_age,doctor_add,doctor_tel FROM doctor_table"
    mycursor.execute(query)
    rows=mycursor.fetchall()
    update(rows,trv)

def clear2(trv2):
    query="SELECT doctor_reg,slot1,slot2,slot3,slot4,slot5,slot6,slot7,slot8,slot9,slot10,slot11,slot12,slot13,slot14,slot15,slot16 FROM schedule_table"
    mycursor.execute(query)
    rows=mycursor.fetchall()
    update(rows,trv2)


def add_appoinment(trv2,t1, t2, t3, t4, t5, t6,opDoc,opslot):
    reg = t1.get()
    name =t2.get()
    sex = t3.get()
    age = t4.get()
    add = t5.get()
    tel = t6.get()
    docReg=opDoc.get()
    slot=str(opslot.lower())
    if opDoc.get()=="" or opslot=="" or reg=="" or name=="" or sex=="" or age=="" or add=="" or tel=="":
        messagebox.showinfo("Error","Please fill the all Details")
    else:
        query1="SELECT * FROM patient_table WHERE patient_reg=%s "
        mycursor.execute(query1, [reg])
        rows1 = mycursor.fetchone()

        if rows1==None:
               # queryCheck=f"SELECT doctor_reg,slot1,slot2,slot3,slot4,slot5,slot6,slot7,slot8,slot9,slot10,slot11,slot12,slot13,slot14,slot15,slot16 FROM schedule_table WHERE doctor_reg=%s and "+slot+"='None'"
                queryCheck = f"SELECT doctor_reg,slot1,slot2,slot3,slot4,slot5,slot6,slot7,slot8,slot9,slot10,slot11,slot12,slot13,slot14,slot15,slot16 FROM schedule_table WHERE doctor_reg=%s AND " + slot + " IS NULL "
                mycursor.execute(queryCheck,[docReg])
                rows = mycursor.fetchone()
                # D1 = rows[0]
                # s1 = rows[1]
                # s2 = rows[2]
                # s3 = rows[3]
                # s4 = rows[4]
                # s5 = rows[5]
                # s6 = rows[6]
                # s7 = rows[7]
                # s8 = rows[8]
                # s9 = rows[9]
                # s10 = rows[10]
                # s11 = rows[11]
                # s12 = rows[12]
                # s13 = rows[13]
                # s14 = rows[14]
                # s15 = rows[15]
                # s16 = rows[16]
                if rows != None:
                    #print(rows)
                    if messagebox.askyesno("Confirm Booking?", "Are you Sure you want to Book this Time Slot?"):
                        #queryUpdate="UPDATE schedule_table SET doctor_reg=%s,slot1=%s,slot2=%s,slot3=%s,slot4=%s,slot5=%s,slot6=%s,slot7=%s,slot8=%s,slot9=%s,slot10=%s,slot11=%s,slot12=%s,slot13=%s,slot14=%s,slot15=%s,slot16=%s"
                        queryUpdate="UPDATE schedule_table SET "+slot+"=%s WHERE doctor_reg=%s"

                        querySavePatient="INSERT INTO patient_table(patient_reg,patient_name,patient_sex,patient_age,patient_address,patient_tel) VALUES(%s,%s,%s,%s,%s,%s)"
                        mycursor.execute(queryUpdate, [reg,docReg])
                        clear2(trv2)
                        mycursor.execute(querySavePatient, [reg, name, sex, age, add, tel])
                        conn.mydb.commit()
                else:
                    messagebox.showinfo("Error","Slot is Already Booked!! Select another time slot!!! ")
        else:
            messagebox.showinfo("Alert","Patient detailes Already have in database")
            queryUpdate = "UPDATE schedule_table SET " + slot + "=%s WHERE doctor_reg=%s"
            mycursor.execute(queryUpdate, [reg, docReg])
            conn.mydb.commit()
            clear2(trv2)







    # print(opDoc,opslot)
    # if messagebox.askyesno("Confirm Delete?", "Are you Sure you want to delete the custemor?"):
    #     query="INSERT INTO patient_table(patient_reg,patient_name,patient_sex,patient_age,patient_address,patient_tel) VALUES(%s,%s,%s,%s,%s,%s)"
    #     mycursor.execute(query,(reg,name,sex,age,add,tel))
    #     conn.mydb.commit()
    #   #  clear(trv)
    # else:
    #     return True

def patient_details(t1,t2,t3,t4,t5,t6):
   pDetails.patientDetails(t1,t2,t3,t4,t5,t6)

def clear_all_booking(trv):
     #doc_reg=t1.get()
    # print(doc_reg)
    docR = askstring('Clear Booking', 'Enter Doctor Reg No?')

    if messagebox.askyesno("Confirm to Clear?","Are you Sure you want to Clear All Scheduling ?"):
        # try:
            queryUpdate="UPDATE schedule_table SET slot1=NULL ,slot2=NULL,slot3=NULL,slot4=NULL,slot5=NULL,slot6=NULL,slot7=NULL,slot8=NULL,slot9=NULL,slot10=NULL,slot11=NULL,slot12=NULL,slot13=NULL,slot14=NULL,slot15=NULL,slot16=NULL WHERE doctor_reg=%s "
            mycursor.execute(queryUpdate,[docR])
            conn.mydb.commit()
            clear2(trv)
        # except:
        #     messagebox.showinfo("Error","Enter the Correct Reg No of Doctor")
    else:
        return True

def getrow(event,trv,tDoc):
    # print("Call to this")

   # rowid = trv.identify_row(event.y)
    item = trv.item(trv.focus())
   #  print(item['values'][0])
   #  print(item)

    tDoc.set(item['values'][0])
    # print(item)
    # t1.set(item['values'][0])
    # t2.set(item['values'][1])
    # t3.set(item['values'][2])
    # t4.set(item['values'][3])
    # t5.set(item['values'][4])
    # t6.set(item['values'][5])





def mainWindow():
    root = Tk()
    # datatype of menu text
    clicked = StringVar()
    clicked2 = StringVar()
    # Dropdown menu options
    options = []
    options2 = ["slot1","slot2","slot3","slot4","slot5","slot6","slot7","slot8","slot9","slot10","slot11","slot12","slot13","slot14","slot15","slot16"]


    q = StringVar()
    q2 = StringVar()
    t1 = StringVar()
    t2 = StringVar()
    t3 = StringVar()
    t4 = StringVar()
    t5 = StringVar()
    t6 = StringVar()
    tDoc = StringVar()
    root.title("Main  Window")
    root.resizable(width=False, height=False)
    root.geometry("1400x780")
    style = ttk.Style()
    style.theme_use('clam')

# ================================== Sectin of Available Doctor =======================================
    wrapper1 = LabelFrame(root, text="Available Doctors List")
    wrapper1.pack(fill="both", expand="no", padx=10, pady=10,ipady=5,ipadx=5)

    wrapper3 = LabelFrame(root, text="Appoinments Details",height=100)
    wrapper3.pack(fill="both", expand="no", padx=10, pady=10, ipady=5, ipadx=5)

    trv = Treeview(wrapper1, columns=(1, 2, 3, 4,5,6), show="headings", height="6")
    trv2 = Treeview(wrapper3, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17), show="headings",
                    height="6")

    trv.column("# 1", anchor=CENTER, stretch=NO, width=130)
    trv.column("# 2", anchor=CENTER, stretch=NO, width=200)
    trv.column("# 3", anchor=CENTER, stretch=NO, width=130)
    trv.column("# 4", anchor=CENTER, stretch=NO, width=130)
    trv.column("# 5", anchor=CENTER, stretch=NO, width=200)
    trv.column("# 6", anchor=CENTER, stretch=NO, width=200)

    treeScroll = ttk.Scrollbar(wrapper1)
    treeScroll.configure(command=trv.yview)
    trv.configure(yscrollcommand=treeScroll.set)
    treeScroll.pack(side=RIGHT, fill=BOTH)


    trv.pack()

    trv.heading(1, text=" Doc Reg No")
    trv.heading(2, text="Name")
    trv.heading(3, text="Sex")
    trv.heading(4, text="Age")
    trv.heading(5, text="Address")
    trv.heading(6, text="Telephone No")

    trv.bind('<Double 1>',lambda event: getrow(event,trv,tDoc))

    query = "SELECT doctor_reg,doctor_name,doctor_sex,doctor_age,doctor_add,doctor_tel FROM doctor_table "
    mycursor.execute(query)
    rows = mycursor.fetchall()
    update(rows,trv)

    queryslot = "SELECT doctor_reg,slot1,slot2,slot3,slot4,slot5,slot6,slot7,slot8,slot9,slot10,slot11,slot12,slot13,slot14,slot15,slot16 FROM schedule_table "
    mycursor.execute(queryslot)
    rowsSlot = mycursor.fetchall()
    update(rowsSlot, trv2)

#===fill drop down availability doctor ==========

    query_doc_reg="SELECT doctor_reg FROM schedule_table"
    mycursor.execute(query_doc_reg)
    rows_doc_name=mycursor.fetchall()

    for n in rows_doc_name:
        options.append(n)


    #query_empty_slot="SELECT doctor_reg,slot1,slot2,slot3,slot4,slot5,slot6,slot7,slot8,slot9,slot10,slot11,slot12,slot13,slot14,slot15,slot16 FROM schedule_table WHERE doctor_reg=%s"

#===================================================================================================================

#====================== Manage Doctors ============================
    wrapper2 = LabelFrame(root, text="Search Doctor")
    wrapper2.pack(fill="both", expand="no", padx=10, pady=10)

# ========== Search Function ============= availability List ==========

    lbl = Label(wrapper2, text="Search Availability List")
    lbl.grid(row=0, column=0, padx=5, pady=3,sticky = 'w')
    ent = Entry(wrapper2, textvariable=q)
    ent.grid(row=0, column=1, padx=5, pady=3)

    btn = Button(wrapper2, text="Searach", command=lambda: search(q,trv))
    btn.grid(row=0, column=2, padx=5, pady=3)

    cbtn = Button(wrapper2, text="Clear", command=lambda:clear(trv))
    cbtn.grid(row=0, column=3, padx=5, pady=3)
 # ==============================================================================

    lbl8 = Label(wrapper2, text="      ")
    lbl8.grid(row=0, column=4, padx=5, pady=3, sticky='e')
    lbl9 = Label(wrapper2, text="      ")
    lbl9.grid(row=0, column=5, padx=5, pady=3, sticky='e')
    lbl10 = Label(wrapper2, text="      ")
    lbl10.grid(row=0, column=6, padx=5, pady=3, sticky='e')
    lbl11 = Label(wrapper2, text="      ")
    lbl11.grid(row=0, column=7, padx=5, pady=3, sticky='e')
    lbl12 = Label(wrapper2, text="      ")
    lbl12.grid(row=0, column=8, padx=5, pady=3, sticky='e')
    lbl13 = Label(wrapper2, text="      ")
    lbl13.grid(row=0, column=9, padx=5, pady=3, sticky='e')


 # ========== Search Function ============= availability List ==========

    lbl7 = Label(wrapper2, text="Search Appoinmnt list")
    lbl7.grid(row=0, column=10, padx=5, pady=3, sticky='e')
    ent7 = Entry(wrapper2, textvariable=q2)
    ent7.grid(row=0, column=11, padx=5, pady=3)

    btn2 = Button(wrapper2, text="Searach", command=lambda: search2(q2, trv2))
    btn2.grid(row=0, column=12, padx=5, pady=3)

    cbtn2 = Button(wrapper2, text="Clear", command=lambda: clear2(trv2))
    cbtn2.grid(row=0, column=13, padx=5, pady=3)
# ==============================================================================


#============ space =============
    lbl11 = Label(wrapper2, text="")
    lbl11.grid(row=1, column=0, padx=5, pady=3)
# =======================



    wrapper4 = LabelFrame(root, text="Make Appoinemnt")
    wrapper4.pack(fill="both", expand="no", padx=10, pady=10, ipady=5,ipadx=5)

    lbl1 = Label(wrapper4,text="Patient Reg No")
    lbl1.grid(row=3, column=0, padx=5, pady=3,sticky = 'w')
    ent1 = Entry(wrapper4, textvariable=t1)
    ent1.grid(row=3, column=1, padx=5, pady=3)






    #doc=options.get()
    #slo=options2.get()

    lbl14 = Label(wrapper4, text="Select Doctor for make appoinment")
    lbl14.grid(row=3, column=2, padx=5, pady=3, sticky='w')
   # drop = OptionMenu(wrapper4, clicked, *options)
    entdco = Entry(wrapper4, textvariable=tDoc)
    entdco.config(state=DISABLED)
    entdco.grid(row=3, column=3, padx=5, pady=3)



    #ent15 = Entry(wrapper4, textvariable=t1)
    #ent15.grid(row=3, column=3, padx=5, pady=3)

    lbl2 = Label(wrapper4, text="Name",justify=LEFT)
    lbl2.grid(row=4, column=0, padx=5, pady=3,sticky = 'w')
    ent2 = Entry(wrapper4, textvariable=t2)
    ent2.grid(row=4, column=1, padx=5, pady=3)

    lbl14 = Label(wrapper4, text="Select Slot")
    lbl14.grid(row=4, column=2, padx=5, pady=3, sticky='w')
    drop2 = OptionMenu(wrapper4, clicked2, *options2)
    drop2.grid(row=4, column=3, padx=5, pady=3)



    lbl3 = Label(wrapper4, text="Sex")
    lbl3.grid(row=5, column=0, padx=5, pady=3,sticky = 'w')
    ent3 = Entry(wrapper4, textvariable=t3)
    ent3.grid(row=5, column=1, padx=5, pady=3)

    lbl4 = Label(wrapper4, text="Age")
    lbl4.grid(row=6, column=0, padx=5, pady=3,sticky = 'w')
    ent4 = Entry(wrapper4, textvariable=t4)
    ent4.grid(row=6, column=1, padx=5, pady=3)

    lbl5 = Label(wrapper4, text="Address")
    lbl5.grid(row=7, column=0, padx=5, pady=3, sticky='w')
    ent5 = Entry(wrapper4, textvariable=t5)
    ent5.grid(row=7, column=1, padx=5, pady=3)

    lbl6 = Label(wrapper4, text="Telephone No")
    lbl6.grid(row=8, column=0, padx=5, pady=3, sticky='w')
    ent6 = Entry(wrapper4, textvariable=t6)
    ent6.grid(row=8, column=1, padx=5, pady=3)

    patient_details_btn = Button(wrapper4, text="Patient Details", command=lambda:patient_details(t1,t2,t3,t4,t5,t6))
    add_btn = Button(wrapper4, text="Add Booking", command=lambda:add_appoinment(trv2,t1, t2, t3, t4, t5, t6,tDoc,clicked2.get()))
    clear_btn = Button(wrapper4, text="Clear All Booking", command=lambda:clear_all_booking(trv2))

    add_btn.grid(row=9, column=0, pady=5, padx=3,sticky = 'w')
    patient_details_btn.grid(row=9, column=2,sticky = 'w')
    clear_btn.grid(row=9, column=1,sticky = 'w')


    #======================== Appoinmnt==========================




    trv2.column("# 1", anchor=CENTER, stretch=NO, width=80)
    trv2.column("# 2", anchor=CENTER, stretch=NO, width=80)
    trv2.column("# 3", anchor=CENTER, stretch=NO, width=80)
    trv2.column("# 4", anchor=CENTER, stretch=NO, width=80)
    trv2.column("# 5", anchor=CENTER, stretch=NO, width=80)
    trv2.column("# 6", anchor=CENTER, stretch=NO, width=80)
    trv2.column("# 7", anchor=CENTER, stretch=NO, width=80)
    trv2.column("# 8", anchor=CENTER, stretch=NO, width=80)
    trv2.column("# 9", anchor=CENTER, stretch=NO, width=80)
    trv2.column("# 10", anchor=CENTER, stretch=NO, width=80)
    trv2.column("# 11", anchor=CENTER, stretch=NO, width=80)
    trv2.column("# 12", anchor=CENTER, stretch=NO, width=80)
    trv2.column("# 13", anchor=CENTER, stretch=NO, width=80)
    trv2.column("# 14", anchor=CENTER, stretch=NO, width=80)
    trv2.column("# 15", anchor=CENTER, stretch=NO, width=80)
    trv2.column("# 16", anchor=CENTER, stretch=NO, width=80)
    trv2.column("# 17", anchor=CENTER, stretch=NO, width=80)

    treeScroll2 = ttk.Scrollbar(wrapper3)
    treeScroll2.configure(command=trv2.yview)
    trv2.configure(yscrollcommand=treeScroll2.set)
    treeScroll2.pack(side=RIGHT, fill=BOTH)
    trv2.pack()
    trv2.pack()

    trv2.heading(1, text="Doc Reg No")
    trv2.heading(2, text="8.30-9.00")
    trv2.heading(3, text="9.00-9.30")
    trv2.heading(4, text="9.30-10.00")
    trv2.heading(5, text="10.00-10.30")
    trv2.heading(6, text="10.30-11.00")
    trv2.heading(7, text="11.00-11.30")
    trv2.heading(8, text="11.30-12.00")
    trv2.heading(9, text="12.00-12.30")
    trv2.heading(10, text="12.30-13.00")
    trv2.heading(11, text="14.00-14.30")
    trv2.heading(12, text="14.30-15.00")
    trv2.heading(13, text="15.00-15.30")
    trv2.heading(14, text="15.30-16.00")
    trv2.heading(15, text="16.00-16.30")
    trv2.heading(16, text="16.30-17.00")
    trv2.heading(17, text="17.00-17.30")

    lbl1Slot1 = Label(wrapper4, text="  Slot1: 8.30 - 9.00  ")
    lbl1Slot1.grid(row=3, column=4, padx=5, pady=3, sticky='w')

    lbl1Slot2 = Label(wrapper4, text="  Slot2: 9.00 - 9.30  ")
    lbl1Slot2.grid(row=4, column=4, padx=5, pady=3, sticky='w')

    lbl1Slot3 = Label(wrapper4, text="  Slot3: 9.30 - 10.00  ")
    lbl1Slot3.grid(row=5, column=4, padx=5, pady=3, sticky='w')

    lbl1Slot4 = Label(wrapper4, text="  Slot4: 10.00 - 10.30  ")
    lbl1Slot4.grid(row=6, column=4, padx=5, pady=3, sticky='w')

    lbl1Slot5 = Label(wrapper4, text="  Slot5: 10.30 - 11.00  ")
    lbl1Slot5.grid(row=7, column=4, padx=5, pady=3, sticky='w')

    lbl1Slot6 = Label(wrapper4, text="  Slot6: 11.00 - 11.30  ")
    lbl1Slot6.grid(row=8, column=4, padx=5, pady=3, sticky='w')

    lbl1Slot7 = Label(wrapper4, text="  Slot7: 11.30 - 12.00  ")
    lbl1Slot7.grid(row=9, column=4, padx=5, pady=3, sticky='w')

    lbl1Slot8 = Label(wrapper4, text="  Slot8: 12.00 - 12.30  ")
    lbl1Slot8.grid(row=3, column=5, padx=5, pady=3, sticky='w')

    lbl1Slot9 = Label(wrapper4, text="  Slot9: 12.30 - 13.00  ")
    lbl1Slot9.grid(row=4, column=5, padx=5, pady=3, sticky='w')

    lbl1Slot10 = Label(wrapper4, text="  Slot10: 14.00 - 14.30  ")
    lbl1Slot10.grid(row=5, column=5, padx=5, pady=3, sticky='w')

    lbl1Slot11 = Label(wrapper4, text="  Slot11: 14.30 - 15.00  ")
    lbl1Slot11.grid(row=6, column=5, padx=5, pady=3, sticky='w')

    lbl1Slot12 = Label(wrapper4, text="  Slot12: 15.00 - 15.30  ")
    lbl1Slot12.grid(row=7, column=5, padx=5, pady=3, sticky='w')

    lbl1Slot13= Label(wrapper4, text="  Slot13: 15.30 - 16.00  ")
    lbl1Slot13.grid(row=8, column=5, padx=5, pady=3, sticky='w')

    lbl1Slot14 = Label(wrapper4, text="  Slot14: 16.00 - 16.30  ")
    lbl1Slot14.grid(row=9, column=5, padx=5, pady=3, sticky='w')

    lbl1Slot15 = Label(wrapper4, text="  Slot15: 16.30 - 17.00  ")
    lbl1Slot15.grid(row=3, column=6, padx=5, pady=3, sticky='w')

    lbl1Slot16 = Label(wrapper4, text="  Slot16: 17.00 - 17.30  ")
    lbl1Slot16.grid(row=4, column=6, padx=5, pady=3, sticky='w')



    root.mainloop()
