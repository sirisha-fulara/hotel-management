from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox
from tkinter import END

class details:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1100x500+250+230")

        # --------------title-----------------
        lbl_title=Label(self.root, text="Details", font=("times new roman", 18, "bold"), bg="white", fg="black", bd=4, relief=RIDGE)
        lbl_title.place(x=0,y=0, width=1100,height=50)

        # ---------------label frame------------
        LabelFrameLeft=LabelFrame(self.root, bd=2, relief=RIDGE,text="Add New Room",font=("times new roman", 12, "bold"))
        LabelFrameLeft.place(x=5,y=50,width=450,height=350)

        # floor
        self.var_floor=StringVar()
        lbl_floor=Label(LabelFrameLeft, text="Floor:",font=("times new roman", 12, "bold"), padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W)
        entry_floor=ttk.Entry(LabelFrameLeft,textvariable=self.var_floor, width=20,font=("times new roman", 13, "bold"))
        entry_floor.grid(row=0,column=1,sticky=W)

        #room no
        self.var_roomno=StringVar()
        roomNo=Label(LabelFrameLeft, text="Room No.:",font=("times new roman", 12, "bold"), padx=2,pady=6)
        roomNo.grid(row=1,column=0,sticky=W)
        txt_roomNo=ttk.Entry(LabelFrameLeft,textvariable=self.var_roomno, width=29,font=("times new roman", 13, "bold"))
        txt_roomNo.grid(row=1,column=1)

        #room type
        self.var_roomtype=StringVar()
        roomType=Label(LabelFrameLeft, text="Room Type:",font=("times new roman", 12, "bold"), padx=2,pady=6)
        roomType.grid(row=2,column=0,sticky=W)
        txt_roomType=ttk.Entry(LabelFrameLeft, textvariable=self.var_roomtype, width=29,font=("times new roman", 13, "bold"))
        txt_roomType.grid(row=2,column=1)

        # -----------------btns----------------
        btn_frame=Frame(LabelFrameLeft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=150,width=400,height=40)

        btn_add=Button(btn_frame,text="Add",command=self.add_data,font=("times new roman", 12, "bold"),bg="Grey",fg="Black",width=10)
        btn_add.grid(row=0,column=0,padx=1)

        btn_update=Button(btn_frame,text="Update",command=self.update,font=("times new roman", 12, "bold"),bg="Grey",fg="Black",width=10)
        btn_update.grid(row=0,column=1,padx=1)

        btn_delete=Button(btn_frame,text="Delete",command=self.mDelete,font=("times new roman", 12, "bold"),bg="Grey",fg="Black",width=10)
        btn_delete.grid(row=0,column=2,padx=1)

        btn_reset=Button(btn_frame,text="Reset",command=self.reset,font=("times new roman", 12, "bold"),bg="Grey",fg="Black",width=10)
        btn_reset.grid(row=0,column=3,padx=1)

        table_frame=LabelFrame(self.root, bd=2, relief=RIDGE,text="Add New Room",font=("times new roman", 12, "bold"))
        table_frame.place(x=480,y=50,width=600,height=350)
        scroll_x=ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.room_table=ttk.Treeview(table_frame,columns=("floor","roomNo","roomType"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("floor",text="Floor")
        self.room_table.heading("roomNo",text="Room No.")
        self.room_table.heading("roomType",text="Room Type")

        self.room_table["show"]="headings"

        self.room_table.column("floor",width=100)
        self.room_table.column("roomNo",width=100)
        self.room_table.column("roomType",width=100)

        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    def add_data(self):
        if self.var_floor.get()=="" or self.var_roomno.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="sirisha27",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values(%s, %s, %s)",(self.var_floor.get(),
                                                                            self.var_roomno.get(),
                                                                            self.var_roomtype.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room added!",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong{str(es)}.",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="sirisha27",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
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

        self.var_floor.set(row[0])
        self.var_roomno.set(row[1])
        self.var_roomtype.set(row[2])
    
    def update(self):
        if(self.var_roomno.get()==""):
            messagebox.showerror("Error","Please fill Room No field",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="sirisha27",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update details set floor=%s, roomType=%s where roomNo=%s",(
                self.var_floor.get(),
                self.var_roomtype.get(),
                self.var_roomno.get(),))
                                                                                     
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room details updated successfully")

    def mDelete(self):
        delete=messagebox.askyesno("Hotel Management System", "Do you want to delete this entry?", parent=self.root)
        if delete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="sirisha27",database="management")
            my_cursor=conn.cursor()
            query="delete from details where roomNo=%s"
            value=(self.var_roomno.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_floor.set("") 
        self.var_roomno.set("")
        self.var_roomtype.set("")
        

if __name__=="__main__":
    root=Tk()
    obj=details(root)
    root.mainloop()