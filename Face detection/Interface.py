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
    style = tk.Style()
    style.configure("BW.TRadiobutton",font=("Arial",17))
    root.title("Smart Classroom")
    root.geometry("800x600")
    root.resizable(False,False)
    root.iconbitmap("logo2.ico")
    
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
    


    plus_image = PhotoImage(file="plus.png")
    minus_image = PhotoImage(file="minus.png")
    on_image = PhotoImage(file="on.png")
    off_image = PhotoImage(file="off.png")
    logo_image = PhotoImage(file="logo_image.png")
    
    l = Label(image=logo_image)   
    configs =Label(root,text="Configurations",fg="#00BDC9",font=("Arial",30,"italic","underline"),padx=5)
    line = Label(root,fg="#134982",text="___________________________________________________________________________________________________________________________________________________________________",font=("Arial",20))
    number = Label(root,text=f"Students per section", font=("Arial",20,"bold"),fg="#134982")
    students = Label(root,text=MAX_NUMBER,font=("Arial",20),fg="black")
    increase = Button(root,text="+",font=("Arial",15),command=lambda:adjustNumber(1),bd=0,image=plus_image)
    decrease = Button(root,text="-",font=("Arial",15),padx=3,command=lambda:adjustNumber(2),image=minus_image,bd=0)

    modes = Label(root,text="Modes",font=("Arial",20,"bold"),fg="#134982")
    autos = tk.Radiobutton(root,text="Auto",variable=r,value=1,command=lambda:mode(r.get()),style="BW.TRadiobutton")
    manual = tk.Radiobutton(root,text="Manual",variable=r,value=2,command=lambda:mode(r.get()),style="BW.TRadiobutton")

    devices =Label(root,text="Device Control",fg="#00BDC9",font=("Arial",30,"italic","underline"),padx=5)
    

    green = Label(root,text="Green LED", font=("Arial",20,"bold"),fg="#134982")
    red = Label(root,text="Red LED",font=("Arial",20,"bold"),fg="#134982")
    ton1 = Button(image=on_image,command=lambda:on(5),bd=0,padx=20)
    ton2 = Button(root,image=on_image,command=lambda:on(7),bd=0)


    l.place(x=225,y=-80)
    
    configs.place(x=260,y=130)
    
    number.place(x=30,y=220)
    increase.place(x=200,y=270)
    students.place(x=145,y=270)
    decrease.place(x=80,y=270)

    modes.place(x=600,y=220)
    autos.place(x=550,y=270)
    manual.place(x=650,y=270)
    
    line.place(x=0,y=300)
    
    devices.place(x=260,y=380)
    
    green.place(x=560,y=450)
    ton1.place(x=600,y=500)
    red.place(x=60,y=450)
    ton2.place(x=80,y=500)

    mode(1)
    mainloop()



def getMode():
    return auto
def getMax():
    return MAX_NUMBER


#draw()