from tkinter import *
from tkinter import messagebox
import os
# import sys

root3 = Tk()

user = StringVar()
passw = StringVar()


class LoginP:
    def __init__(self, master):
        master.geometry("1920x1080")
        self.frame = Frame(master, width=1920, height=1080, bg="#a64dff")
        self.photo1 = PhotoImage(file="login2.png")
        self.label1 = Label(self.frame, bg="#a64dff", image=self.photo1)
        self.label1.place(x=640, y=45)

        # self.frame2 = Frame(self.frame, bg="#9933ff")
        # self.frame2.place(x=0, y=330)
        self.photo2 = PhotoImage(file="exit.png")

        self.frame3 = Frame(self.frame, width=900, height=450, bg="#a64dff")
        self.username = Label(self.frame3, text="Username ", font="Consolas 30", bg="#a64dff")
        self.username.grid(row=0, column=1)
        self.username_entry = Entry(self.frame3, textvariable=user, bd=8, font="0 30", bg="#a366ff")
        self.username_entry.grid(row=0, column=2)
        self.password1 = Label(self.frame3, text="Password ", font="Consolas 30", bg="#a64dff")
        self.password1.grid(row=3, column=1)
        self.password_entry = Entry(self.frame3, textvariable=passw,bd=8 , font="Consolas 30", show='*', bg="#a366ff")
        self.password_entry.grid(row=3, column=2)
        self.submit = Button(self.frame3, text="Submit", command=self.Check, font="times 25", bg="#a64dff")
        self.submit.grid(row=5, column=1)
        self.button1 = Button(self.frame3, image=self.photo2, command=q, bg="#a64dff")
        self.button1.grid(row=5, column=2)
        self.frame3.place(x=400, y=300)
        self.frame.pack()

    def Check(self):
        if (user.get() == str("admin")) and (passw.get() == str("12345")):
            os.system('HomePage.py')
            root3.destroy()
        elif (user.get() == str("")) and (passw.get() == str("")):
            messagebox.showerror("error", "Please Input Username and password")
        else:
            messagebox.showerror("error", "Incorrect Username or password")


def q():
    answer = messagebox.askquestion("Exit", "Do you really want to exit?")
    if answer == "yes":
        root3.quit()


root3.title("Supermarket System")
a = LoginP(root3)
root3.mainloop()
