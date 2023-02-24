import serial 
from tkinter import * 



global MAX_NUMBER
MAX_NUMBER = 10
global auto
auto = True
s = serial.Serial('COM3',9600)

def draw():
    
    
    root = Tk()
    root.title("Smart Classroom")
    r = IntVar()
    
    def on(num):
        global MAX_NUMBER
        if num == 5:
            fe = '5'
            s.write(fe.encode('utf-8'))
            MAX_NUMBER += 1
            maxN.config(text=MAX_NUMBER)
            print(MAX_NUMBER)

        elif num == 6:
            fe = '6'
            s.write(fe.encode('utf-8'))
            MAX_NUMBER -= 1
            maxN.config(text=MAX_NUMBER)
            
        elif num == 7:
            fe = '7'
            s.write(fe.encode('utf-8'))
        elif num == 8:
            fe = '8'
            s.write(fe.encode('utf-8'))
    r.set("1")
    
    def mode(value):
        global auto 
        if value == 1:
            auto = True
            getMode()
            print(auto)
            green.config(state=DISABLED)
            red.config(state=DISABLED)
            ton1.config(state=DISABLED)
            ton2.config(state=DISABLED)
            toff1.config(state=DISABLED)
            toff2.config(state=DISABLED)
        elif value == 2:  
            auto = False
            getMode()
            print(auto)    
            green.config(state=ACTIVE)
            red.config(state=ACTIVE)
            ton1.config(state=ACTIVE)
            ton2.config(state=ACTIVE)
            toff1.config(state=ACTIVE)
            toff2.config(state=ACTIVE)


    Radiobutton(root,text="Auto",variable=r,value=1,command=lambda:mode(r.get())).grid(row=2,column=0,padx=10,pady=5)
    Radiobutton(root,text="Manual",variable=r,value=2,command=lambda:mode(r.get())).grid(row=2,column=1,padx=10,pady=5)

    green = Label(root,text="Green",padx=70)
    red = Label(root,text="Red",padx=70)
    space = Label(root,text="              ")
    maxN = Label(root,text=str(MAX_NUMBER))
    ton1 = Button(text="Turn on",command=lambda:on(5))
    toff1 = Button(text="Turn off",command=lambda:on(6))
    ton2 = Button(root,text="Turn on",command=lambda:on(7))
    toff2 = Button(root,text="Turn off",command=lambda:on(8))

    green.grid(row=0,column=0,pady=5,columnspan=2)
    red.grid(row=0,column=3,columnspan=2,pady=5)
    space.grid(row=0,column=1)
    ton1.grid(row=1,column=0,columnspan=1)
    toff1.grid(row=1,column=1)
    ton2.grid(row=1,column=3)
    toff2.grid(row=1,column=4)
    maxN.grid(row=3,column=0,padx=30)
   
    mode(1)
    mainloop()

def getMode():
    return auto
def getMax():
    return MAX_NUMBER