from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import csv


class Student_A:
    def __init__(self):
        self.w1 = Tk()
        self.w1.title("Student INfo ")

        # Login OR Main Page
        self.login_frame = Frame(self.w1, bg="skyblue", height=300, width=250)
        self.login_frame.pack()
        self.login_frame.propagate("a" in "bcd")

# =============================== login  ( FRAME 1)

        self.l1 = Label(self.login_frame, bg="skyblue", fg="skyblue").pack()
        self.l2 = Label(self.login_frame, fg="black", bg="Skyblue", text="Login").pack()
        self.l3 = Label(self.login_frame, bg="skyblue").pack()
        self.l5 = Label(self.login_frame, fg="black", bg="Skyblue", text="Username:").pack()
        self.e1 = Entry(self.login_frame)
        self.e1.pack()
        self.l6 = Label(self.login_frame, fg="black", bg="Skyblue", text="Password:").pack()
        self.e2 = Entry(self.login_frame, show='*')
        self.e2.pack()
        self.l3 = Label(self.login_frame, bg="skyblue").pack()
        self.l3 = Label(self.login_frame, bg="skyblue").pack()  # this is for giving extra space
        # self.b1=Button(self.f,text="login").pack()
        self.b1 = Button(self.login_frame, text="Login", command=self.login)
        self.b1.place(x=105, y=198)
        self.l4 = Label(self.login_frame, text="Or ", bg="skyblue")
        self.l4.place(x=115, y=220)
        self.b2 = Button(self.login_frame, text=" Register", command=self.register)
        self.b2.place(x=10, y=240)
        self.b3 = Button(self.login_frame, text=" Admin Login ", command=self.admin_login)
        self.b3.place(x=140, y=240)

        self.warning_label=Label(self.login_frame,fg='red',bg='sky blue')
        self.warning_label.place(x=90,y=190)


#====================================Registration Frame

        self.register_frame = Frame(self.w1, bg="skyblue", height=300, width=250)
        #self.f2.pack()  #pack() this in button
        self.register_frame.propagate("a" in "bcd")
        self.l8 = Label(self.register_frame, bg="skyblue").pack()
        self.l7 = Label(self.register_frame, text="Registration", bg="skyblue").pack()
        self.l8 = Label(self.register_frame, bg="skyblue").pack()
        self.l9 = Label(self.register_frame, text=" Name : ", bg="skyblue").pack()
        self.e3 = Entry(self.register_frame)
        self.e3.pack()

        self.l10 = Label(self.register_frame, text="Password : ", bg="skyblue").pack()
        self.e5 = Entry(self.register_frame, show="*")
        self.e5.pack()
        self.b2 = Button(self.register_frame, text="Register", command=self.register_info)
        self.b2.place(x=105, y=240)
        self.l11 = Label(self.register_frame, bg="skyblue")
        self.l11.place(x=70, y=260)
#===================== Back button from registration
        self.b4=Button(self.register_frame, text="Back", command=self.back)
        self.b4.place(x=2,y=2)

#===================== Admin frame login

        self.f_login_admin = Frame(self.w1, bg="skyblue", height=300, width=250)
        self.f_login_admin.propagate("a" in "bcd")

        self.l1 = Label(self.f_login_admin, bg="skyblue", fg="skyblue").pack()
        self.l2 = Label(self.f_login_admin, fg="black", bg="Skyblue", text="Admin Login").pack()
        self.l3 = Label(self.f_login_admin, bg="skyblue").pack()
        self.l5 = Label(self.f_login_admin, fg="black", bg="Skyblue", text="Username:").pack()
        self.e6 = Entry(self.f_login_admin)
        self.e6.pack()
        self.l6 = Label(self.f_login_admin, fg="black", bg="Skyblue", text="Password:").pack()
        self.e7 = Entry(self.f_login_admin, show='*')



        self.e7.pack()
        self.l3 = Label(self.f_login_admin, bg="skyblue").pack()
        self.l3 = Label(self.f_login_admin, bg="skyblue").pack()  # this is for giving extra space
        # self.b1=Button(self.f,text="login").pack()
        self.b1 = Button(self.f_login_admin, text="Login", command=self.admin_win)
        self.b1.place(x=105, y=200)

