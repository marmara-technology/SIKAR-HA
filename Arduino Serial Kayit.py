import serial
import time
import tkinter
from tkinter import *
from tkinter import messagebox
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) #Numbers GPIOs by physical location
GPIO.setup(3,GPIO.OUT)
GPIO.output(3,GPIO.HIGH)
ser= serial.Serial('/dev/ttyACM0',9600)
time.sleep(1)
arduino=Tk()
arduino.title('KONUM KAYIT')
arduino.geometry('400x200')
arduino.minsize(height='200',width='400')
Label(arduino,text='Robot Pozisyonu').grid(column=1,row=0)
global reg
reg=[]
global counter1
counter1 = 0
global counter2
counter2 = 0
def KayitBaslat():
    
    if len(reg)<1:
        messagebox.showerror('HATA!',' Robota en az 2 konum vermelisiniz !')
        return None
    else :
            bilgi='Robot şu konumlara ilerleyecektir :' + str(reg)
            messagebox.showinfo('BAŞARILI!',bilgi)
            
            for i in range (0,8):
                a=reg[i]
                
                ser.write(str(a).encode())
                
                time.sleep(1.2)
                i+=1
                if i == 4:
                    time.sleep(2)
            
            return None
               
    
def SerialRead():
    global counter
    global base
    global yatay
    global dikey
    global gripper
    global grpkonum
    counter = 0
    while 1:
        if (counter==0):
            base=int(ser.readline())
            counter=1
         
        if (counter==1):
            yatay = int(ser.readline())        
            counter=2
        if (counter==2):
            dikey = int(ser.readline())
            counter = 3
        if (counter == 3):
            gripper = int(ser.readline())
            counter = 4
        if (counter==4):
            
            bilgi="Alınan açı bilgileri :\n" "Base Motor :"+str(base) + ("\nYatay Motor :")+ str(yatay) +("\nDikey Motor :") +str(dikey) +("\nGripper") + str(gripper)
            messagebox.showinfo(' KAYIT TAMAMLANDI',bilgi)
            counter = 0
            break

def kayit1():
    global brg1
    global yrg1
    global drg1
    global grp1
    global counter1
    if counter1 == 0:
        brg1=base
        yrg1=yatay
        drg1=dikey
        grp1=gripper
        counter1 = 1
        
    reg.append(brg1)
    reg.append(yrg1)
    reg.append(drg1)
    reg.append(grp1)
        
    bilgi1="Alınan açı bilgileri :\n" "Base Motor :"+str(brg1) + ("\nYatay Motor :")+ str(yrg1) +("\nDikey Motor 3 :") +str(drg1) +("\nGripper  :") + str(grp1)
    messagebox.showinfo(' POZİSYON 1',bilgi1)
def kayit2():
    global counter1
    global brg2
    global yrg2
    global drg2
    global grp2
    if counter1 == 1:
        brg2=base
        yrg2=yatay
        drg2=dikey
        grp2=gripper
        counter1=2
        reg.append(brg2)
        reg.append(yrg2)
        reg.append(drg2)
        reg.append(grp2)
    bilgi2="Alınan açı bilgileri :\n" "Base Motor :"+str(brg2) + ("\nYatay Motor :")+ str(yrg2) +("\nDikey Motor 3 :") +str(drg2) +("\nGripper") + str(grp2)
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