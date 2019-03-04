import tkinter as tk
import tkinter.font
from tkinter import *
from tkinter import messagebox
from tkinter import Menu
import RPi.GPIO as GPIO
wait=None
rec=None
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) #Rpi pinleri fiziksel olarak tanımlandı
#PINOUT SETTINGS
## MOTOR 1
GPIO.setup(3,GPIO.OUT) #Pin 3 1. servo çıkışı
pwm=GPIO.PWM(3,50) # Pin 3 ten 50 Hz PWM başlatılır
pwm.start(0) # Lets start PWM
##MOTOR 2
GPIO.setup(5,GPIO.OUT) #Pin 5 ten 2. servo çıkışı
pwm2=GPIO.PWM(5,50)
pwm2.start(0)

#SERVO SIGNAL CODES
def SetAngle(angle):  # Angle parametresi input alınacak
    duty = angle / 18 + 2  #Açı değeri PWM duty ye çevrilir
    GPIO.output(3, True)   # duty boyunca çıkış HIGH
    pwm.ChangeDutyCycle(duty)
    wait=pencere.after(1000) # Burada GUI kullandığımız için sleep yerine after fonksiyonu kullandık. Detaylar GUI branch da
    GPIO.output(3, False)   # OUTPUT is low till starting function again
    pwm.ChangeDutyCycle(0)
    
def SetAngle2(angle):  # 2. Motor için aynı fonksiyon.
    duty = angle / 18 + 2  
    GPIO.output(5, True)   
    pwm2.ChangeDutyCycle(duty)
    wait=pencere.after(1000)
    GPIO.output(5, False)   
    pwm2.ChangeDutyCycle(0)

#MOTOR ANGLES
def ServoOn():  #Servoya sinyal göndermek için, Set Angle fonksiyonlarını çağıran ana fonksiyon.
    x=int(str(angle1.get())) # GUI branchtaki Read Me'ye bakınız.
    y=int(str(angle2.get()))
    if x>180 or y>180:  # Robotun ulaşacağı noktalara göre açıları sınırlayınız.
     messagebox.showerror('TEKİLLİK HATASI', 'Verilebilecek en büyük açı 180 derecedir.') # Açı aşıldığında error mesajı verilir
     return None #fonksiyondan çıkmak için return None yazılır.
    SetAngle(x) #hata yoksa fonksiyonlar çağırılır
    SetAngle2(y)
##servoOn fonks sonu
    
def kayit():    
    global status
    status=False
    stop=False
    kayit = tk.Tk()    ## kayit ekranı penceresi.
    kayit.title("Kayit Ekrani")
    kayit.geometry('600x200')
    lbl=Label(kayit,text="  Kaydedilecek Pozisyonu Giriniz")
    lbl.grid(column=0,row=0,columnspan=4)
    lbl=Label(kayit,text="Bekleme Süresini Giriniz",width='20')
    lbl.grid(column=10,row=0)   
    lbl=Label(kayit,text="Tekrar Sayısını Giriniz",width='20')
    lbl.grid(column=100,row=0)
    def timereg():     # motorların belirtilen pozisyonda ne kadar süre bekleyeceğini belirlemek
        global timvar
        global inf
        timvar=0
        timvar=float(str(timnt.get()))
        timvar*=1000  #saniyeyi mS ye çevirdik
        if timvar>400:
         status=True
         inf='Zaman degeri kabul mü? :'+ str(status)# servonun beklemesi için min süre gerekli. Kontrol eden kodlar.
         Label(kayit,text=inf).grid(column=10,row=15)
         timvar=int(timvar)
         return True  #Koşullar sağlanırsa fonksiyon True çıkış verir
        else:
            status=False
            inf2='Zaman degeri kabul mü? :' + str(status)
            Label(kayit,text=inf2).grid(column=10,row=15)
            return False # koşullar sağlanmamışsa False çıkış vverir
    def tkrreg():    # Robotun belirliten hareketi kaç kez tekrarlayacağını belirten fonksiyon.
         global tkrvar
         tkrvar=int(str(tkrent.get()))
         inf3='Tekrar Sayisi :' + str(tkrvar)
         Label(kayit,text=inf3).grid(column=100,row=15)
         return True 
    def register ():
        global regvar
        global regvar2
        regvar=int(str(regent.get()))
        regvar2=int(str(regent2.get())) # ayrıntılar GUI de
        kayitlar='Motor1 :' +str(regvar) +' Motor2 :'+str(regvar2) #bilgi metini
        Label(kayit,text=kayitlar).grid(column=0,row=15)
        return regvar 
    def regOn():
        if timereg()==True and tkrreg()==True: #Tüm fonksiyonlar True çıkış verirse SetAngle çağırma koşulu sağlanır
          for x in range(tkrvar):  #tekrar sayısını for döngüsüyle sağladık
           SetAngle(regvar)
           SetAngle2(regvar2)
           kayit.after(timvar) # bekleme süresi burada
           SetAngle(0)
           SetAngle2(0) # robot 0 pozisyonuna döner.
           if x==tkrvar-1:
               messagebox.showinfo("Durum","Kayıt İşlemi Tamamlandı") # Döngü tamamlandığında bilgi mesaj kutusu
               
        else:
            messagebox.showerror('EKSIK PARAMETRE','Lütfen gerekli parametreleri tam olarak giriniz') # Fonksiyonlardan True bilgisi gelmemişse#alınan
     
    Label(kayit,text='Motor1       Motor2').grid(column=0,row=10,sticky=W) # Girdi kutucuğu bilgi metinleri
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
    
    
    
    

    ##Kayit fonk sonu
    
pencere = tk.Tk()
##Menu Toolbar
menu= Menu(pencere)  #menü toolbar fonksiyonu
yeni = Menu(menu,tearoff=0) 
yeni.add_command(label='Kayit',command=kayit) #kayit penceresi çağırma
menu.add_cascade(label='File', menu=yeni)
pencere.config(menu=menu)
#Başlık
pencere.title("SIKAR HA Control Panel")
pencere.geometry('480x255')
lbl = Label(pencere, text="MOTOR 1",fg='blue',bg='yellow',font=("Arial Bold",24),width='10') #Ana pencerede servoya bilgi gönderme kodları
lbl.grid(column=20, row=0)
lbl = Label(pencere, text="MOTOR 2",fg='blue',bg='yellow',font=("Arial Bold",24),width='10')
lbl.grid(column=150, row=0)
angle1 = Entry(pencere,width=5)
angle1.grid(column=20, row=40)

angle2 = Entry(pencere,width=5)
angle2.grid(column=150, row=40)


btn2= Button(pencere,text='Onayla', command=ServoOn,height='2',width='5')
btn2.grid(column=120,row=70)
 
pencere.mainloop()




