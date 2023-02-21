import serial 
from tkinter import * 

MAX_NUMBER = 3
auto = True
s = serial.Serial('COM3',9600)

def draw():
        
    
    root = Tk()
    root.title("Smart Classroom")
    r = IntVar()
    

    def on(num):
        if num == 1:
            fe = '5'
            s.write(fe.encode('utf-8'))
            #MAX_NUMBER += 1
        elif num == 2:
            fe = '6'
            s.write(fe.encode('utf-8'))
            #MAX_NUMBER -= 1
        elif num == 3:
            fe = '7'
            s.write(fe.encode('utf-8'))
        elif num == 4:
            fe = '8'
            s.write(fe.encode('utf-8'))
    r.set("1")
    
    def mode(value):
        if value == 1:
            auto = True
            green = Label(root,text="Green",padx=70,state=DISABLED)
            red = Label(root,text="Red",padx=70,state=DISABLED)
            space = Label(root,text="              ")
            ton1 = Button(text="Turn on",state=DISABLED)
            toff1 = Button(text="Turn off",state=DISABLED)
            ton2 = Button(root,text="Turn on",state=DISABLED)
            toff2 = Button(root,text="Turn off",state=DISABLED)
            green.grid(row=0,column=0,pady=5,columnspan=2)
            red.grid(row=0,column=3,columnspan=2,pady=5)
            space.grid(row=0,column=1)
            ton1.grid(row=1,column=0)
            toff1.grid(row=1,column=1)
            ton2.grid(row=1,column=3)
            toff2.grid(row=1,column=4)

        else:
            auto = False
            green = Label(root,text="Green",padx=70)
            red = Label(root,text="Red",padx=70)
            space = Label(root,text="              ")
            ton1 = Button(text="Turn on",command=lambda:on(1))
            toff1 = Button(text="Turn off",command=lambda:on(2))
            ton2 = Button(root,text="Turn on",command=lambda:on(3))
            toff2 = Button(root,text="Turn off",command=lambda:on(4))   
            green.grid(row=0,column=0,pady=5,columnspan=2)
            red.grid(row=0,column=3,columnspan=2,pady=5)
            space.grid(row=0,column=1)
            ton1.grid(row=1,column=0)
            toff1.grid(row=1,column=1)
            ton2.grid(row=1,column=3)
            toff2.grid(row=1,column=4)
    mode(1)
    Radiobutton(root,text="Auto",variable=r,value=1,command=lambda:mode(r.get())).grid(row=2,column=0,padx=10,pady=5)
    Radiobutton(root,text="Manual",variable=r,value=2,command=lambda:mode(r.get())).grid(row=2,column=1,padx=10,pady=5)

    

    
    mainloop()
