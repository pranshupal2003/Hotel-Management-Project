from tkinter import *
from PIL import Image, ImageTk
from customer import Customer_Window
from room import Roombooking
from report import Report
from details import DetailsRoom

class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("The Great Grand Hotel")
        self.root.geometry("1550x800+0+0")


        #==============First Image=======================

        img1 = Image.open(r"D:\Attenance_Login\hotel images\hotel1.png")
        img1 = img1.resize((1550, 140),Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1550, height=140)

        #================Logo=======================

        img2 = Image.open(r"D:\Attenance_Login\hotel images\logohotel.png")
        img2 = img2.resize((230, 140),Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=230, height=140)


        #===============title===============================
        lbl_title=Label(self.root,text="THE GREAT GRAND HOTEL" ,font=("TIMES NEW ROMAN",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)

        #=========================main frame===================
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)

        #===============================Menu=========================
        lbl_menu=Label(main_frame,text="MENU" ,font=("TIMES NEW ROMAN",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)

         #=========================Btn frame===================
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=190)

        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22,font=("TIMES NEW ROMAN",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn=Button(btn_frame,text="ROOM",command=self.roombooking,width=22,font=("TIMES NEW ROMAN",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1)

        details_btn=Button(btn_frame,text="DETAILS",command=self.details_room,width=22,font=("TIMES NEW ROMAN",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        details_btn.grid(row=2,column=0,pady=1)

        report_btn=Button(btn_frame,text="REPORT",command=self.developer_report,width=22,font=("TIMES NEW ROMAN",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        report_btn.grid(row=3,column=0,pady=1)

        logout_btn=Button(btn_frame,text="LOGOUT",command=self.logout,width=22,font=("TIMES NEW ROMAN",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        logout_btn.grid(row=4,column=0,pady=1)


        #================================RIght Side Image=========================
        img3 = Image.open(r"D:\Attenance_Login\hotel images\slide3.jpg")
        img3= img3.resize((1310, 590),Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg1 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg1.place(x=225, y=0, width=1300, height=590)

        #======================Down Image======================================
        img4 = Image.open(r"D:\Attenance_Login\hotel images\myh.jpg")
        img4= img4.resize((230, 210),Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lblimg1 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=225, width=230, height=210)

        img5 = Image.open(r"D:\Attenance_Login\hotel images\khana.jpg")
        img5= img5.resize((230, 190),Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lblimg1 = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=420, width=230, height=190)

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Customer_Window(self.new_window)

    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window)

    def details_room(self):
        self.new_window=Toplevel(self.root)
        self.app=DetailsRoom(self.new_window)

    def developer_report(self):
        self.new_window=Toplevel(self.root)
        self.app=Report(self.new_window)

    def logout(self):
        self.root.destroy()

    




















if __name__ == "__main__":
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()
