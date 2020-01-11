from tkinter import *
from tkinter import messagebox
import csv


class Student_A:
    def __init__(self):
        self.w1 = Tk()
        self.w1.title("This is w ")
        # self.w2=Tk() # This is directly call
        # self.w2.title("This is w2")
        #  self.w2=Toplevel(self.w) # This take will call by (self.w)

        # Login OR Main Page
        self.f1 = Frame(self.w1, bg="skyblue", height=300, width=250)
        self.f1.pack()
        self.f1.propagate("a" in "bcd")
        #  Register Frame
        # self.f2=Frame(self.w2, bg="skyblue", height=300, width=250)
        # self.f2.pack()
        # self.f2.propagate("a" in "bcd")

        self.l1 = Label(self.f1, bg="skyblue", fg="skyblue").pack()
        self.l2 = Label(self.f1, fg="black", bg="Skyblue", text="Welcome").pack()
        self.l3 = Label(self.f1, bg="skyblue").pack()
        self.l5 = Label(self.f1, fg="black", bg="Skyblue", text="Username:").pack()
        self.e1 = Entry(self.f1)
        self.e1.pack()
        self.l6 = Label(self.f1, fg="black", bg="Skyblue", text="Password:").pack()
        self.e2 = Entry(self.f1)
        self.e2.pack()
        self.l3 = Label(self.f1, bg="skyblue").pack()
        self.l3 = Label(self.f1, bg="skyblue").pack()  # this is for giving extra space
        # self.b1=Button(self.f,text="login").pack()
        self.b1 = Button(self.f1, text="Login", command=self.login)
        self.b1.place(x=105, y=150)
        self.l4 = Label(self.f1, text="Or ", bg="skyblue")
        self.l4.place(x=115, y=180)
        self.b2 = Button(self.f1, text=" Student Register", command=self.register)
        self.b2.place(x=20, y=200)
        self.b3 = Button(self.f1, text=" Faculty Login ")
        self.b3.place(x=130, y=200)

        #Registration Frame
        self.f2 = Frame(self.w1, bg="skyblue", height=300, width=250)
        #self.f2.pack()
        self.f2.propagate("a" in "bcd")
        self.l8 = Label(self.f2, bg="skyblue").pack()
        self.l7 = Label(self.f2, text="Enter Your Details", bg="skyblue").pack()
        self.l8 = Label(self.f2, bg="skyblue").pack()
        self.l9 = Label(self.f2, text="Name : ", bg="skyblue").pack()
        self.e3 = Entry(self.f2)
        self.e3.pack()
        self.l10 = Label(self.f2, text="Phone Number : ", bg="skyblue").pack()
        self.e4 = Entry(self.f2)
        self.e4.pack()
        self.l10 = Label(self.f2, text="Password : ", bg="skyblue").pack()
        self.e5 = Entry(self.f2, show="*")
        self.e5.pack()
        self.b2 = Button(self.f2, text="Register", command=self.register_info)
        self.b2.place(x=105, y=200)
        self.l11 = Label(self.f2, bg="skyblue")
        self.l11.place(x=70, y=240)

    def login(self):
        if self.e1.get() == "" or self.e2.get() == "":
            messagebox.showerror("Error", "All fields are required !")
        else:
            print("working...")
            # first delete the username and password from frame f1
            name=self.e1.get()
            pwd=self.e2.get()
            with open("data.csv", 'r') as f:
                data = csv.reader(f)
                #print(data)
                for row in data:
                    #print(row[0], row[2])
                    if row[0]==name:
                        if row[2]==pwd:
                            print("Login Successful")
                            break
                        else:
                            print("PWD does not match")
                            break
                else:
                    print("username doesnot exist")

            self.e1.delete(0, END)
            self.e2.delete(0, END)

            # now we wanted to verify this one
            with open("data1.csv", 'r') as f:
                data = f.readlines()
            #

    def register(self):
        self.f1.pack_forget()
        self.f2.pack()

    def register_info(self):
        if self.e3.get() =="" or self.e4.get() =="" or self.e5.get() =="":
            messagebox.showerror("Error", "All fields are required !")
        else:
            self.l11["text"]="Successful"                      #
            with open("data.csv", 'a')as f:
                f.write(self.e3.get()+","+ self.e4.get()+","+ self.e5.get()+"\n")
            self.e3.delete(0, END)
            self.e4.delete(0, END)
            self.e5.delete(0, END)



Student_A()
mainloop()