from tkinter import *
from tkinter import messagebox
import csv


class Student_A:
    def __init__(self):
        self.w1 = Tk()
        self.w1.title("Student INfo ")
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

# =============================== Student login  ( FRAME 1)

        self.l1 = Label(self.f1, bg="skyblue", fg="skyblue").pack()
        self.l2 = Label(self.f1, fg="black", bg="Skyblue", text="Student Login").pack()
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
        self.b1.place(x=105, y=198)
        self.l4 = Label(self.f1, text="Or ", bg="skyblue")
        self.l4.place(x=115, y=220)
        self.b2 = Button(self.f1, text=" Student Register", command=self.register)
        self.b2.place(x=10, y=240)
        self.b3 = Button(self.f1, text=" Faculty Login ",command=self.faculty_login)
        self.b3.place(x=140, y=240)

#====================================Registration Frame

        self.f2 = Frame(self.w1, bg="skyblue", height=300, width=250)
        #self.f2.pack()  #pack() this in button
        self.f2.propagate("a" in "bcd")
        self.l8 = Label(self.f2, bg="skyblue").pack()
        self.l7 = Label(self.f2, text="Student Registration", bg="skyblue").pack()
        self.l8 = Label(self.f2, bg="skyblue").pack()
        self.l9 = Label(self.f2, text=" Student Name : ", bg="skyblue").pack()
        self.e3 = Entry(self.f2)
        self.e3.pack()
        self.l10 = Label(self.f2, text="Phone Number : ", bg="skyblue").pack()
        self.e4 = Entry(self.f2)
        self.e4.pack()
        self.l10 = Label(self.f2, text="Password : ", bg="skyblue").pack()
        self.e5 = Entry(self.f2, show="*")
        self.e5.pack()
        self.b2 = Button(self.f2, text="Register", command=self.register_info)
        self.b2.place(x=105, y=240)
        self.l11 = Label(self.f2, bg="skyblue")
        self.l11.place(x=70, y=260)
#===================== Back button from registration
        self.b4=Button(self.f2,text="Back",command=self.back)
        self.b4.place(x=2,y=2)