#=========================== Inside Admin Frame
        self.f_inside_admin=Frame(self.w1,bg='cadet blue',height=450,width=1000)
        self.f_inside_admin.propagate('a'in 'bcd')
        self.frame_label=Label(self.f_inside_admin,text='User Details',bg='sky blue',font=('arial', 20, 'bold'),padx=1000,pady=10).pack()
        self.admin_bottom=Frame(self.w1,bg='skyblue',height=50,width=1000)
        self.admin_bottom.propagate('a'in 'bcd')
        self.admin_submit=Button(self.admin_bottom,text='Submit', pady=20, padx=30,command=self.combo_sele)
        self.admin_submit.place(x=400,y=0)
        self.admin_exit = Button(self.admin_bottom, text='Exit',fg='red' , pady=20, padx=30,command=self.exit)
        self.admin_exit.place(x=910,y=0)
        self.admin_exit = Button(self.f_inside_admin, text='Back', fg='red', pady=5, padx=10, command=self.back_admin)
        self.admin_exit.place(x=0, y=0)


        self.space_label=Label(self.f_inside_admin,bg='sky blue')
        self.space_label.grid(row=0,column=0)
        self.space_label = Label(self.f_inside_admin,bg='sky blue')
        self.space_label.grid(row=2, column=0)
        self.space_label=Label(self.f_inside_admin,bg='cadet blue')
        self.space_label.grid(row=3,column=2)
        self.space_label = Label(self.f_inside_admin, bg='cadet blue')
        self.space_label.grid(row=3, column=3)
        self.space_label = Label(self.f_inside_admin,bg='cadet blue')
        self.space_label.grid(row=3, column=5)
        self.space_label = Label(self.f_inside_admin,bg='cadet blue')




        self.space_label.grid(row=3, column=6)
        self.space_label = Label(self.f_inside_admin,bg='cadet blue')
        self.space_label.grid(row=3, column=7)
        self.space_label = Label(self.f_inside_admin, bg='cadet blue')
        self.space_label.grid(row=3, column=8)
        self.space_label = Label(self.f_inside_admin,bg='cadet blue')
        self.space_label.grid(row=3, column=9)
        self.space_label = Label(self.f_inside_admin, bg='cadet blue')
        self.space_label.grid(row=3, column=10)
        self.space_label = Label(self.f_inside_admin, bg='cadet blue')
        self.space_label.grid(row=3, column=11)
        self.space_label = Label(self.f_inside_admin,bg='cadet blue')
        self.space_label.grid(row=3, column=12)
        self.space_label = Label(self.f_inside_admin, bg='cadet blue')
        self.space_label.grid(row=3, column=13)






        self.userid_label=Label(self.f_inside_admin,text='UserID',bg='cadet blue',font=('times',30,'bold'))
        self.userid_label.grid(row=3,column=4)  #=========================================== all id should be in this row
        self.userrole_label = Label(self.f_inside_admin, text='Role', bg='cadet blue', font=('times', 30, 'bold'))
        self.userrole_label.grid(row=3, column=14) #=============================

        self.username_1 = Label(self.f_inside_admin, text='samir', bg='cadet blue',)
        self.username_1.grid(row=4, column=4)


        self.username_1 = Label(self.f_inside_admin, text='ketan', bg='cadet blue',)
        self.username_1.grid(row=6, column=4)


        self.username_1 = Label(self.f_inside_admin, text='rushi', bg='cadet blue', )
        self.username_1.grid(row=8, column=4)

        self.username_1 = Label(self.f_inside_admin, text='surojit', bg='cadet blue', )
        self.username_1.grid(row=10, column=4)

        self.username_1 = Label(self.f_inside_admin, text='Anuja', bg='cadet blue', )
        self.username_1.grid(row=12, column=4)

        v ='Student','Faculty'

        self.combo1 = Combobox(self.f_inside_admin, values=v)
        self.combo1.set('Select')
        self.combo1.grid(row=4,column=14)

        self.combo2 = Combobox(self.f_inside_admin, values=v)
        self.combo2.set('Select')
        self.combo2.grid(row=6,column=14)

        self.combo3 = Combobox(self.f_inside_admin, values=v)
        self.combo3.set('Select')
        self.combo3.grid(row=8,column=14)

        self.combo4 = Combobox(self.f_inside_admin, values=v)
        self.combo4.set('Select')
        self.combo4.grid(row=10,column=14)

        self.combo5 = Combobox(self.f_inside_admin, values=v)
        self.combo5.set('Select')
        self.combo5.grid(row=12,column=14)


        self.f_inside_admin.grid_propagate(0)
        #
        # with open('data.csv','r') as f:
        #     data=csv.reader(f)
        #
        #     for column in data:
        #         for n in range (0,2):
        #             n=self.id
        #             self.id=column[n]
        #             print(self.id)
        #



