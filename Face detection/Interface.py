import serial 
from tkinter import * 
import tkinter.ttk as tk


global MAX_NUMBER
MAX_NUMBER = 10
global auto
auto = True
flag_green = False
flag_red = False
s = serial.Serial('COM3',9600)

def draw():
    
    
    root = Tk()
    # root.configure(bg="black")
    style = tk.Style()
    style.configure("TRadiobutton",font=("Arial",17),background="#F0F0F0")
    root.title("Smart Classroom")
    root.geometry("800x650")
    root.resizable(False,False)
    root.iconbitmap("icons/logo2.ico")
    
    r = IntVar()
    
    def on(num):
        global flag_green
        global flag_red
        global MAX_NUMBER
        if num == 5:
          
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

    def mode(value):
        global auto 
        if value == 1:
            auto = True
            getMode()
            print(auto)
            ton1.config(state=DISABLED)
            ton2.config(state=DISABLED)
    
        elif value == 2:  
            auto = False
            getMode()
            print(auto)    
            ton1.config(state=ACTIVE)
            ton2.config(state=ACTIVE)
            


    def adjustNumber(value):
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
    logo_image = PhotoImage(file="icons/SCR-logo2.png")
    
    l = Label(image=logo_image)   
    configs =Label(root,text="Configurations",fg="#AA0121",font=("Arial",30,"italic","underline"),padx=5)
    line = Label(root,fg="black",text="___________________________________________________________________________________________________________________________________________________________________",font=("Arial",20))
    number = Label(root,text=f"Students per section", font=("Arial",20,"bold"),fg="#134982")
    students = Label(root,text=MAX_NUMBER,font=("Arial",20),fg="black")
    increase = Button(root,text="+",font=("Arial",15),command=lambda:adjustNumber(1),bd=0,image=plus_image)
    decrease = Button(root,text="-",font=("Arial",15),padx=3,command=lambda:adjustNumber(2),image=minus_image,bd=0)
    modes = Label(root,text="Modes",font=("Arial",20,"bold"),fg="#134982")
    autos = tk.Radiobutton(root,text="Auto",variable=r,value=1,command=lambda:mode(r.get()))
    manual = tk.Radiobutton(root,text="Manual",variable=r,value=2,command=lambda:mode(r.get()))

    devices =Label(root,text="Device Control",fg="#AA0121",font=("Arial",30,"italic","underline"),padx=5)
    

    green = Label(root,text="Green LED", font=("Arial",20,"bold"),fg="#134982")
    red = Label(root,text="Red LED",font=("Arial",20,"bold"),fg="#134982")
    ton1 = Button(image=on_image,command=lambda:on(5),bd=0,padx=20)
    ton2 = Button(root,image=on_image,command=lambda:on(7),bd=0)


    l.place(x=280,y=-35)
    

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



def getMode():
    return auto
def getMax():
    return MAX_NUMBER


draw()