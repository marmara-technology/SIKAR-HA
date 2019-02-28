import tkinter as tk
import tkinter.font
from tkinter import *
from tkinter import messagebox
import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) #Numbers GPIOs by physical location
GPIO.setup(3,GPIO.OUT) #Pin 3 is set output for servo
pwm=GPIO.PWM(3,50) # creating 50 Hz PWM from Pin 3 (Servo works with 20ms period or 50Hz freq)
pwm.start(0) # Lets start PWM

pencere = tk.Tk()

pencere.title("SIKAR HA Control Panel")
pencere.geometry('780x555')
lbl = Label(pencere, text="MOTOR1")
lbl.grid(column=0, row=0)
a=0
def clicked():

 lbl.configure(text="Button was clicked !!")
 
def SetAngle(angle):  # kullanıcıdan alınacak açı parametresi
    duty = angle / 18 + 2  #açıyı duty e çevir
    GPIO.output(3, True)   # Çıkış duty boyunca HIGH olacaktır
    pwm.ChangeDutyCycle(duty)
    sleep(1) # servonun pozisyon almasını bekle
    GPIO.output(3, False)   # Fonksiyon tekrar çalışana kadar çıkış LOW
    pwm.ChangeDutyCycle(0)

def tanimlama():    # Kullanıcı GUI den açı değeri girdiğinde çağrılan fonksiyon
 global x  
 global txt    # farklı fonksiyonlarda çağrılacağı için global kullanılır.
 txt = Entry(pencere,width=3) #Entry e girilen değer "txt" parametresine atanır
 txt.grid(column=1, row=0)  # entry nin bulunduğu konum
 a=1
 btn2= Button(pencere,text='Onayla', command=ServoOn) #entry nin onaylandığı buton
 btn2.grid(column=0,row=5)
 
btn = Button(pencere, text='Açı giriniz',bg = 'yellow',fg='blue',command=tanimlama) # program açıldığında buradan başlayacaktır.
btn.grid(column=0, row=1) # Bu butona basıldığında commnad sayesinde tanimlama fonksiyonu çağırılır.
def ServoOn(): #tanimlama fonksiyonundaki onayla butonu bu fonksiyonu çağırır
    x=int(str(txt.get())) #Burası çok önemli. Detaylı anlatım "panelreadme" dosyasında bulunmaktadır
    if x>180: # açı değeri 180 i aştığında :
     messagebox.showerror('TEKİLLİK HATASI', 'Verilebilecek en büyük açı 180 derecedir.') #hata mesajı verilir
     return None # bu satır yazılarak fonksiyondan çıkışsız olarak ayrılırız
    SetAngle(x) # eğer 180 i aşmamışsa program burdan devam eder ve SetAngle fonksiyonuna x değeri atanır
    mtn = Label(pencere, text="1. motor pozisyon aldi") # işlem tamamlandığına dair bilgi texti
    mtn.grid(column = 11,row=0)
 
pencere.mainloop()




