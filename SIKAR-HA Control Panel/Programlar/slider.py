import tkinter.font
from tkinter import *
from tkinter import messagebox
from tkinter import Menu
import RPi.GPIO as GPIO
import os
wait=None
rec=None
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) #Numbers GPIOs by physical location
def SetAngle(angle):  # Angle paramater will be got from user
    print('go')
def SetAngle2(angle):  # Angle paramater will be got from user
    print('go')
def SetAngle3(angle):  # Angle paramater will be got from user
    print('go')
#MOTOR ANGLES
def ServoOn():
    x=int(str(angle1.get()))
    y=int(str(angle2.get()))
    if x>180 or y>180:
     messagebox.showerror('TEKİLLİK HATASI', 'Verilebilecek en büyük açı 180 derecedir.')
     return None
    SetAngle(x)
    SetAngle2(y)
##servoOn fonks sonu
global grp
grp=150
def GrOn():
    global grp
    grp+=1
    SetAngle3(155)
    grinfo=Label(slide,text='Gripper Pozisyonu:'+str(grp)).grid(column=25,row=1)

def GrOff():
    global grp
    grp-=1
    if grp<150 or grp>170:
        messagebox.showerror('TEKİLLİK HATASI','Gripper Konum Sınırlarına ulaşılmıştır.')
        return None
    SetAngle3(176)
    grinfo2=Label(slide,text='Gripper Pozisyonu:'+str(grp)).grid(column=25,row=1)

    
def Gripper():
    z=int(str(gripper.get()))
    global grp
    grp = z
    SetAngle3(z)
   


def slider():
    global angle1
    global angle2
    global gripper
    global slide
    slide=Tk()
    slide.geometry('750x400')
    slide.title('SLIDER İLE HAREKET')
    lbl = Label(slide, text="MOTOR 1",fg='blue',bg='yellow',font=("Arial Bold",24),width='10')
    lbl.grid(column=20, row=0)
    lbl = Label(slide, text="MOTOR 2",fg='blue',bg='yellow',font=("Arial Bold",24),width='10')
    lbl.grid(column=20, row=3)
    lbl = Label(slide, text="GRIPPER",fg='blue',bg='yellow',font=("Arial Bold",24),width='10')
    lbl.grid(column=25, row=0,sticky=E)
    angle1 = Scale(slide,from_=0,to=180,orient=HORIZONTAL)
    angle1.grid(column=20, row=1)
    
    angle2 = Scale(slide,from_=0,to=180,orient=HORIZONTAL)
    angle2.grid(column=20, row=4)



    btn2= Button(slide,text='Onayla', command=ServoOn,height='2',width='5')
    btn2.grid(column=20,row=5)

    gon= Button(slide,text='Gripper Aç',command=GrOn)
    gon.grid(column=24,row=1,sticky=E)

    goff= Button(slide,text='Gripper Kapat', command=GrOff)
    goff.grid(column=26,row=1,sticky=E)
    gripper=Scale(slide,from_=150,to=180,orient=HORIZONTAL)
    gripper.grid(column=25,row=2)

    grpbutton=Button(slide,text='Move',command=Gripper)
    grpbutton.grid(column=25,row=3)
    slide.mainloop()
slider()