#========================BACK BUTTON
        self.b4 = Button(self.f_login_admin, text="Back", command=self.back)
        self.b4.place(x=2, y=2)

#========================INSIDE STUDENT FRAME
        self.f_inside_student= Frame(self.w1, height=600, width=1000)
        self.l1 = Label(self.f_inside_student, text="Students INFO", bg="sky blue", font=('arial', 20, 'bold'), padx=1000)

        self.l1.pack()

        self.f_inside_student.propagate("a" in "bcd")
        with open('sam.csv','r') as f:  # for multiple student i cannot find the way
            data=csv.reader(f)

            for row in data:
                    print(row[0],row[1])
                    self.name=row[0]
                    self.surname=row[1]
                    self.hobbi1=row[2]
                    self.hobbi2=row[3]
                    self.achiev1_updated=row[4]
                    self.achiev2_updated=row[5]



    #==================THESE LABEL FOR SPACING In INSIDE STUDENT FRAME=======
        self.l32 = Label(self.f_inside_student,bg="sky blue")
        self.l32.grid(row=1, column=0)
        self.l32 = Label(self.f_inside_student,bg="sky blue")
        self.l32.grid(row=2, column=0)
        self.l32 = Label(self.f_inside_student)
        self.l32.grid(row=3, column=0)
        self.l32 = Label(self.f_inside_student)
        self.l32.grid(row=4, column=0)


    #========================UPTO THIS IS FOR SPACING

    #============ Detils Shoawing Label
        self.detailshowinglabel=Label(self.f_inside_student)

        self.l32=Label(self.f_inside_student, text="First Name     :")
        self.l32.grid(row=5,column=0)
        self.l32 = Label(self.f_inside_student, text=self.name)
        self.l32.grid(row=5, column=1)
        # self.e32=Entry(self.f_inside_student )
        # self.e32.grid(row=5,column=1)

        self.l33=Label(self.f_inside_student, text="Last Name      :")
        self.l33.grid(row=6,column=0)
        self.l33 = Label(self.f_inside_student, text=self.surname)
        self.l33.grid(row=6, column=1)
        # self.e33=Entry(self.f_inside_student)
        # self.e33.grid(row=7,column=1)

    #=========HOBBIES and Achievements

        self.hobbies=self.hobbi1,",",self.hobbi2
        self.achievments= self.achiev1_updated, ",", self.achiev2_updated

        self.l32 = Label(self.f_inside_student, text=" Hobbies      :")
        self.l32.grid(row=7, column=0)
        self.labfotdisplayhob=Label(self.f_inside_student,text=self.hobbies)
        self.labfotdisplayhob.grid(row=7,column=1)
        self.l32 = Label(self.f_inside_student, text="Achievements :")
        self.l32.grid(row=8, column=0)
        self.labfotdisplayachiv=Label(self.f_inside_student,text=self.achievments)
        self.labfotdisplayachiv.grid(row=8,column=1)

        self.edit_button = Button(self.f_inside_student, text='Edit', command=self.edit_frame)
        self.edit_button.grid(row=11, column=2)

        self.back_buttom_edit = Button(self.f_inside_student, text='Back', command=self.back_from_inside_std)
        self.back_buttom_edit.grid(row=0,column=0)

        self.f_inside_student.grid_propagate(0)





    #=====================Confirm Data


