import serial 
from tkinter import * 
from tkinter import messagebox
import tkinter.ttk as tk
import time
import sqlite3
import random
import subprocess
import shlex



s = serial.Serial('COM3',9600)
global MAX_NUMBER
MAX_NUMBER = 10
global auto
auto = True
global temp
temp = 18
global lst
lst = [False,False,False,False,False,False,False,False]
global fans
fans=FALSE

class Application_Interface:
    logged=False
    opened=True
    def run(self):
        self.window = Tk()

        def disable_event():
            self.opened = False
        
        self.window.protocol("WM_DELETE_WINDOW", disable_event)
        self.window.resizable(False,False)
        self.window.geometry("800x650+250+50")
        # self.window.iconbitmap("icons\lamp.ico")
        self.window.title("Login")
        txt ="Welcome, you'll see that saving power will be easier than before!" 
        self.welcome = Label(self.window,font=("Arial",15,"italic"),fg="Green")
        #self.quit = Button(self.window,text="Exit",command=self.des,width=8,font=("Arial 10 bold") ,bd=3,bg="#AA0121",fg='white',activebackground='#AA0121')
        self.usernameEntry = Entry(self.window, width=22,font=("bold",15))  
        self.passwordEntry = Entry(self.window, width=22,font=("bold",15),show="*")
        self.usernameLabel = Label(self.window, text="Username",font=('Sitka Small', 15, 'bold'))
        self.passwordLabel = Label(self.window, text="Password",font=('Sitka Small', 15, 'bold'))
        self.userlogin=Button(self.window,text="Login as User",command=self.login,padx=20, pady=5, fg="white",bg="#B33030", font=('calibre', 10, 'bold'),activebackground="#B33030",activeforeground="white")
        self.message_label =  Label(self.window, text="",font=("Arial",10,"bold"),fg="red")
        self.logo_image = PhotoImage(file="icons/LightMode1.png")
        self.logo = Label(image=self.logo_image)
        self.adminlogin=Button(self.window,text="Login as Admin",padx=20, pady=5, fg="white",bg="#B33030", font=('calibre', 10, 'bold'),command=self.check_admin,activebackground="#B33030",activeforeground="white")

        #self.quit.place(x=78,y=0)
        self.userlogin.place(x=510, y=580)
        self.adminlogin.place(x= 170, y=580)
        self.logo.place(x=290,y=-20)
        self.message_label.place(x=280,y=520)
        self.usernameEntry.place(x=370,y=335,height=28)
        self.passwordEntry.place(x=370,y=435,height=28)  
        self.usernameLabel.place(x=200,y=330)
        self.passwordLabel.place(x=200,y=430)

        self.con = sqlite3.connect("Database.db")
        self.cr = self.con.cursor()
        self.cr.execute(""" CREATE TABLE IF NOT EXISTS users (ID INTEGER PRIMARY KEY AUTOINCREMENT, username VARCHAR(30), password VARCHAR(30)) """)
        self.con.commit() 
        self.printString(txt)
        self.window.mainloop()

    def des(self):

            self.opened=False


    def printString(self, string):
        for char in string:
            self.welcome.configure(text=self.welcome.cget('text') + char)
            self.welcome.update()
            self.welcome.place(x=100,y=230)
            time.sleep(.07)

    def register(self):
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()

        if username and password:
            try:
                self.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
                self.conn.commit()
                self.message_label.config(text="Registration successful")
            except:
                self.message_label.config(text="Username already exists")
        else:
            self.message_label.config(text="Please enter a valid username and password")

    def login(self):
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()

        if username and password:
            self.cr.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
            user = self.cr.fetchone()

            if user:
                self.window.withdraw()
                self.logged = True
                self.User_Interface()

            else:
                messagebox.showerror("Failed","Please enter a valid username and password")
        else:
            messagebox.showerror("Failed","Please enter a valid username and password")
    

    def check_admin(self):
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()

        if username=="admin" and password=="admin":
            self.window.withdraw()
            self.Admin_Page()      
        else:
            messagebox.showerror("Failed","Please enter a valid username and password")

    

    def Options_page(self):
    
        root = Toplevel()


        def disable_event(): # close window
            self.opened = False


        def back(): # back button
            root.destroy()
            self.Admin_Page()


        def insert_user(): #add user
            name=namee.get()
            username = usere.get()
            password = passe.get()
            if name and username and password:
                self.cr.execute("SELECT * FROM users WHERE username=?", (username,))
                user = self.cr.fetchone()
                if not user:
                    con = sqlite3.connect("Database.db")
                    cur = con.cursor()
                    cur.execute("INSERT INTO users (username,password,name) VALUES (?,?,?)",(username,password,name))
                    con.commit()
                    message_label.config(text="User inserted succesfully!",fg="green")
                    

                else:
                    message_label.config(text="User already exists!",fg="red")
                message_label.place(x=360,y=440)   
            else:
                message_label.config(text="Please enter a valid username and password",fg="red")
                message_label.place(x=300,y=440)


        def delete_user(): # delete user
            username = delete.get()
            if username:
                self.cr.execute("SELECT * FROM users WHERE username=?", (username,))
                user = self.cr.fetchone()
                if user:
                    con = sqlite3.connect("Database.db")
                    cur = con.cursor()
                    cur.execute("DELETE FROM users WHERE username=?",(username,))
                    con.commit()
                    message_label.config(text="User deleted succesfully!",fg="green")
                else:
                    message_label.config(text="User doesn't exist!",fg="red")
                message_label.place(x=360,y=600)

            else:
                message_label.config(text="Please enter a valid username and password",fg="red")
                message_label.place(x=300,y=600)


        root.protocol("WM_DELETE_WINDOW", disable_event)
        root.title("Smart Classroom")
        root.geometry("800x650+250+50")
        root.resizable(False,False)
        root.iconbitmap("icons\lamp.ico")

        logo_image = PhotoImage(file="icons\LightMode1.png")
        l = Label(root,image=logo_image) 

        back_button=Button(root,text="Back",width=15, padx=7, command=back,pady=5, bg="#B33030", fg="white", font=('calibre', 10, 'bold'))

        line2 = Label(root,fg="black",text="___________________________________________________________________________________________________________________________________________________________________",font=("Arial",20))
        insert=Label(root,text="Add User",font=('Sitka Small', 15, 'bold'))
        name=Label(root,text="Full Name",font=("Arial",15))
        user=Label(root,text="Username",font=("Arial",15))
        password=Label(root,text="Password",font=("Arial",15))
        usere= Entry(root, width=22,font=("bold",15))
        passe= Entry(root, width=22,font=("bold",15),show='*')
        namee= Entry(root, width=22,font=("bold",15))
        line = Label(root,fg="black",text="___________________________________________________________________________________________________________________________________________________________________",font=("Arial",20))
        insert_button=Button(root,text="Add",width=15, padx=7, command=insert_user,pady=5, bg="#B33030", fg="white", font=('calibre', 10, 'bold'))
        
        back_button.place(x=50,y=50)
        line2.place(x=0,y=185)
        l.place(x=280,y=-35)
        insert.place(x=350,y=200)
        name.place(x=200,y=280)
        user.place(x=200,y=340)
        password.place(x=200,y=400)
        namee.place(x=330,y=280,height=28)
        usere.place(x=330,y=340,height=28)
        passe.place(x=330,y=400,height=28)
        insert_button.place(x=600,y=340)
        line.place(x=0,y=450)

        
        
        delete= Entry(root, width=22,font=("bold",15))
        Delete_user=Label(root,text="Delete User",font=('Sitka Small', 15, 'bold'))
        user_delete_label=Label(root,text="Username",font=("Arial",15))
        Delete_button=Button(root,text="Delete",width=15, padx=7,command=delete_user, pady=5, bg="#B33030", fg="white", font=('calibre', 10, 'bold'))
        
        Delete_user.place(x=340,y=465,height=28)
        user_delete_label.place(x=200,y=550)
        delete.place(x=330,y=550)  
        Delete_button.place(x=600,y=550)

        message_label =  Label(root, text="",font=("Arial",10,"bold"),fg="red")
        message_label.place(x=360,y=380)


        mainloop()




        




    def Table(self):
    
        root = Toplevel()


        def disable_event(): # close window
            self.opened = False


        def back(): # back button
            root.destroy()
            self.Admin_Page()


        root.protocol("WM_DELETE_WINDOW", disable_event)
        root.title("Smart Classroom")
        root.geometry("800x650+250+50")
        root.resizable(False,False)
        root.iconbitmap("icons\lamp.ico")




        def create_task(start_time,day,end_time=None):
            task_name = random.randint(1,1000000)
            exe_path = r"E:\mohamed\FCI\last term\finished\network\NP Task\Client\Client\bin\Debug\Client.exe"
            quoted_exe_path = shlex.quote(exe_path)

            command = f'schtasks /create /tn "{task_name}" /tr "{quoted_exe_path}" /sc weekly /st 17:21 /d {day} /f'

            if end_time is not None:
                command += f' /et {end_time}'
            print(command)
            # result = subprocess.run(command, shell=True, capture_output=True, text=True)
            # if result.returncode == 0:
            #     print(f"Task '{task_name}' created successfully!")
            # else:
            #     print("Failed to create the task.")
            #     print(result.stderr)

            # Example usage
            
            # create_task(task_name, exe_path, start_time,end_time)


        
        def update_users(): # Update Users in combo box 
            self.cr.execute("SELECT name FROM users")
            result = self.cr.fetchall()
            lst = []
            for i in result:
                lst.append(i[0])
            return lst

            
        def data(name):
            x = (int(name[0])*5+int(name[1]))
            if bool[x] == 0:    
                root2 = Toplevel()
                root2.protocol("WM_DELETE_WINDOW", lambda:root2.destroy())
                root2.title("Smart Classroom")
                root2.geometry("400x400+250+50")
                root2.resizable(False,False)
                root2.iconbitmap("icons\lamp.ico")
                value = StringVar()
                combo = tk.Combobox(root2,value=update_users(),state='readonly',textvariable=value,font=('calibre', 10, 'bold'))
                combo.pack()
                confirm=Button(root2,text="Confirm",width=15, padx=7, command=lambda x=name:add_delete(x,str(combo.get()),root2), pady=5, activebackground="#B33030", activeforeground="white" ,bg="#B33030", fg="white", font=('calibre', 10, 'bold'))
                confirm.pack()
                # combo.bind("<<ComboboxSelected>>",show_data)      
            else:
                add_delete(name)

        back_button=Button(root,text="Back",width=15, padx=7, command=back,pady=5, activebackground="#B33030", activeforeground="white" ,bg="#B33030", fg="white", font=('calibre', 10, 'bold'))
        back_button.place(x=50,y=50)
        studentLabel=Label(root,text="Study Table",font=("calibre",25,"bold"),fg="#2AAAFF")
        studentLabel.place(x=320,y=50)

        sat = Label(root,text="Sat",font=("Arial",15))
        sun = Label(root,text="Sun",font=("Arial",15))
        mon = Label(root,text="Mon",font=("Arial",15))
        tue = Label(root,text="Tue",font=("Arial",15))
        wen = Label(root,text="Wed",font=("Arial",15))
        thu = Label(root,text="Thu",font=("Arial",15))
        fri = Label(root,text="Fri",font=("Arial",15))

        
        sat.place(x=100,y=200)
        sun.place(x=100,y=260)
        mon.place(x=100,y=320)
        tue.place(x=100,y=380)
        wen.place(x=100,y=440)
        thu.place(x=100,y=500)
        fri.place(x=100,y=560)
        
        
        f8t10 =Label(root,text="8-10",font=("calibre",15))
        f10t12 =Label(root,text="10-12",font=("calibre",15))
        f12t2 =Label(root,text="12-2",font=("calibre",15))
        f2t4 =Label(root,text="2-4",font=("calibre",15))
        f4t6 =Label(root,text="4-6",font=("calibre",15))
        
        f8t10.place(x=200,y=150)
        f10t12.place(x=300,y=150)
        f12t2.place(x=400,y=150)
        f2t4.place(x=500,y=150)
        f4t6.place(x=600,y=150)

        days = ["SAT", "SUN","MON", "TUE", "WED", "THU", "FRI" ]
        fr=["08:00","10:00","12:00","02:00","04:00"]
        to=["10:00","12:00","02:00","04:00","06:00"]
        buttons = {}
        bool = [0 for _ in range(35)]
        self.cr.execute("SELECT * FROM Students_table")
        result = self.cr.fetchall()
        for i in result:
                x = (int(i[0][0])*5+int(i[0][1]))
                bool[x] = 1
        # create 35 buttons and store them in the dictionary with unique variable names
        for i in range(7):
            for j in range(5):
                button_name = f"{i}{j}"
                if bool[i*5+j] == 1:       #command=lambda x=button_name:add_delete(x)
                    buttons[button_name] = Button(root, text=f"Button {i} {j}",width=13, height=2,bg="#00DD00", command=lambda x=button_name:data(x), activebackground="#00DD00")
                else:
                    buttons[button_name] = Button(root, text=f"Button {i} {j}",width=13, height=2,bg="#BB0000",command=lambda x=button_name:data(x),activebackground="#BB0000")
                buttons[button_name].place(x=j*100+180,y=i*60+200)
        
        def add_delete(name, Doctor="Empty", root2=None):
            if root2 != None:
                root2.destroy()
            con = sqlite3.connect("Database.db")
            cur = con.cursor()
            x = (int(name[0])*5+int(name[1]))
            
            if bool[x] == 0:
                cur.execute("INSERT INTO Students_table VALUES (?,?)",(name,1235,))
                con.commit()
                bool[x] = 1
                buttons[name].config(bg="#00DD00",activebackground="#00DD00",text=Doctor)
                day=days[int(name[0])]
                start_time=fr[int(name[1])]
                end_time=to[int(name[1])]
                create_task(start_time,day)

            else:
                cur.execute("DELETE FROM Students_table WHERE Name=?",(name,))
                con.commit()
                bool[x] = 0
                buttons[name].config(bg="#BB0000",activebackground="#BB0000",text=Doctor)

    def Admin_Page(self):

      
        def call_page(): # More Options
            root.withdraw()
            self.Options_page()
        
        def modify_table(): # More Options
            root.withdraw()
            self.Table()
    


        def disable_event(): # Close window
            self.opened = False
      

        root = Toplevel()
        root.protocol("WM_DELETE_WINDOW", disable_event)
        root.title("Smart Classroom")
        root.geometry("800x650+250+50")
        root.resizable(False,False)
        root.iconbitmap("icons\lamp.ico")
        

        def show_data(event): # Show users data
            self.cr.execute("SELECT username,password,name FROM users WHERE name = ? ",(str(combo.get()),))
            result = self.cr.fetchall()
            namee.config(state="normal")
            namee.delete(0,END)
            namee.insert(0,result[0][2])
            namee.config(state=DISABLED)
            usere.config(state="normal")
            usere.delete(0,END)
            usere.insert(0,result[0][0])
            usere.config(state=DISABLED)
            passe.config(state="normal")
            passe.delete(0,END)
            passe.insert(0,result[0][1])
            passe.config(state=DISABLED)
        

        def update_users(): # Update Users in combo box 
            self.cr.execute("SELECT name FROM users")
            result = self.cr.fetchall()
            lst = []
            for i in result:
                lst.append(i[0])
            return lst
            
         
        logo_image = PhotoImage(file="icons\LightMode1.png")
        l = Label(root,image=logo_image)   
        show=Label(root,text="Show User",font=('Sitka Small', 15, 'bold'))
        name=Label(root,text="Full Name",font=("Arial",15))
        user=Label(root,text="Username",font=("Arial",15))
        password=Label(root,text="Password",font=("Arial",15))
        usere= Entry(root, width=22,font=("bold",15),state=DISABLED)
        passe= Entry(root, width=22,font=("bold",15),state=DISABLED)
        namee= Entry(root, width=22,font=("bold",15),state=DISABLED)
        line = Label(root,fg="black",text="___________________________________________________________________________________________________________________________________________________________________",font=("Arial",20))
        More_option=Button(root,text="More options",width=20, padx=7, command=call_page,pady=5, bg="#B33030", fg="white", font=('calibre', 12, 'bold'))
        table=Button(root,text="Modify study schedule",width=20, padx=7, command=modify_table,pady=5, bg="#B33030", fg="white", font=('calibre', 12, 'bold'))

        value = StringVar()
        combo = tk.Combobox(root,value=update_users(),state='readonly',textvariable=value,font=('calibre', 10, 'bold'))
        combo.bind("<<ComboboxSelected>>",show_data)      
        
        l.place(x=280,y=-35)
        show.place(x=330,y=200)
        combo.place(x=330,y=240,height=28)
        name.place(x=200,y=280)
        user.place(x=200,y=340)
        password.place(x=200,y=400)
        namee.place(x=330,y=280,height=28)
        usere.place(x=330,y=340,height=28)
        passe.place(x=330,y=400,height=28)
        line.place(x=0,y=450)
        More_option.place(x=100,y=580)
        table.place(x=450,y=580)
        mainloop()


    def User_Interface(self): # User Interface
        

        def disable_event(): # Close Window
            self.opened = False
        
        global lst
        global darkMood
        darkMood = False
        style = tk.Style()
        root = Toplevel()
        root.protocol("WM_DELETE_WINDOW", disable_event)
        style.configure("BW.TRadiobutton",font=("Arial",17))
        root.title("Smart Classroom")
        root.geometry("1400x800+250+50")
        root.resizable(False,False)
        root.iconbitmap("icons/lamp.ico")  
        root.attributes('-fullscreen', True)
  
        r = IntVar()
        

        def on(num): # On/Off Buttons
            
            global MAX_NUMBER
            global auto
            global lst
            global fans

            if auto:
                ton1.config(command=None)
                ton2.config(command=None)
                ton3.config(command=None)
                ton4.config(command=None) 
                ton5.config(command=None)
                ton6.config(command=None) 
                ton7.config(command=None)
                ton8.config(command=None)  
                
            elif num == 0:
                if lst[num]:
                    ton1.config(image=on_image)
                    lst[num] = False
                    fe = 'a'
                    s.write(fe.encode('utf-8'))
                else:
                    ton1.config(image=off_image)
                    lst[num] = True
                    fe = 'b'
                    s.write(fe.encode('utf-8'))

            elif num == 1:
                if lst[num]:
                    ton2.config(image=on_image)
                    lst[num] = False
                    fe = 'c'
                    s.write(fe.encode('utf-8'))
                else:
                    ton2.config(image=off_image)
                    lst[num] = True
                    fe = 'd'
                    s.write(fe.encode('utf-8'))
            elif num == 2:
                if lst[num]:
                    ton3.config(image=on_image)
                    lst[num] = False
                    fe = 'e'
                    s.write(fe.encode('utf-8'))
                else:
                    ton3.config(image=off_image)
                    lst[num] = True
                    fe = 'f'
                    s.write(fe.encode('utf-8'))
            elif num == 3:
                if lst[num]:
                    ton4.config(image=on_image)
                    lst[num] = False
                    fe = 'g'
                    s.write(fe.encode('utf-8'))
                else:
                    ton4.config(image=off_image)
                    lst[num] = True
                    fe = 'h'
                    s.write(fe.encode('utf-8'))
            elif num == 4:
                if lst[num]:
                    ton5.config(image=on_image)
                    lst[num] = False
                    fe = 'i'
                    s.write(fe.encode('utf-8'))
                else:
                    ton5.config(image=off_image)
                    lst[num] = True
                    fe = 'j'
                    s.write(fe.encode('utf-8'))
            elif num == 5:
                if lst[num]:
                    ton6.config(image=on_image)
                    lst[num] = False
                    fe = 'k'
                    s.write(fe.encode('utf-8'))
                else:
                    ton6.config(image=off_image)
                    lst[num] = True
                    fe = 'l'
                    s.write(fe.encode('utf-8'))
            elif num == 6:
                if lst[num]:
                    ton7.config(image=on_image)
                    lst[num] = False
                    fe = 'm'
                    s.write(fe.encode('utf-8'))
                else:
                    ton7.config(image=off_image)
                    lst[num] = True
                    fe = 'n'
                    s.write(fe.encode('utf-8'))
            elif num == 7:
                if lst[num]:
                    ton8.config(image=on_image)
                    lst[num] = False
                    fe = 'o'
                    s.write(fe.encode('utf-8'))
                else:
                    ton8.config(image=off_image)
                    lst[num] = True
                    fe = 'p'
                    s.write(fe.encode('utf-8'))
            if num == 8:
                if auto:
                    if fans:
                        te.config(image=off_image)
                        fans = False
                        
                    else:
                        te.config(image=on_image)
                        fans = True
                        

                    

        r.set("1")


        def dark(): # Dark Mood
            global darkMood

            if not darkMood:
                darkMood = True
                dark_mood.config(text="Light Mood",bg='black',fg='#F0F0F0')                
                root.configure(bg="#111111")
                style.configure("TRadiobutton",font=("Arial",17),background="#111111",foreground="white")
                l.config(bg="#111111",image=dark_logo)
                configs.config(bg="#111111",fg="#4E31AA")
                line.config(bg="#111111",fg="white")
                number.config(bg="#111111",fg="#E94560")
                students.config(bg="#111111",fg="white")
                increase.config(bg="#111111",activebackground="#111111")
                decrease.config(bg="#111111",activebackground="#111111")
                modes.config(bg="#111111",fg="#E94560")
                #autos.config(bg="#111111")
                #manual.config(bg="#111111")
                devices.config(bg="#111111",fg="#4E31AA")
                led1.config(bg="#111111",fg="#E94560")
                fan1.config(bg="#111111",fg="#E94560")
                ton1.config(bg="#111111",activebackground="#111111")
                ton2.config(bg="#111111",activebackground="#111111")
                temp_label.config(bg="#111111",activebackground="#111111",fg="#E94560") 
                # tempe.config(bg="#111111",activebackground="#111111",fg="white")
                te.config(bg="#111111",activebackground="#111111")
                # decrease_temp.config(bg="#111111",activebackground="#111111")
                section1.config(bg="#111111",activebackground="#111111",fg="#E94560")
                section2.config(bg="#111111",activebackground="#111111",fg="#E94560")
                section3.config(bg="#111111",activebackground="#111111",fg="#E94560")
                section4.config(bg="#111111",activebackground="#111111",fg="#E94560")
                ton3.config(bg="#111111",activebackground="#111111")
                ton4.config(bg="#111111",activebackground="#111111")
                ton5.config(bg="#111111",activebackground="#111111")
                ton6.config(bg="#111111",activebackground="#111111")
                ton7.config(bg="#111111",activebackground="#111111")
                ton8.config(bg="#111111",activebackground="#111111")
                led2.config(bg="#111111",fg="#E94560")
                fan2.config(bg="#111111",fg="#E94560")
                led3.config(bg="#111111",fg="#E94560")
                fan3.config(bg="#111111",fg="#E94560")
                led4.config(bg="#111111",fg="#E94560")
                fan4.config(bg="#111111",fg="#E94560")


            else:
                darkMood = False
                dark_mood.config(text="Dark Mood",bg='black',fg='#F0F0F0')
                root.configure(bg="#F0F0F0")
                style.configure("TRadiobutton",font=("Arial",17),background="#F0F0F0",foreground="black")
                l.config(bg="#F0F0F0",image=logo_image)
                configs.config(bg="#F0F0F0",fg="#AA0121")
                line.config(bg="#F0F0F0",fg="black")
                number.config(bg="#F0F0F0",fg="#134982")
                students.config(bg="#F0F0F0",fg="black")
                increase.config(bg="#F0F0F0",activebackground="#F0F0F0")
                decrease.config(bg="#F0F0F0",activebackground="#F0F0F0")
                modes.config(bg="#F0F0F0",fg="#134982")
                devices.config(bg="#F0F0F0",fg="#AA0121")
                led1.config(bg="#F0F0F0",fg="#134982")
                fan1.config(bg="#F0F0F0",fg="#134982")
                ton1.config(bg="#F0F0F0",activebackground="#F0F0F0")
                ton2.config(bg="#F0F0F0",activebackground="#F0F0F0")
                temp_label.config(bg="#F0F0F0",fg="#AA0121") 
                # tempe.config(bg="#F0F0F0",fg="black")
                te.config(bg="#F0F0F0",activebackground="#F0F0F0")
                # decrease_temp.config(bg="#F0F0F0",activebackground="#F0F0F0")
                section1.config(bg="#F0F0F0",fg="#AA0121")
                section2.config(bg="#F0F0F0",fg="#AA0121")
                section3.config(bg="#F0F0F0",fg="#AA0121")
                section4.config(bg="#F0F0F0",fg="#AA0121")
                ton3.config(bg="#F0F0F0",activebackground="#F0F0F0")
                ton4.config(bg="#F0F0F0",activebackground="#F0F0F0")
                ton5.config(bg="#F0F0F0",activebackground="#F0F0F0")
                ton6.config(bg="#F0F0F0",activebackground="#F0F0F0")
                ton7.config(bg="#F0F0F0",activebackground="#F0F0F0")
                ton8.config(bg="#F0F0F0",activebackground="#F0F0F0")
                led2.config(bg="#F0F0F0",fg="#134982")
                fan2.config(bg="#F0F0F0",fg="#134982")
                led3.config(bg="#F0F0F0",fg="#134982")
                fan3.config(bg="#F0F0F0",fg="#134982")
                led4.config(bg="#F0F0F0",fg="#134982")
                fan4.config(bg="#F0F0F0",fg="#134982")

            
        def mode(value): # Mode Radio Button
            global auto 
            if value == 1:
                auto = True
                getMode()
                        
            elif value == 2:  
                auto = False
                getMode()
                ton1.config(state=ACTIVE,command=lambda:on(0))
                ton2.config(state=ACTIVE,command=lambda:on(1))
                ton3.config(state=ACTIVE,command=lambda:on(2))
                ton4.config(state=ACTIVE,command=lambda:on(3))
                ton5.config(state=ACTIVE,command=lambda:on(4))
                ton6.config(state=ACTIVE,command=lambda:on(5))
                ton7.config(state=ACTIVE,command=lambda:on(6))
                ton8.config(state=ACTIVE,command=lambda:on(7))
                

        def adjustNumber(value): # Plus and Minus sign buttons
            global MAX_NUMBER
            if value == 1:
                MAX_NUMBER += 1
                students.config(text=MAX_NUMBER)
            else:
                if not (MAX_NUMBER <= 1):
                    MAX_NUMBER -= 1
                    students.config(text=MAX_NUMBER)


        # def adjustTemp(value): # Plus and Minus sign buttons
        #         global temp
        #         if value == 1:
        #             temp += 1
        #             tempe.config(text=temp)
        #         else:
        #             if not (temp <= 1):
        #                 temp -= 1
        #                 tempe.config(text=temp)
                


        plus_image = PhotoImage(file="icons/plus.png")
        minus_image = PhotoImage(file="icons/minus.png")
        on_image = PhotoImage(file="icons/on.png")
        off_image = PhotoImage(file="icons/off.png")
        logo_image = PhotoImage(file="icons/LightMode1.png")
        dark_logo = PhotoImage(file="icons/DarkMode1.png")
        quit = Button(root,text="Exit",command=self.des,width=8,font=("Arial 10 bold") ,bd=3,bg="#AA0121",fg='white',activebackground='#AA0121')
        l = Label(root,image=logo_image)   
        configs =Label(root,text="Configurations",fg="#AA0121",font=("Arial",30,"italic","underline"),padx=5)
        line = Label(root,fg="#134982",text="___________________________________________________________________________________________________________________________________________________________________",font=("Arial",20))
        number = Label(root,text=f"Students per section", font=("Arial",20,"bold"),fg="#134982")
        students = Label(root,text=MAX_NUMBER,font=("Arial",20),fg="black")
        increase = Button(root,text="+",font=("Arial",15),command=lambda:adjustNumber(1),bd=0,image=plus_image)
        decrease = Button(root,text="-",font=("Arial",15),padx=3,command=lambda:adjustNumber(2),image=minus_image,bd=0)   
        
        temp_label = Label(root,text=f"Fans", font=("Arial",20,"bold"),fg="#134982")
        # tempe = Label(root,text=temp,font=("Arial",20),fg="black")
        # increase_temp = Button(root,text="+",font=("Arial",15),command=lambda:adjustTemp(1),bd=0,image=plus_image)
        # decrease_temp = Button(root,text="-",font=("Arial",15),padx=3,command=lambda:adjustTemp(2),image=minus_image,bd=0) 

        #temp_label = Label(root,text=f"Temperature", font=("Arial",20,"bold"),fg="#134982")
        te = Button(root,image=off_image,command=lambda:on(8),bd=0,padx=20) 

             
        dark_mood = Button(root,text="Dark Mode",command=dark,width=8,font=("Arial 10 bold") ,bd=3,bg="black",fg='White',activeforeground='white',activebackground='black')
        modes = Label(root,text="Modes",font=("Arial",20,"bold"),fg="#134982")
        autos = tk.Radiobutton(root,text="Auto",variable=r,value=1,command=lambda:mode(r.get()),style="BW.TRadiobutton")
        manual = tk.Radiobutton(root,text="Manual",variable=r,value=2,command=lambda:mode(r.get()),style="BW.TRadiobutton")
        devices =Label(root,text="Device Control",fg="#AA0121",font=("Arial",30,"italic","underline"),padx=5)

        section1 = Label(root,text="Section 1", font=("Arial",20,"bold"),fg="#134982") 
        led1 = Label(root,text="LED", font=("Arial",20,"bold"),fg="#134982")
        fan1 = Label(root,text="Fan",font=("Arial",20,"bold"),fg="#134982")
        ton1 = Button(root,image=on_image,command=lambda:on(0),bd=0,padx=20)
        ton2 = Button(root,image=on_image,command=lambda:on(1),bd=0)
        
        section2 = Label(root,text="Section 2", font=("Arial",20,"bold"),fg="#134982")
        led2 = Label(root,text="LED", font=("Arial",20,"bold"),fg="#134982")
        fan2 = Label(root,text="Fan",font=("Arial",20,"bold"),fg="#134982")
        ton3 = Button(root,image=on_image,command=lambda:on(2),bd=0,padx=20)
        ton4 = Button(root,image=on_image,command=lambda:on(3),bd=0)

        section3 = Label(root,text="Section 3", font=("Arial",20,"bold"),fg="#134982")
        led3 = Label(root,text="LED", font=("Arial",20,"bold"),fg="#134982")
        fan3 = Label(root,text="Fan",font=("Arial",20,"bold"),fg="#134982")
        ton5 = Button(root,image=on_image,command=lambda:on(4),bd=0,padx=20)
        ton6 = Button(root,image=on_image,command=lambda:on(5),bd=0)

        section4 = Label(root,text="Section 4", font=("Arial",20,"bold"),fg="#134982")
        led4 = Label(root,text="LED", font=("Arial",20,"bold"),fg="#134982")
        fan4 = Label(root,text="Fan",font=("Arial",20,"bold"),fg="#134982")
        ton7 = Button(root,image=on_image,command=lambda:on(6),bd=0,padx=20)
        ton8 = Button(root,image=on_image,command=lambda:on(7),bd=0)

        temp_label.place(x=1155,y=270)
        te.place(x=1150,y=300)
        # tempe.place(x=1160,y=320)
        # decrease_temp.place(x=1100,y=320)
        # increase_temp.place(x=1220,y=320)
        quit.place(x=78,y=0)

        l.place(x=650,y=-35)
        dark_mood.place(x=0,y=0)
        configs.place(x=640,y=180)
        number.place(x=200,y=270)
        increase.place(x=370,y=320)
        students.place(x=320,y=320)
        decrease.place(x=250,y=320)
        modes.place(x=720,y=270)
        autos.place(x=670,y=320)
        manual.place(x=780,y=320)
        line.place(x=0,y=350)
        devices.place(x=630,y=400)
        
        section1.place(x=260,y=450)
        led1.place(x=130,y=530)
        ton1.place(x=220,y=510)
        fan1.place(x=400,y=530)
        ton2.place(x=480,y=510)
        
        section2.place(x=1060,y=450)
        led2.place(x=930,y=530)
        ton3.place(x=1020,y=510)
        fan2.place(x=1200,y=530)    
        ton4.place(x=1280,y=510)
        
        section3.place(x=260,y=650)
        led3.place(x=130,y=730)
        ton5.place(x=220,y=710)
        fan3.place(x=400,y=730)
        ton6.place(x=480,y=710)
        
        section4.place(x=1060,y=650)
        led4.place(x=930,y=730)
        ton7.place(x=1020,y=710)
        fan4.place(x=1200,y=730)
        ton8.place(x=1280,y=710)
        

        mode(1)
        mainloop()

    


def getMode(): # Update Mode
    return auto

def getMax(): # Update Number of students
    return MAX_NUMBER

def getTemp():
    return temp
def getfan():
    return fans

app = Application_Interface()
# app.run()