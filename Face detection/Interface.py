import serial 
from tkinter import * 
from tkinter import messagebox
import tkinter.ttk as tk
import time
import sqlite3

s = serial.Serial('COM3',9600)
global MAX_NUMBER
MAX_NUMBER = 10
global auto
auto = True

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
       # self.quit = Button(self.window,text="Exit",command=self.des,width=8,font=("Arial 10 bold") ,bd=3,bg="#AA0121",fg='white',activebackground='#AA0121')
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



    def Admin_Page(self):

      
        def call_page(): # More Options
            root.withdraw()
            self.Options_page()
    


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
        More_option.place(x=250,y=580)
        
        mainloop()


    def User_Interface(self): # User Interface
        

        def disable_event(): # Close Window
            self.opened = False
        

        global flag_green
        global flag_red
        global darkMood
        darkMood = False
        flag_green = False
        flag_red = False
        style = tk.Style()
        root = Toplevel()
        root.protocol("WM_DELETE_WINDOW", disable_event)
        style.configure("BW.TRadiobutton",font=("Arial",17))
        root.title("Smart Classroom")
        root.geometry("800x650+250+50")
        root.resizable(False,False)
        root.iconbitmap("icons/lamp.ico")    
        r = IntVar()
        

        def on(num): # On/Off Buttons
            global flag_green
            global flag_red
            global MAX_NUMBER
            global auto
            
            if auto:
                ton1.config(command=None)
                ton2.config(command=None) 
                
            elif num == 5:
                if flag_green:
                    ton1.config(image=on_image)
                    flag_green = False
                    fe = '5'
                    s.write(fe.encode('utf-8'))
                else:
                    ton1.config(image=off_image)
                    flag_green = True
                    fe = '6'
                    s.write(fe.encode('utf-8'))

            elif num == 7:
                if flag_red:
                    ton2.config(image=on_image)
                    flag_red = False
                    fe = '7'
                    s.write(fe.encode('utf-8'))
                else:
                    ton2.config(image=off_image)
                    flag_red = True
                    fe = '8'
                    s.write(fe.encode('utf-8'))
            

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
                green.config(bg="#111111",fg="#E94560")
                red.config(bg="#111111",fg="#E94560")
                ton1.config(bg="#111111",activebackground="#111111")
                ton2.config(bg="#111111",activebackground="#111111")
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
                green.config(bg="#F0F0F0",fg="#134982")
                red.config(bg="#F0F0F0",fg="#134982")
                ton1.config(bg="#F0F0F0",activebackground="#F0F0F0")
                ton2.config(bg="#F0F0F0",activebackground="#F0F0F0")

            
        def mode(value): # Mode Radio Button
            global auto 
            if value == 1:
                auto = True
                getMode()
                        
            elif value == 2:  
                auto = False
                getMode()
                ton1.config(state=ACTIVE,command=lambda:on(5))
                ton2.config(state=ACTIVE,command=lambda:on(7))
                

        def adjustNumber(value): # Plus and Minus sign buttons
            global MAX_NUMBER
            if value == 1:
                MAX_NUMBER += 1
                students.config(text=MAX_NUMBER)
            else:
                if not (MAX_NUMBER <= 1):
                    MAX_NUMBER -= 1
                    students.config(text=MAX_NUMBER)


        plus_image = PhotoImage(file="icons/plus.png")
        minus_image = PhotoImage(file="icons/minus.png")
        on_image = PhotoImage(file="icons/on.png")
        off_image = PhotoImage(file="icons/off.png")
        logo_image = PhotoImage(file="icons/LightMode1.png")
        dark_logo = PhotoImage(file="icons/DarkMode1.png")

        l = Label(root,image=logo_image)   
        configs =Label(root,text="Configurations",fg="#AA0121",font=("Arial",30,"italic","underline"),padx=5)
        line = Label(root,fg="#134982",text="___________________________________________________________________________________________________________________________________________________________________",font=("Arial",20))
        number = Label(root,text=f"Students per section", font=("Arial",20,"bold"),fg="#134982")
        students = Label(root,text=MAX_NUMBER,font=("Arial",20),fg="black")
        increase = Button(root,text="+",font=("Arial",15),command=lambda:adjustNumber(1),bd=0,image=plus_image)
        decrease = Button(root,text="-",font=("Arial",15),padx=3,command=lambda:adjustNumber(2),image=minus_image,bd=0)        
        dark_mood = Button(root,text="Dark Mood",command=dark,width=8,font=("Arial 10 bold") ,bd=3,bg="black",fg='White',activeforeground='white',activebackground='black')
        modes = Label(root,text="Modes",font=("Arial",20,"bold"),fg="#134982")
        autos = tk.Radiobutton(root,text="Auto",variable=r,value=1,command=lambda:mode(r.get()),style="BW.TRadiobutton")
        manual = tk.Radiobutton(root,text="Manual",variable=r,value=2,command=lambda:mode(r.get()),style="BW.TRadiobutton")
        devices =Label(root,text="Device Control",fg="#AA0121",font=("Arial",30,"italic","underline"),padx=5)
        green = Label(root,text="Green LED", font=("Arial",20,"bold"),fg="#134982")
        red = Label(root,text="Red LED",font=("Arial",20,"bold"),fg="#134982")
        ton1 = Button(root,image=on_image,command=lambda:on(5),bd=0,padx=20)
        ton2 = Button(root,image=on_image,command=lambda:on(7),bd=0)
    
        l.place(x=280,y=-35)
        dark_mood.place(x=0,y=0)
        configs.place(x=270,y=180)
        number.place(x=30,y=270)
        increase.place(x=200,y=320)
        students.place(x=145,y=320)
        decrease.place(x=80,y=320)
        modes.place(x=600,y=270)
        autos.place(x=550,y=320)
        manual.place(x=650,y=320)
        line.place(x=0,y=350)
        devices.place(x=260,y=400)
        green.place(x=560,y=500)
        ton1.place(x=600,y=550)
        red.place(x=60,y=500)
        ton2.place(x=80,y=550)


        mode(1)
        mainloop()

    


def getMode(): # Update Mode
    return auto

def getMax(): # Update Number of students
    return MAX_NUMBER
    
app = Application_Interface()
app.run()