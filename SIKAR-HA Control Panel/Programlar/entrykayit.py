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
def kayit():
    global status
    status=False
    stop=False
    kayit = Tk()
    kayit.title("Kayit Ekrani")
    kayit.geometry('600x200')
    lbl=Label(kayit,text="  Kaydedilecek Pozisyonu Giriniz")
    lbl.grid(column=0,row=0,columnspan=4)
    lbl=Label(kayit,text="Bekleme Süresini Giriniz",width='20')
    lbl.grid(column=10,row=0)   
    lbl=Label(kayit,text="Tekrar Sayısını Giriniz",width='20')
    lbl.grid(column=100,row=0)
    def timereg():
        global timvar
        global inf
        timvar=0
        timvar=float(str(timnt.get()))
        timvar*=1000
        if timvar>400:
         status=True
         inf='Zaman degeri kabul mü? :'+ str(status)
         Label(kayit,text=inf).grid(column=10,row=15)
         timvar=int(timvar)
         return True
        else:
            status=False
            inf2='Zaman degeri kabul mü? :' + str(status)
            Label(kayit,text=inf2).grid(column=10,row=15)
            return False
    def tkrreg():
         global tkrvar
         tkrvar=int(str(tkrent.get()))
         inf3='Tekrar Sayisi :' + str(tkrvar)
         Label(kayit,text=inf3).grid(column=100,row=15)
         return True
    def register ():
        global regvar
        global regvar2
        regvar=int(str(regent.get()))
        regvar2=int(str(regent2.get()))
        kayitlar='Motor1 :' +str(regvar) +' Motor2 :'+str(regvar2)
        Label(kayit,text=kayitlar).grid(column=0,row=15)
        return regvar
    def regOn():
        if timereg()==True and tkrreg()==True:
          for x in range(tkrvar):  
           SetAngle(regvar)
           SetAngle2(regvar2)
           kayit.after(timvar)
           SetAngle(0)
           SetAngle2(0)
           if x==tkrvar-1:
               messagebox.showinfo("Durum","Kayıt İşlemi Tamamlandı")
               
        else:
            messagebox.showerror('EKSIK PARAMETRE','Lütfen gerekli parametreleri tam olarak giriniz')
     
    Label(kayit,text='Motor1       Motor2').grid(column=0,row=10,sticky=W)
    regent= Entry(kayit,width=4)
    regent.grid(column=0,row=11,sticky=W)
    regent2= Entry(kayit,width=5)
    regent2.grid(column=0,row=11)
    regbtn=Button(kayit,text='Onayla',command = register,width='5')
    regbtn.grid(column=0,row=20,sticky=W)
    regOnbtn=Button(kayit,text='Başlat',font=("Arial",18),bg='yellow',fg='blue',command=regOn)
    regOnbtn.grid(column=10,row=180)
    regOnbtn.config(height=1,width=10)
    
    timnt=Entry(kayit,width=5)
    timnt.grid(column=10,row=11)
    timbtn=Button(kayit,text='Onayla',command = timereg)
    timbtn.grid(column=10,row=20)
    
    tkrent=Entry(kayit,width=5)
    tkrent.grid(column=100,row=11)
    tkrbtn=Button(kayit,text='Onayla',command = tkrreg)
    tkrbtn.grid(column=100,row=20)
    kayit.mainloop()

kayit()
 