#================= CREATE NEW FRAME FOR EDIT DETAILS



        self.f_student_edit=Frame(self.w1, height=600, width=1000)
        self.l1 = Label(self.f_student_edit, text="Edit Your Details", bg="sky blue", font=('arial', 20, 'bold'),
                        padx=1000)

        self.l1.pack()

        self.f_student_edit.propagate("a" in "bcd")
        # ========= INside Student EDit  frame

        # ============================ SPACING IN STUDENT EDIT FRAME

        self.l32 = Label(self.f_student_edit, bg="sky blue")
        self.l32.grid(row=1, column=0)
        self.l32 = Label(self.f_student_edit, bg="sky blue")
        self.l32.grid(row=2, column=0)
        self.l32 = Label(self.f_student_edit)
        self.l32.grid(row=3, column=0)
        self.l32 = Label(self.f_student_edit)
        self.l32.grid(row=4, column=0)


        #<-----------------------Spacing
#================ write here all updated details

        # self.nam_updated =self.name_edit.get()
        #
        # self.srname_updated = self.srname_edit.get()
        # self.hobbie_updated = self.hobi1 , ',', self.hobi2
        # self.achiev_updated = self.achiev1, ',', self.achiev2

        self.l32 = Label(self.f_student_edit, text="First Name     :")
        self.l32.grid(row=5, column=0)
        self.label_of_st_name = Label(self.f_student_edit, text=self.name)     # this nam is for newly edited name
        self.label_of_st_name.grid(row=5, column=1)
        self.name_edit=Entry(self.f_student_edit)
        self.name_edit.grid(row=6, column=1)
        self.bne = Button(self.f_student_edit, text=' Edit ', bg='ghost white', command=self.edit_name)
        self.bne.grid(row=6, column=2)

        self.l33 = Label(self.f_student_edit, text="Last Name      :")
        self.l33.grid(row=7, column=0)
        self.label_srname_edit = Label(self.f_student_edit, text=self.surname)  # same
        self.label_srname_edit.grid(row=7, column=1)
        self.srname_edit=Entry(self.f_student_edit)
        self.srname_edit.grid(row=8, column=1)
        self.bne = Button(self.f_student_edit, text=' Edit ', bg='ghost white', command=self.edit_surname)
        self.bne.grid(row=8, column=2)

#===== define the new hobbies


        self.l32 = Label(self.f_student_edit, text=" Hobbies      :")
        self.l32.grid(row=9, column=0)
        self.l33 = Label(self.f_student_edit, text=self.hobbies)
        self.l33.grid(row=9, column=1)

        self.eh1 = Entry(self.f_student_edit)
        self.eh1.grid(row=10, column=1)
        self.eh2 = Entry(self.f_student_edit)
        self.eh2.grid(row=10, column=2)
        self.bh = Button(self.f_student_edit, text=' Edit ', bg='ghost white', command=self.addhobbi)
        self.bh.grid(row=10, column=3)

        self.l32 = Label(self.f_student_edit, text="Achievements :")
        self.l32.grid(row=11, column=0)
        self.l33 = Label(self.f_student_edit, text=self.achievments)
        self.l33.grid(row=11, column=1)
        self.ea1 = Entry(self.f_student_edit)
        self.ea1.grid(row=12, column=1)
        self.ea2 = Entry(self.f_student_edit)
        self.ea2.grid(row=12, column=2)
        self.ba = Button(self.f_student_edit, text=' ADD ', command=self.addachiv)
        self.ba.grid(row=12, column=3)
        self.space = Button(self.f_student_edit,)
        self.space.grid(row=13, column=2)

        self.submit_button = Button(self.f_student_edit, text='Exit', padx=10,bg='red',fg='red', command=self.exit)
        self.submit_button.grid(row=14, column=3)

        self.submit_button = Button(self.f_student_edit, text='Submit', padx=15,command=self.storedatastudent)
        self.submit_button.grid(row=14, column=1)

        self.back_buttom_edit=Button(self.f_student_edit, text='Back', command=self.back_from_stu_edit)
        self.back_buttom_edit.grid(row=0,column=0)



