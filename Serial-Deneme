import serial
import tkinter
from tkinter import *
from tkinter import messagebox

arduino=Tk()
arduino.title('KONUM KAYIT')
arduino.geometry('400x200')
arduino.minsize(height='200',width='400')
Label(arduino,text='Robot Pozisyonu').grid(column=1,row=0)
ser= serial.Serial('/dev/ttyACM0',9600)
global reg
reg=[]
global counter1
counter1 = 0
global counter2
counter2 = 0
def KayitBaslat():
    if len(reg)<4:
        messagebox.showerror('HATA!',' Robota en az 2 konum vermelisiniz !')
        return None
    else :
            bilgi='Robot şu konumlara ilerleyecektir :' + str(reg)
            messagebox.showinfo('BAŞARILI!',bilgi)
    
def SerialRead():
    global counter
    global base
    global yatay
    global dikey
    counter = 0
    while 1:
        if (counter==0):
            base=int(ser.readline())
            if base>0:
                counter=1
         
        if (counter==1):
            yatay = int(ser.readline())
            if yatay>0:
                counter=2
        if (counter==2):
            dikey = int(ser.readline())
            if dikey>0:
                counter = 3
        if (counter==3):
            bilgi="Alınan açı bilgileri :\n" "Motor 1 :"+str(base) + ("\nMotor 2 :")+ str(yatay) +("\nMotor 3 :") +str(dikey)
            messagebox.showinfo(' KAYIT TAMAMLANDI',bilgi)
            counter = 0
            break

def kayit1():
    global brg1
    global yrg1
    global drg1
    global counter1
    if counter1 == 0:
        brg1=base
        yrg1=yatay
        drg1=dikey
        counter1 = 1
        
    reg.append(brg1)
    reg.append(yrg1)
    reg.append(drg1)
        
    bilgi1="Alınan açı bilgileri :\n" "Motor 1 :"+str(brg1) + ("\nMotor 2 :")+ str(yrg1) +("\nMotor 3 :") +str(drg1)
    messagebox.showinfo(' POZİSYON 1',bilgi1)
def kayit2():
    global counter1
    global brg2
    global yrg2
    global drg2
    if counter1 == 1:
        brg2=base
        yrg2=yatay
        drg2=dikey
        counter1=2
        reg.append(brg2)
        reg.append(yrg2)
        reg.append(drg2)
    bilgi2="Alınan açı bilgileri :\n" "Motor 1 :"+str(brg2) + ("\nMotor 2 :")+ str(yrg2) +("\nMotor 3 :") +str(drg2)
    messagebox.showinfo(' POZİSYON 1',bilgi2)
serial=Button(arduino,text='Serial Port Aç',command=SerialRead)
serial.grid(column =1,row=1)
Label(text='Kayıtlı Olan Pozisyonlar',fg='black',bg='yellow',font='Arial',height=2).grid(column=1,row=2)
bkayit1=Button(text='1. Pozisyon',command=kayit1)
bkayit1.grid(column=0,row=3,sticky=W)
bkayit2=Button(text='2. Pozisyon',command=kayit2)
bkayit2.grid(column=2,row=3,sticky=W)

bkayitbaslat=Button(text='Kayıt Başlat',fg='yellow',bg='blue',font='Arial',height=2,command=KayitBaslat)
bkayitbaslat.grid(column=1,row=4)
