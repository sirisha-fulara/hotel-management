from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO
from customer import cust_win
from room import roomBooking
from details import details

class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

        # -----------1st Image--------------
        # Downloading image from URL
        url = "https://media.istockphoto.com/id/104731717/photo/luxury-resort.jpg?s=612x612&w=0&k=20&c=cODMSPbYyrn1FHake1xYz9M8r15iOfGz9Aosy9Db7mI="
        response = requests.get(url)  # Fetch image from the internet
        img1 = Image.open(BytesIO(response.content))  # Open image from bytes
        img1 = img1.resize((1550, 140))  # Resize image
        self.photoImage1 = ImageTk.PhotoImage(img1)  # Convert to Tkinter image
        # Displaying Image in Label
        lblimg = Label(self.root, image=self.photoImage1, border=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1550, height=140)

        # --------------logo----------------
        img2 = Image.open("D:\Python+MySQL Project\images\logo.png")  # Open image from bytes
        img2 = img2.resize((200, 140))  # Resize image
        self.photoImage2 = ImageTk.PhotoImage(img2)  # Convert to Tkinter image
        # Displaying Image in Label
        lblimg = Label(self.root, image=self.photoImage2, border=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=200, height=140)

        # --------------title-----------------
        lbl_title=Label(self.root, text="HOTEL MANAGEMENT SYSTEM", font=("times new roman", 40, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0,y=140, width=1550,height=50)

        # ----------------main frame-------------
        main_frame= Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0,y=200,width=1550,height=650)

        # ------------------menu-------------------
        lbl_menu=Label(main_frame, text="MENU", font=("times new roman", 20, "bold"), bg="grey", fg="black", bd=4, relief=RIDGE)
        lbl_menu.place(x=0,y=0, width=240)

        # -------------------btn frame---------------
        btn_frame= Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0,y=35,width=240,height=170)

        cust_btn= Button(btn_frame,text="Customer",command=self.cust_details, font=("times new roman", 14, "bold"), bg="white", fg="black", cursor="hand2" ,width=20)
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn= Button(btn_frame,text="Room",command=self.roomBooking, font=("times new roman", 14, "bold"), bg="white", fg="black", cursor="hand2" ,width=20)
        room_btn.grid(row=1,column=0,pady=1)

        details_btn= Button(btn_frame,text="Details",command=self.details, font=("times new roman", 14, "bold"), bg="white", fg="black", cursor="hand2" ,width=20)
        details_btn.grid(row=2,column=0,pady=1)

        # report_btn= Button(btn_frame,text="Report", font=("times new roman", 14, "bold"), bg="white", fg="black", cursor="hand2" ,width=20)
        # report_btn.grid(row=3,column=0,pady=1)

        logout_btn= Button(btn_frame,text="Logout", command=self.logout, font=("times new roman", 14, "bold"), bg="white", fg="black", cursor="hand2" ,width=20)
        logout_btn.grid(row=4,column=0,pady=1)

        


    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=cust_win(self.new_window)

    def roomBooking(self):
        self.new_window=Toplevel(self.root)
        self.app=roomBooking(self.new_window)

    def details(self):
        self.new_window=Toplevel(self.root)
        self.app=details(self.new_window)

    def logout(self):
        self.root.destroy()



if __name__ == "__main__":
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()