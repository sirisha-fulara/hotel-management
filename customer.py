from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random
import mysql.connector
from tkinter import messagebox

class cust_win:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1100x500+250+230")

        # ----------------variables-------------
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_address=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()
        self.var_address=StringVar()

        # --------------title-----------------
        lbl_title=Label(self.root, text="Add Customer Details", font=("times new roman", 18, "bold"), bg="white", fg="black", bd=4, relief=RIDGE)
        lbl_title.place(x=0,y=0, width=1100,height=50)

        # ---------------label frame------------
        LabelFrameLeft=LabelFrame(self.root, bd=2, relief=RIDGE,text="Customer Details",font=("times new roman", 12, "bold"))
        LabelFrameLeft.place(x=5,y=50,width=425,height=500)

        # -----------------labels and entries-----------
        # custref
        lbl_cust_ref=Label(LabelFrameLeft, text="Customer Ref:",font=("times new roman", 12, "bold"), padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)
        entry_ref=ttk.Entry(LabelFrameLeft,textvariable=self.var_ref, width=29,font=("times new roman", 13, "bold"),state="readonly")
        entry_ref.grid(row=0,column=1)

        # cust name
        cname=Label(LabelFrameLeft, text="Customer Name:",font=("times new roman", 12, "bold"), padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)
        txtcname=ttk.Entry(LabelFrameLeft,textvariable=self.var_cust_name, width=29,font=("times new roman", 13, "bold"))
        txtcname.grid(row=1,column=1)

        #gender combobox
        lblGender=Label(LabelFrameLeft, text="Gender:",font=("times new roman", 12, "bold"), padx=2,pady=6)
        lblGender.grid(row=2,column=0,sticky=W)
        genderCombo=ttk.Combobox(LabelFrameLeft,textvariable=self.var_gender,font=("times new roman", 12, "bold"),width=31, state="readonly")
        genderCombo["value"]=("Male","Female", "Other")
        genderCombo.current(0)
        genderCombo.grid(row=2,column=1)

        #postcode
        lblPostCode=Label(LabelFrameLeft, text="PostCode:",font=("times new roman", 12, "bold"), padx=2,pady=6)
        lblPostCode.grid(row=3,column=0,sticky=W)
        txtPostCode=ttk.Entry(LabelFrameLeft,textvariable=self.var_post, width=29,font=("times new roman", 13, "bold"))
        txtPostCode.grid(row=3,column=1)

        #Mobile Number
        lblMobile=Label(LabelFrameLeft, text="Mobile:",font=("times new roman", 12, "bold"), padx=2,pady=6)
        lblMobile.grid(row=4,column=0,sticky=W)
        txtMobile=ttk.Entry(LabelFrameLeft,textvariable=self.var_mobile, width=29,font=("times new roman", 13, "bold"))
        txtMobile.grid(row=4,column=1)

        #Email
        lblEmail=Label(LabelFrameLeft, text="Email:",font=("times new roman", 12, "bold"), padx=2,pady=6)
        lblEmail.grid(row=5,column=0,sticky=W)
        txtEmail=ttk.Entry(LabelFrameLeft,textvariable=self.var_email, width=29,font=("times new roman", 13, "bold"))
        txtEmail.grid(row=5,column=1)

        #Nationality
        lblNationality=Label(LabelFrameLeft, text="Nationality:",font=("times new roman", 12, "bold"), padx=2,pady=6)
        lblNationality.grid(row=6,column=0,sticky=W)
        nationalityCombo=ttk.Combobox(LabelFrameLeft,textvariable=self.var_nationality,font=("times new roman", 12, "bold"), width=31, state="readonly")
        nationalityCombo["value"]=("Indian","American", "British")
        nationalityCombo.current(0)
        nationalityCombo.grid(row=6,column=1)

        #id proof type combobox
        lblIdProof=Label(LabelFrameLeft, text="Id Proof Type:",font=("times new roman", 12, "bold"), padx=2,pady=6)
        lblIdProof.grid(row=7,column=0,sticky=W)
        IdProofCombo=ttk.Combobox(LabelFrameLeft,textvariable=self.var_id_proof,font=("times new roman", 12, "bold"), width=31, state="readonly")
        IdProofCombo["value"]=("Adhaar Card","Passport", "Driving Liscence")
        IdProofCombo.current(0)
        IdProofCombo.grid(row=7,column=1)

        # id number
        lblIdNumber=Label(LabelFrameLeft, text="Id Number:",font=("times new roman", 12, "bold"), padx=2,pady=6)
        lblIdNumber.grid(row=8,column=0,sticky=W)
        txtIdNumber=ttk.Entry(LabelFrameLeft,textvariable=self.var_id_number, width=29,font=("times new roman", 13, "bold"))
        txtIdNumber.grid(row=8,column=1)

        # address
        lblAddress=Label(LabelFrameLeft, text="Address:",font=("times new roman", 12, "bold"), padx=2,pady=6)
        lblAddress.grid(row=9,column=0,sticky=W)
        txtAddress=ttk.Entry(LabelFrameLeft,textvariable=self.var_address, width=29,font=("times new roman", 13, "bold"))
        txtAddress.grid(row=9,column=1)

        # ---------------buttons------------------
        btn_frame=Frame(LabelFrameLeft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=360,width=412,height=40)

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
        table_frame.place(x=435,y=50,width=860,height=500)

        lblSearchBy=Label(table_frame,font=("times new roman", 12, "bold"),text="Search By:",)
        lblSearchBy.grid(row=0,column=0,sticky=W, padx=2)

        self.search_var=StringVar()
        SearchCombo=ttk.Combobox(table_frame,textvariable=self.search_var,font=("times new roman", 12, "bold"), width=15, state="readonly",)
        SearchCombo["value"]=("Mobile","Ref")
        SearchCombo.current(0)
        SearchCombo.grid(row=0,column=1, padx=2)  

        self.txt_search=StringVar()
        txtSearch=ttk.Entry(table_frame,textvariable=self.txt_search, width=24,font=("times new roman", 13, "bold"),)
        txtSearch.grid(row=0,column=2, padx=2)

        btn_Search=Button(table_frame,command=self.search,text="Search",font=("times new roman", 12, "bold"),bg="Grey",fg="Black",width=10)
        btn_Search.grid(row=0,column=3,padx=1)

        btn_ShowAll=Button(table_frame,command=self.fetch_data,text="Show All",font=("times new roman", 12, "bold"),bg="Grey",fg="Black",width=10)
        btn_ShowAll.grid(row=0,column=4,padx=1)

        # -----------------show data table----------------
        details_table= Frame(table_frame, bd=2,relief=RIDGE)
        details_table.place(x=0,y=50, width=650,height=300)

        scroll_x=ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table, orient=VERTICAL)

        self.cust_details_table=ttk.Treeview(details_table,columns=("ref","name","gender","postcode","mobile","email","nationality","idproof","idnumber","address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.cust_details_table.xview)
        scroll_y.config(command=self.cust_details_table.yview)

        self.cust_details_table.heading("ref",text="Refer No.")
        self.cust_details_table.heading("name",text="Name")
        self.cust_details_table.heading("gender",text="Gender")
        self.cust_details_table.heading("postcode",text="Post Code")
        self.cust_details_table.heading("mobile",text="Mobile")
        self.cust_details_table.heading("email",text="Email")
        self.cust_details_table.heading("nationality",text="Nationality")
        self.cust_details_table.heading("idproof",text="Id Proof")
        self.cust_details_table.heading("idnumber",text="Id No.")
        self.cust_details_table.heading("address",text="Address")

        self.cust_details_table["show"]="headings"

        self.cust_details_table.column("ref",width=100)
        self.cust_details_table.column("name",width=100)
        self.cust_details_table.column("gender",width=100)
        self.cust_details_table.column("postcode",width=100)
        self.cust_details_table.column("mobile",width=100)
        self.cust_details_table.column("email",width=100)
        self.cust_details_table.column("nationality",width=100)
        self.cust_details_table.column("idproof",width=100)
        self.cust_details_table.column("idnumber",width=100)
        self.cust_details_table.column("address",width=100)

        self.cust_details_table.pack(fill=BOTH, expand=1)
        self.cust_details_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_mobile.get()=="" or self.var_cust_name.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="sirisha27",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(self.var_ref.get(),
                                                                                                         self.var_cust_name.get(), 
                                                                                                         self.var_gender.get(),
                                                                                                         self.var_post.get(),
                                                                                                         self.var_mobile.get(),
                                                                                                         self.var_email.get(), 
                                                                                                         self.var_nationality.get(),
                                                                                                         self.var_id_proof.get(),
                                                                                                         self.var_id_number.get(),
                                                                                                         self.var_address.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Customer added!",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong{str(es)}.",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="sirisha27",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if(len(rows)!=0):
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in rows:
                self.cust_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,Event=""):
        cursor_row=self.cust_details_table.focus()
        content=self.cust_details_table.item(cursor_row)
        row=content["values"]

        self.var_ref.set(row[0])
        self.var_cust_name.set(row[1]) 
        self.var_gender.set(row[2])
        self.var_post.set(row[3])
        self.var_mobile.set(row[4])
        self.var_email.set(row[5]) 
        self.var_nationality.set(row[6])
        self.var_id_proof.set(row[7])
        self.var_id_number.set(row[8])
        self.var_address.set(row[9])

    def update(self):
        if(self.var_mobile.get()==""):
            messagebox.showerror("Error","Please fill Mobile field",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="sirisha27",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update customer set Name=%s, Gender=%s,PostCode=%s, Mobile=%s, Email=%s,Nationality=%s, Idproof=%s, IdNumber=%s, Address=%s where Ref=%s",(
                                                                                                         self.var_cust_name.get(), 
                                                                                                         self.var_gender.get(),
                                                                                                         self.var_post.get(),
                                                                                                         self.var_mobile.get(),
                                                                                                         self.var_email.get(), 
                                                                                                         self.var_nationality.get(),
                                                                                                         self.var_id_proof.get(),
                                                                                                         self.var_id_number.get(),
                                                                                                         self.var_address.get(),
                                                                                                         self.var_ref.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","stomer details updated successfully")

    def mDelete(self):
        delete=messagebox.askyesno("Hotel Management System", "Do you want to delete this entry?", parent=self.root)
        if delete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="sirisha27",database="management")
            my_cursor=conn.cursor()
            query="delete from customer where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        # self.var_ref.set("")
        self.var_cust_name.set("") 
        # self.var_gender.set("")
        self.var_post.set("")
        self.var_mobile.set("")
        self.var_email.set("") 
        # self.var_nationality.set("")
        # self.var_id_proof.set("")
        self.var_id_number.set("")
        self.var_address.set("")

        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="sirisha27",database="management")
        my_cursor=conn.cursor()
        search_column = str(self.search_var.get()).strip()
        search_value = "%" + str(self.txt_search.get()).strip() + "%"
        query = f"SELECT * FROM customer WHERE {search_column} LIKE %s"
        my_cursor.execute(query, (search_value,))
        # my_cursor.execute("select * from customer where "+ str(self.search_var.get())+ "LIKE'%" + str(self.txt_search.get())+ "%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in rows:
                self.cust_details_table.insert("",END, values=i)
            conn.commit()
        conn.close()
            

if __name__=="__main__":
    root=Tk()
    obj=cust_win(root)
    root.mainloop()
