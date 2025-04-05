from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox
from tkinter import END

class roomBooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1100x500+250+230")

        # ----------------variables-------------
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()

        # --------------title-----------------
        lbl_title=Label(self.root, text="Room Booking Details", font=("times new roman", 18, "bold"), bg="white", fg="black", bd=4, relief=RIDGE)
        lbl_title.place(x=0,y=0, width=1100,height=50)

        # ---------------label frame------------
        LabelFrameLeft=LabelFrame(self.root, bd=2, relief=RIDGE,text="Room Booking Details",font=("times new roman", 12, "bold"))
        LabelFrameLeft.place(x=5,y=50,width=425,height=500)

        # -----------------labels and entries-----------
        # cust_mobile
        lbl_cust_contact=Label(LabelFrameLeft, text="Customer Contact:",font=("times new roman", 12, "bold"), padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)
        entry_contact=ttk.Entry(LabelFrameLeft,textvariable=self.var_contact, width=20,font=("times new roman", 13, "bold"))
        entry_contact.grid(row=0,column=1,sticky=W)

        btn_fetch_data=Button(LabelFrameLeft,command=self.fetch_contact,text="Fetch",font=("times new roman", 10, "bold"),bg="Grey",fg="Black",width=6)
        btn_fetch_data.place(x=325,y=4)

        #check_in_date
        check_in_date=Label(LabelFrameLeft, text="Check-In Date:",font=("times new roman", 12, "bold"), padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)
        txt_check_in_date=ttk.Entry(LabelFrameLeft,textvariable=self.var_checkin, width=29,font=("times new roman", 13, "bold"))
        txt_check_in_date.grid(row=1,column=1)

        #check_out_date
        check_out_date=Label(LabelFrameLeft, text="Check-Out Date:",font=("times new roman", 12, "bold"), padx=2,pady=6)
        check_out_date.grid(row=2,column=0,sticky=W)
        txt_check_out_date=ttk.Entry(LabelFrameLeft,textvariable=self.var_checkout, width=29,font=("times new roman", 13, "bold"))
        txt_check_out_date.grid(row=2,column=1)

        #available room
        lbl_availableRoom=Label(LabelFrameLeft, text="Available Room:",font=("times new roman", 12, "bold"), padx=2,pady=6)
        lbl_availableRoom.grid(row=3,column=0,sticky=W)
        txt_availableRoom=ttk.Entry(LabelFrameLeft,textvariable=self.var_roomavailable ,width=29,font=("times new roman", 13, "bold"))
        txt_availableRoom.grid(row=3,column=1)

        #meal
        lbl_meal=Label(LabelFrameLeft, text="Meal:",font=("times new roman", 12, "bold"), padx=2,pady=6)
        lbl_meal.grid(row=4,column=0,sticky=W)
        txt_meal=ttk.Entry(LabelFrameLeft,textvariable=self.var_meal, width=29,font=("times new roman", 13, "bold"))
        txt_meal.grid(row=4,column=1)

        #No of days
        lbl_noOfDays=Label(LabelFrameLeft, text="No. of Days:",font=("times new roman", 12, "bold"), padx=2,pady=6)
        lbl_noOfDays.grid(row=5,column=0,sticky=W)
        txt_noOfDays=ttk.Entry(LabelFrameLeft,textvariable=self.var_noofdays, width=29,font=("times new roman", 13, "bold"))
        txt_noOfDays.grid(row=5,column=1)

        #paid tax
        lbl_paid_tax=Label(LabelFrameLeft, text="Paid Tax:",font=("times new roman", 12, "bold"), padx=2,pady=6)
        lbl_paid_tax.grid(row=6,column=0,sticky=W)
        txt_paid_tax=ttk.Entry(LabelFrameLeft,textvariable=self.var_paidtax, width=29,font=("times new roman", 13, "bold"))
        txt_paid_tax.grid(row=6,column=1)

        #subtotal
        lbl_subtotal=Label(LabelFrameLeft, text="Subtotal:",font=("times new roman", 12, "bold"), padx=2,pady=6)
        lbl_subtotal.grid(row=7,column=0,sticky=W)
        txt_subtotal=ttk.Entry(LabelFrameLeft,textvariable=self.var_actualtotal, width=29,font=("times new roman", 13, "bold"))
        txt_subtotal.grid(row=7,column=1)

        #Total cost
        lbl_total_cost=Label(LabelFrameLeft, text="Total Cost:",font=("times new roman", 12, "bold"), padx=2,pady=6)
        lbl_total_cost.grid(row=7,column=0,sticky=W)
        txt_total_cost=ttk.Entry(LabelFrameLeft,textvariable=self.var_total, width=29,font=("times new roman", 13, "bold"))
        txt_total_cost.grid(row=7,column=1)

        # -------------------bill btn-----------
        btn_bill=Button(LabelFrameLeft,command=self.total,text="Bill",font=("times new roman", 12, "bold"),bg="Grey",fg="Black",width=10)
        btn_bill.grid(row=8,column=0,padx=1)

        # -----------------btns----------------
        btn_frame=Frame(LabelFrameLeft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=340,width=412,height=40)

        btn_add=Button(btn_frame,text="Add",command=self.add_data,font=("times new roman", 12, "bold"),bg="Grey",fg="Black",width=10)
        btn_add.grid(row=0,column=0,padx=1)

        btn_update=Button(btn_frame,text="Update",command=self.update,font=("times new roman", 12, "bold"),bg="Grey",fg="Black",width=10)
        btn_update.grid(row=0,column=1,padx=1)

        btn_delete=Button(btn_frame,text="Delete",command=self.mDelete,font=("times new roman", 12, "bold"),bg="Grey",fg="Black",width=10)
        btn_delete.grid(row=0,column=2,padx=1)

        btn_reset=Button(btn_frame,text="Reset",command=self.reset,font=("times new roman", 12, "bold"),bg="Grey",fg="Black",width=10)
        btn_reset.grid(row=0,column=3,padx=1)

        # --------------table frame---------------
        table_frame=LabelFrame(self.root, bd=2, relief=RIDGE,text="View Details",font=("times new roman", 12, "bold"))
        table_frame.place(x=435,y=240,width=860,height=500)

        lblSearchBy=Label(table_frame,font=("times new roman", 12, "bold"),text="Search By:",)
        lblSearchBy.grid(row=0,column=0,sticky=W, padx=2)

        self.search_var=StringVar()
        SearchCombo=ttk.Combobox(table_frame,font=("times new roman", 12, "bold"), width=15, state="readonly",)
        SearchCombo["value"]=("Contact","Room")
        SearchCombo.current(0)
        SearchCombo.grid(row=0,column=1, padx=2)  

        self.txt_search=StringVar()
        txtSearch=ttk.Entry(table_frame, width=24,font=("times new roman", 13, "bold"),)
        txtSearch.grid(row=0,column=2, padx=2)

        btn_Search=Button(table_frame,command=self.search,text="Search",font=("times new roman", 12, "bold"),bg="Grey",fg="Black",width=10)
        btn_Search.grid(row=0,column=3,padx=1)

        btn_ShowAll=Button(table_frame,command=self.fetch_data,text="Show All",font=("times new roman", 12, "bold"),bg="Grey",fg="Black",width=10)
        btn_ShowAll.grid(row=0,column=4,padx=1)


        # -----------------show data table----------------
        details_table= Frame(table_frame, bd=2,relief=RIDGE)
        details_table.place(x=0,y=50, width=650,height=150)

        scroll_x=ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table, orient=VERTICAL)

        self.room_table=ttk.Treeview(details_table,columns=("contact","checkin","checkout","roomavailable","meal","noOfDays"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact",text="Contact")
        self.room_table.heading("checkin",text="Check-in")
        self.room_table.heading("checkout",text="Check-out")
        self.room_table.heading("roomavailable",text="Room Available")
        self.room_table.heading("meal",text="Meal")
        self.room_table.heading("noOfDays",text="No. Of Days")

        self.room_table["show"]="headings"

        self.room_table.column("contact",width=100)
        self.room_table.column("checkin",width=100)
        self.room_table.column("checkout",width=100)
        self.room_table.column("roomavailable",width=100)
        self.room_table.column("meal",width=100)
        self.room_table.column("noOfDays",width=100)

        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter contact number", parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="sirisha27",database="management")
            my_cursor=conn.cursor()
            query=("select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==NONE:
                messagebox.showerror("Error","Contact not found" , parent=self.root)
            else:
                conn.commit()
                conn.close()

                # displaying name
                showDataFrame=Frame(self.root, bd=4, relief=RIDGE, padx=2)
                showDataFrame.place(x=455,y=55,height=180,width=300)
                lblName=Label(showDataFrame, text="Name:", font=("arial",12,"bold"))
                lblName.place(x=0,y=0)
                lbl=Label(showDataFrame, text=row, font=("arial",12))
                lbl.place(x=100,y=0)

                # displaying gender
                conn=mysql.connector.connect(host="localhost",username="root",password="sirisha27",database="management")
                my_cursor=conn.cursor()
                query=("select Gender from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                lblGender=Label(showDataFrame, text="Gender:", font=("arial",12,"bold"))
                lblGender.place(x=0,y=30)
                lbl2=Label(showDataFrame, text=row, font=("arial",12))
                lbl2.place(x=100,y=30)

                # displaying email
                conn=mysql.connector.connect(host="localhost",username="root",password="sirisha27",database="management")
                my_cursor=conn.cursor()
                query=("select Email from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                lblEmail=Label(showDataFrame, text="Email:", font=("arial",12,"bold"))
                lblEmail.place(x=0,y=60)
                lbl3=Label(showDataFrame, text=row, font=("arial",12))
                lbl3.place(x=100,y=60)

                # displaying nationality
                conn=mysql.connector.connect(host="localhost",username="root",password="sirisha27",database="management")
                my_cursor=conn.cursor()
                query=("select Nationality from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                lblNationality=Label(showDataFrame, text="Nationality:", font=("arial",12,"bold"))
                lblNationality.place(x=0,y=90)
                lbl4=Label(showDataFrame, text=row, font=("arial",12))
                lbl4.place(x=100,y=90)

                # displaying address
                conn=mysql.connector.connect(host="localhost",username="root",password="sirisha27",database="management")
                my_cursor=conn.cursor()
                query=("select Address from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                lblAddress=Label(showDataFrame, text="Address:", font=("arial",12,"bold"))
                lblAddress.place(x=0,y=120)
                lbl5=Label(showDataFrame, text=row, font=("arial",12))
                lbl5.place(x=100,y=120)

    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="sirisha27",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s, %s, %s, %s, %s, %s, %s)",(self.var_contact.get(),
                                                                                            self.var_checkin.get(),
                                                                                            self.var_checkout.get(),
                                                                                            self.var_roomtype.get(),
                                                                                            self.var_roomavailable.get(),
                                                                                            self.var_meal.get(),
                                                                                            self.var_noofdays.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Customer added!",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong{str(es)}.",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="sirisha27",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if(len(rows)!=0):
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,Event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_meal.set(row[5])
        self.var_noofdays.set(row[6])

    def update(self):
        if(self.var_contact.get()==""):
            messagebox.showerror("Error","Please fill Contact field",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="sirisha27",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update room set check_in=%s,check_out=%s, roomtype=%s, roomavailable=%s,meal=%s, noOfDays=%s where Contact=%s",(
                self.var_checkin.get(),
                self.var_checkout.get(),
                self.var_roomtype.get(),
                self.var_roomavailable.get(),
                self.var_meal.get(),
                self.var_noofdays.get(),
                self.var_contact.get()))
                                                                                     
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room details updated successfully")
    
    def mDelete(self):
        delete=messagebox.askyesno("Hotel Management System", "Do you want to delete this entry?", parent=self.root)
        if delete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="sirisha27",database="management")
            my_cursor=conn.cursor()
            query="delete from room where Contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_contact.set("") 
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_meal.set("") 
        self.var_noofdays.set("")
        self.var_roomavailable.set("")

    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noofdays.set(abs(outDate-inDate).days)

        if(self.var_meal.get()=='Breakfast' or self.var_meal.get()=='breakfast'):
            q1=float(300)
            days=float(self.var_noofdays.get())
            bill=float(q1*days)
            tax="Rs" + str("%.2f"%(bill*0.1))
            subtot="Rs" + str("%.2f"%(bill))
            total="Rs" + str("%.2f"%(bill + (bill*0.1)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(subtot)
            self.var_total.set(total)

        elif(self.var_meal.get()=='Lunch' or self.var_meal.get()=='lunch'):
            q1=float(500)
            days=float(self.var_noofdays.get())
            bill=float(q1*days)
            tax="Rs" + str("%.2f"%(bill*0.1))
            subtot="Rs" + str("%.2f"%(bill))
            total="Rs" + str("%.2f"%(bill + (bill*0.1)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(subtot)
            self.var_total.set(total)

        if(self.var_meal.get()=='Dinner' or self.var_meal.get()=='dinner'):
            q1=float(700)
            days=float(self.var_noofdays.get())
            bill=float(q1*days)
            tax="Rs" + str("%.2f"%(bill*0.1))
            subtot="Rs" + str("%.2f"%(bill))
            total="Rs" + str("%.2f"%(bill + (bill*0.1)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(subtot)
            self.var_total.set(total)

    def search(self):
        try:

            conn=mysql.connector.connect(host="localhost",username="root",password="sirisha27",database="management")
            my_cursor = conn.cursor()

            # Get input values
            search_column = str(self.search_var.get()).strip()  # Column to search
            search_value = str(self.txt_search.get()).strip()   # Value to search

            # Check for empty values
            if not search_column or not search_value:
                print("Please select a column and enter a search value.")
                return

            # Validate column to avoid SQL injection
            valid_columns = ["room_no", "room_type", "status"]  # Replace with actual table columns
            if search_column not in valid_columns:
                print("Invalid column selected.")
                return

            # Construct and execute the query
            query = f"SELECT * FROM room WHERE {search_column} LIKE %s"
            my_cursor.execute(query, (f"%{search_value}%",))
            rows = my_cursor.fetchall()

            # Display the results
            if rows:
                self.room_table.delete(*self.room_table.get_children())  # Clear old data
                for row in rows:
                    self.room_table.insert("", END, values=row)  # Insert new data
                conn.commit()
            else:
                print("No records found.")

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        finally:
            conn.close()
    
if __name__=="__main__":
    root=Tk()
    obj=roomBooking(root)
    root.mainloop()