#================= FACULTY FRAME
        self.f_inside_faculty = Frame(self.w1, bg='cadet blue', height=450, width=1000)
        self.f_inside_faculty.propagate('a' in 'bcd')
    def password_not_match(self):
        self.warning_label['text']='Password Does Not Match'

    def username_not_exists(self):
        self.warning_label['text']='Username does not exist'



    def back_admin(self):
        self.f_inside_admin.pack_forget()
        self.admin_bottom.pack_forget()
        self.f_login_admin.pack()



    def back_from_stu_edit(self):
        self.f_student_edit.pack_forget()
        self.f_inside_student.pack()

    def back_from_inside_std(self):
        self.f_inside_student.pack_forget()
        self.login_frame.pack()

    def edit_name(self):
        self.nam_updated=self.name_edit.get()

        if self.nam_updated== "":
            messagebox.showerror("Error ", "No Input ")
        else:
           self.label_of_st_name['text']=self.nam_updated

    def edit_surname(self):
        self.srname_updated=self.srname_edit.get()
        if self.srname_updated== "":
            messagebox.showerror("Error ", "No Input ")
        else:
           self.label_srname_edit['text']=self.srname_updated


    def addhobbi(self):
        self.hobbi1_updated=self.eh1.get()
        self.hobbi2_updated=self.eh2.get()
        self.hobbi_update= self.hobbi1_updated, ',', self.hobbi2_updated

        if self.hobbi1_updated == "" and self.hobbi2_updated == "":
            messagebox.showerror("Error ", "No Input ")

        else:

             self.labfotdisplayhob['text']= self.hobbi1_updated, ",", self.hobbi2_updated
        #
        # self.eh1.delete(0,END)
        # self.eh2.delete(0,END)


    def addachiv(self):
        self.achiev1_updated=self.ea1.get()
        self.achiev2_updated=self.ea2.get()
        self.achiev_update= self.achiev1_updated, ",", self.achiev2_updated
        if self.achiev1_updated== "" and self.achiev2_updated== "":
            messagebox.showerror("Error","No Input")

        else:

              self.labfotdisplayachiv['text'] = self.achiev1_updated, ",", self.achiev2_updated
        #
        #
        # self.ea1.delete(0,END)
        # self.ea2.delete(0,END)

    # to store the data from
    def storedatastudent(self):

        # if self.eh1.get()=="" or self.eh2.get()=="" or




        with open('sam.csv','w')as f:
           # f.write(self.nam_updated + "," + self.srname_updated + "," + self.hobbi_update + "," + self.achiev_update)
           f.write(self.name_edit.get()+','+self.srname_edit.get()+','+self.hobbi1_updated+','+self.hobbi2_updated+','+self.achiev1_updated+','+self.achiev2_updated+','+self.role_selected)

        self.confirm_successful=Label(self.f_student_edit,text="Details Successfully Edited ",fg='red')
        self.confirm_successful.pack()

        messagebox.askyesno("Confirm","Do yuo real want to save ")

        self.f_inside_student.grid_propagate(0)





