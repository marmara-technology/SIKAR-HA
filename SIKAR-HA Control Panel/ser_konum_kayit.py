import serial
import time
import tkinter
from tkinter import *
from tkinter import messagebox
import RPi.GPIO as GPIO
from tkinter import Menu
from tkinter import filedialog
import sys

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) #Numbers GPIOs by physical location
GPIO.setup(5,GPIO.OUT)
GPIO.output(5,GPIO.LOW)
#ser = None
while True :
    try:
        tries=0
        if tries ==0:
            try:
              ser= serial.Serial('/dev/ttyACM0',9600)
              break
            except:
                tries = 1
        if tries == 1:
            try:
                ser = serial.Serial('/dev/ttyACM1',9600)
                break
            except:
                tries = 2
        if tries == 2:
            try:
                ser=serial.Serial('/dev/ttyACM2',9600)
                break
            except:
                 print("HATA ! Lütfen Arduino serial kablosunu kontrol ediniz")
    except:
        print("BAŞARISIZ")
           
    
time.sleep(1)
arduino=Tk()
arduino.title('KONUM KAYIT')
arduino.geometry('550x430')
arduino.minsize(height='800',width='430')
Label(arduino,text='Robot Konumlandırınız',height=2,font='Arial').grid(column = '1',row = '0')
Label(arduino,text="KAYIT NO",fg = 'blue',bg='White',height = '4',width= 14,font=('times',20)).grid(column = 0,row = 6)
Label(arduino,text= "KONUM BİLGİLERİ",bg = 'white',width = 17,height = '4',font=('times',20)).grid(column = 1,row=6)
global reg
reg=[]
global counter1
counter1 = 0
global counter2
counter2 = 0
global kayitno
kayitno = 0
def Kayitlar():
    kayitnumara = "Konum " + str(kayitno)
    kayitdurum1=Label(arduino,text=kayitnumara,fg = 'blue',bg='White',height = '4',width= 14,font=('times',20)).grid(column = 0,row = 5+int(kayitno),sticky=E)
    kayitlar = "Base Motor :"+str(base) + ("\nYatay Motor :")+ str(yatay) +("\nDikey Motor :") +str(dikey) +("\nGripper") + str(gripper)
    kayitdurum = Label(arduino,text= kayitlar,bg = 'white',width = 17,font=('times',20)).grid(column = 1,row=5+int(kayitno),sticky = E)
   

def sil():
    global kayitno
    global x
    
    kayitno -=1
    if kayitno<0:
        kayitno=0
        return None
    for i in range (0,4):
        reg.pop()
    Label(arduino, text ="    KAYIT", bg ='white',width = 14,height = 4,font=('times',20)).grid( column = 0, row= 5 + int(kayitno) +1)
    Label(arduino, text ="SİLİNDİ", bg ='white',width = 17,height = 4,font=('times',20)).grid( column = 1, row= 5 + int(kayitno) +1) 
def KayitBaslat():
    
    if len(reg)<1:
        messagebox.showerror('HATA!',' Robota en az 2 konum vermelisiniz !')
        return None
    else :
            bilgi='Robot kayıtlı konumlara ilerleyecektir'
            messagebox.showinfo('BAŞARILI!',bilgi)
            
            for i in range(len(reg)):
                a=reg[i]
                
                ser.write(str(a).encode())
                
                time.sleep(0.2)
                i+=1
                if i%4 == 0:
                    time.sleep(1)
            
            return None
               
def kayit():
    global kayitno
    reg.append(base)
    reg.append(yatay)
    reg.append(dikey)
    reg.append(gripper)    
    kayitno+=1
    Kayitlar()
    #bilgi1="Alınan açı bilgileri :\n" "Base Motor :"+str(brg) + ("\nYatay Motor :")+ str(yrg) +("\nDikey Motor 3 :") +str(drg) +("\nGripper  :") + str(grp)
    #messagebox.showinfo(' POZİSYON 1',bilgi1)
    
def SerialRead():
    global counter
    global base
    global yatay
    global dikey
    global gripper
    global grpkonum
    counter = 0
    GPIO.output(5,GPIO.HIGH)
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
            
            #bilgi="Alınan açı bilgileri :\n" "Base Motor :"+str(base) + ("\nYatay Motor :")+ str(yatay) +("\nDikey Motor :") +str(dikey) +("\nGripper") + str(gripper)
            #messagebox.showinfo(' KAYIT TAMAMLANDI',bilgi)
            counter = 0
            GPIO.output(5,GPIO.LOW)
            break
    kayit()

def dosya_kaydet():
    global reg
    global yaz
    yaz = ""
    #yaz = "global saved\n" + "saved = " + str(reg)
    if len(reg) < 8:
        messagebox.showerror('HATA',' Lütfen en az 2 konum belirleyiniz')
        return None
    for i in range(len(reg)):
        yaz+=str(reg[i])
        yaz+=" "
    f = filedialog.asksaveasfile(initialdir = '/home/pi/Desktop/SIKAR-HA Control Panel/Kayitlar',mode='w', defaultextension=".txt")
    if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return # starts from `1.0`, not `0.0`
    f.write(yaz)
    f.close() # `()` was missing.
    
def dosya_ac():
    filename = filedialog.askopenfile(initialdir = '/home/pi/Desktop/SIKAR-HA Control Panel/Kayitlar')
    saved = filename.read()
    reg.clear()
    global kayitno
    global base
    global yatay
    global dikey
    global gripper
    kayitli = saved.split()
    for i in range(len(kayitli)):
        reg.append(int(kayitli[i]))
    
    for i in range(len(reg)):
        if i%4==0:
            base=reg[i-4]
            yatay=reg[i-3]
            dikey=reg[i-2]
            gripper = reg[i-1]
            kayitno+=1
            Kayitlar()
        if i == len(reg)-1:
            messagebox.showinfo(' BAŞARILI','Kayıtlı Robot konumlarına ulaşıldı')

def bos():
    return None

serial=Button(arduino,text='Serial Port Aç',fg='white',bg='blue',font = 'Arial',command=SerialRead,height = 2)
serial.grid(column =0,row=1)
Label(text='Kayıtlı Olan Pozisyonlar',fg='black',bg='yellow',font='Arial',height=2).grid(column = 1, row = 2)
#bkayit1=Button(text='1. Pozisyon',command=kayit)
#bkayit1.grid(column=1,row=3,sticky=W)
bkayitbaslat=Button(text='Kayıt Başlat',fg='white',bg='red',font='Arial',width = 11,height=2,command=KayitBaslat)
bkayitbaslat.grid(column=0,row=2)

gerial=Button(text='Geri Al ', font=('times',14),width = 11,height=2,command = sil).grid(column = 1, row = 1)
menubar = Menu(arduino)
filemenu = Menu(menubar)
filemenu.add_command(label ="Aç", command = dosya_ac)
filemenu.add_command(label = " Kaydet",command =dosya_kaydet)
menubar.add_cascade(label ="Kayit İşlemleri", menu = filemenu)
arduino.config(menu=menubar)
arduino.mainloop()