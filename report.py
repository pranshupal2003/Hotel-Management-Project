from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
 

class Report:
    def __init__(self,root):
        self.root=root
        self.root.title("Developer Window")
        self.root.geometry("1295x550+230+220")

        self.bg=ImageTk.PhotoImage(file=r"D:\Attenance_Login\hotel images\developer.jpg")
        lbl_bg1=Label(self.root,image=self.bg)
        lbl_bg1.place(x=0,y=0,relwidth=1,relheight=1)
        
        #===============title===============================
        lbl_title1=Label(self.root,text="DEVELOPED BY : PRANSHU PAL" ,font=("TIMES NEW ROMAN",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title1.place(x=0,y=440,width=1550)
        


if __name__=="__main__":
    root=Tk()
    app=Report(root)
    root.mainloop()