#=======================  iNisde Admin Frame

        self.f_inside_admin = Frame(self.w1, width=1000, height=750)
        self.l1 = Label(self.f_inside_admin, text="USERs INFO", bg="sky blue", font=('arial', 35, 'bold'), padx=1000)

        self.l1.pack()
        self.f_inside_admin.propagate("a" in "bcd")



    def login(self):
        if self.e1.get() == "" or self.e2.get() == "":
            messagebox.showerror("Error", "All fields are required !")
        else:
            print("working...")
            # first delete the username and password from frame f1
            name=self.e1.get()
            pwd=self.e2.get()
            with open("data.csv", 'r') as f:
                data =csv.reader(f)
                #print(data)
                for row in data:



                        if row[0]==name:
                            if row[2]==pwd:
                                self.l12=Label(self.login_frame, text="")
                                print("Login Successful")
                                self.login_frame.pack_forget()



                                if row[3]==0:
                                    self.f_inside_student.pack()
                                else:
                                    self.f_inside_faculty.pack()


                            else:
                                self.l12=Label(self.login_frame, text="PWD does not match", bg="sky blue", fg="red")
                                self.l12.pack()
                                self.password_not_match()

                                print("PWD does not match")
                                break
                        else:
                            self.username_not_exists()
                            print("username doesnot exist")

            self.e1.delete(0, END)
            self.e2.delete(0, END)



    def register(self):

        self.login_frame.pack_forget()
        self.register_frame.pack()


    def register_info(self):
        if self.e3.get() =="" or self.e5.get() =="":
            messagebox.showerror("Error", "All fields are required !")
        else:
            self.l11["text"]="Successful"                      #
            with open("data.csv", 'a')as f:
                f.write(self.e3.get()+","+self.e5.get()+"\n")
                #f.write (f"{self.e3.get(),self.e4.get(),self.e5.get()}\n") this is wrong method it will create Tuple
            student_name=self.e3.get()
            with open(student_name.csv,'w')as f:        # how we can create file like this
                f.write(self.e3.get()+","+self.e5.get())
                pass


            self.e3.delete(0, END)
            self.e5.delete(0, END)
    def back(self):
        self.register_frame.forget()
        self.f_login_admin.forget()
        self.login_frame.pack()


    def admin_login(self):
        self.login_frame.pack_forget()
        self.f_login_admin.pack()


    def admin_win(self):
        if self.e6.get() =="" or self.e7.get()=="":
            messagebox.showerror("Error","All fields are required !")
        else:
            admin_name=self.e6.get()
            admin_pwd=self.e7.get()
            if admin_name=="a":
                if admin_pwd=="a":
                    print("Successful")
                    self.f_login_admin.pack_forget()
                    self.f_inside_admin.pack()
                    self.admin_bottom.pack(side=BOTTOM)


                else:
                    print("wrong pwd ")
                    self.l = Label(self.f_login_admin, text=" Wrong Password ", bg="sky blue", fg="red")
                    self.l.place(x=90, y=230)

            else:
                print("get the help of your HOD ")
                self.l=Label(self.f_login_admin, text=" Username Does not exits ",bg="sky blue",fg="red")
                self.l.place(x=90,y=230)

            self.e6.delete(0,END)
            self.e7.delete(0,END)



    def edit_frame(self):
        self.f_inside_student.pack_forget()
        self.f_student_edit.pack()


    def combo_sele(self):
        self.student_role='student'
        self.faculty_role='faculty'
        lst = []
        user_role_1 = self.combo1.get()
        user_role_2 = self.combo2.get()
        user_role_3 = self.combo3.get()
        user_role_4 = self.combo4.get()
        user_role_5 = self.combo5.get()

        lst.append(user_role_1)
        lst.append(user_role_2)
        lst.append(user_role_3)
        lst.append(user_role_4)
        lst.append(user_role_5)



        for item in lst :
            print(item)
            if item=="":
                messagebox.showerror('Error','Plz fill All The Roles of student ')

            else:
                if item==self.student_role:
                    self.role_selected=0

                else:
                    self.role_selected=1    #now this in





    def exit(self):
        messagebox.askyesno("Student Data Management System ", "Confirm if you want exit")
        self.w1.destroy()




        # self.f4.pack()
        pass


Student_A()
mainloop()
