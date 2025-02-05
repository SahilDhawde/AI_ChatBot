from tkinter import *
import tkinter as tk
from Alchatbot import bot_name, msgg


class chatbot:

    def __init__(self,root):
        self.root=root
        self.chat_window()

        

    def chat_window(self):
        self.root.title("Al ChatBot -- Sahil Dhawde")

        self.root.geometry("550x470+0+0")

        title2=Label(self.root,text="ChatBot",font=("Scheherazade",15,"bold"),bg="#828282",fg="white",padx="10",pady="10")
        title2.place(relwidth=1)

        line = Label(self.root,width=450,bg="red")
        line.place(relwidth=1, relheight=0.012, rely=0.10,)

        self.text_view=Text(self.root,width=20,height=2,bg="dark blue",fg='White',font=("Scheherazade",10,"bold"),padx=5,pady=5)
        self.text_view.place(relheight=0.745,relwidth=1,rely=0.11)
        self.text_view.configure(cursor='arrow',state=DISABLED)

        scroolbar=Scrollbar(self.text_view)
        scroolbar.place(relheight=1,relx=0.974)
        scroolbar.configure(command=self.text_view.yview)

        bottom_label= Label(self.root,bg="Dark Grey",height=80)
        bottom_label.place(relwidth=1,y=403)

        self.msg_entry=Entry(bottom_label,bg="#2c3e50",fg='white',font=("Scheherazade",10,"bold"),)
        self.msg_entry.place(relwidth=0.74,relheight=0.05,rely=0.0008,relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>",self.enter_pressed)

        send_button=Button(bottom_label,text="Send",font=("Scheherazade",10,"bold"),width=20,bg="Dark Grey",
        command=lambda: self.enter_pressed(None))
        send_button.place(x=415,y=3,height=55,width=126)

    def enter_pressed(self,event):
        msg= self.msg_entry.get()
        self.insert_msg(msg,"You")


    def insert_msg(self,msg,sender):
        if not msg:
            return

        self.msg_entry.delete(0,END)
        msg1= f"{sender}: {msg}\n\n"
        self.text_view.configure(state=NORMAL)
        self.text_view.insert(END,msg1)
        self.text_view.configure(state=DISABLED)

        self.msg_entry.delete(0,END)
        msg2= f"{bot_name}: {msgg(msg)}\n\n"
        self.text_view.configure(state=NORMAL)
        self.text_view.insert(END,msg2)
        self.text_view.configure(state=DISABLED)





    

if __name__ == "__main__":
    root = Tk()
    obj = chatbot(root)
    root.resizable(False,False)
    root.mainloop()