#===================== Faculty Login frame 3

        self.f3 = Frame(self.w1, bg="skyblue", height=300, width=250)
        self.f3.propagate("a" in "bcd")

        self.l1 = Label(self.f3, bg="skyblue", fg="skyblue").pack()
        self.l2 = Label(self.f3, fg="black", bg="Skyblue", text="Faculty Login").pack()
        self.l3 = Label(self.f3, bg="skyblue").pack()
        self.l5 = Label(self.f3, fg="black", bg="Skyblue", text="Username:").pack()
        self.e6 = Entry(self.f3)
        self.e6.pack()
        self.l6 = Label(self.f3, fg="black", bg="Skyblue", text="Password:").pack()
        self.e7 = Entry(self.f3)



        self.e7.pack()
        self.l3 = Label(self.f3, bg="skyblue").pack()
        self.l3 = Label(self.f3, bg="skyblue").pack()  # this is for giving extra space
        # self.b1=Button(self.f,text="login").pack()
        self.b1 = Button(self.f3, text="Login" , command=self.faculty_win)
        self.b1.place(x=105, y=200)

    #================== Frame Faculty

        ##=======================  iNisde FAculty Frame

        self.facultyMain = Frame(self.w1, bg="sky blue")
        #self.facultyMain.pack()
        # self.f1.propagate("a" in "bcd")
        self.l1 = Label(self.facultyMain, text="Data of students", padx=1300, bg="sky blue", pady=10,
                        font=('arial', 35, 'bold'))
        self.l1.pack()
        # bottom frame
        self.facultybottom = Frame(self.w1, width=1400, height=60)

        self.b1 = Button(self.facultybottom, text="Edit", font=('arial', 20, 'bold'), bd=4, height=1, width=10)
        self.b1.grid(row=0, column=0)

        self.b1 = Button(self.facultybottom, text="Edit", font=('arial', 20, 'bold'), bd=4, height=1, width=10)
        self.b1.grid(row=0, column=1)
        #self.facultybottom.pack(side=BOTTOM)

        # Data frame
        self.facultydata = Frame(self.w1, width=800, height=600, padx=20, bg="white")

        self.l31 = Label(self.facultydata, text="Student ID:")
        self.l31.grid(row=0, column=0)
        self.e31 = Entry(self.facultydata)
        self.e31.grid(row=0, column=1)

        self.l32 = Label(self.facultydata, text="First Name: ")
        self.l32.grid(row=2, column=0)
        self.e32 = Entry(self.facultydata)
        self.e32.grid(row=2, column=1)

        self.l33 = Label(self.facultydata, text="Last Name:")
        self.l33.grid(row=4, column=0)
        self.e33 = Entry(self.facultydata)
        self.e33.grid(row=4, column=1)

        self.l34 = Label(self.facultydata, text="Hobbies:")
        self.l34.grid(row=5, column=0)
        self.e34 = Entry(self.facultydata)
        self.e34.grid(row=5, column=1)

        self.l34 = Label(self.facultydata, text="Achievement's : ")
        self.l34.grid(row=6, column=0)
        self.e34 = Entry(self.facultydata)
        self.e34.grid(row=6, column=1)  # i wann increase length

        #self.facultydata.pack(side=LEFT)
        self.facultydata.grid_propagate(0)

        self.l3 = Label(self.facultydata, text="Student Info", pady=5, font=('arial', 25, 'bold'))
        self.l3.grid_propagate(0)
        # Right FRame
        self.facultyRight = Frame(self.w1, width=550, height=600, padx=20)
        self.s = Scrollbar(self.facultyRight)
        self.s.grid(row=0, column=1, sticky='ns')
        self.li = Listbox(self.facultyRight, width=100, height=37)
        self.li.grid(row=0, column=0)
        #self.facultyRight.pack(side=RIGHT)
        self.l4 = Label(self.facultyRight, text="Student Details", pady=5, font=('arial', 25, 'bold'))
        self.l4.place(x=200, y=10)

        #================ back button
        self.b4 = Button(self.f3, text="Back", command=self.back)
        self.b4.place(x=2, y=2)





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
                            self.l12=Label(self.f1,text="")
                            print("Login Successful")
                            break
                        else:
                            self.l12=Label(self.f1,text="PWD does not match",bg="sky blue",fg="red")
                            self.l12.pack()
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
                f.write(self.e3.get()+","+self.e4.get()+","+self.e5.get()+"\n")
                #f.write (f"{self.e3.get(),self.e4.get(),self.e5.get()}\n") this is wrong method it will create Tuple
            self.e3.delete(0, END)
            self.e4.delete(0, END)
            self.e5.delete(0, END)
    def back(self):
        self.f2.forget()
        self.f3.forget()
        self.f1.pack()


    def faculty_login(self):
        self.f1.pack_forget()
        self.f3.pack()


    def faculty_win(self):
        if self.e6.get() =="" or self.e7.get()=="":
            messagebox.showerror("Error","All fields are required !")
        else:
            fac_name=self.e6.get()
            fac_pwd=self.e7.get()
            if fac_name=="f":
                if fac_pwd=="f":
                    print("Successful")
                    self.f3.pack_forget()
                    self.facultyMain.pack()
                    self.facultybottom.pack(side=BOTTOM)
                    self.facultydata.pack(side=LEFT)
                    self.facultyRight.pack(side=RIGHT)









                else:
                    print("wrong pwd ")

            else:
                print("get the help of your HOD ")

            self.e6.delete(0,END)
            self.e7.delete(0,END)










        # self.f3.pack_forget()
        # self.f4.pack()
        pass


Student_A()
mainloop()
