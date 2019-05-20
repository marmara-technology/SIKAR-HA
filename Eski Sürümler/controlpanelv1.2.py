import webbrowser
import tkinter.font
from tkinter import *
from tkinter import messagebox
from tkinter import Menu
import RPi.GPIO as GPIO
wait=None
rec=None
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) #Numbers GPIOs by physical location
#PINOUT SETTINGS
## MOTOR 1
GPIO.setup(3,GPIO.OUT) #Pin 3 is set output for servo
pwm=GPIO.PWM(3,50) # creating 50 Hz PWM from Pin 3 (Servo works with 20ms period or 50Hz freq)
pwm.start(0) # Lets start PWM
##MOTOR 2
GPIO.setup(5,GPIO.OUT)
pwm2=GPIO.PWM(5,50)
pwm2.start(0)
##GRIPPER
GPIO.setup(7,GPIO.OUT)
pwm3=GPIO.PWM(7,50)
pwm3.start(0)

#SERVO SINYAL KODLARI
def SetAngle(angle):  # Angle paramater will be got from user
    duty = angle / 18 + 2  #Converting angle to duty
    GPIO.output(3, True)   # OUTPUT is high along the duty length
    pwm.ChangeDutyCycle(duty)
    wait=pencere.after(1000) # wait servo to get there
    GPIO.output(3, False)   # OUTPUT is low till starting function again
    pwm.ChangeDutyCycle(0)
    
def SetAngle2(angle):  # Angle paramater will be got from user
    duty = angle / 18 + 2  #Converting angle to duty
    GPIO.output(5, True)   # OUTPUT is high along the duty length
    pwm2.ChangeDutyCycle(duty)
    wait=pencere.after(1000) # wait servo to get there
    GPIO.output(5, False)   # OUTPUT is low till starting function again
    pwm2.ChangeDutyCycle(0)

def SetAngle3(angle):  # Angle paramater will be got from user
    duty = angle / 18 + 2  #Converting angle to duty
    GPIO.output(7, True)   # OUTPUT is high along the duty length
    pwm3.ChangeDutyCycle(duty)
    wait=pencere.after(1000) # wait servo to get there
    GPIO.output(7, False)   # OUTPUT is low till starting function again
    pwm3.ChangeDutyCycle(0)

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
    grinfo=Label(pencere,text='Gripper Pozisyonu:'+str(grp)).grid(column=24,row=71)

def GrOff():
    global grp
    grp-=1
    if grp<150 or grp>170:
        messagebox.showerror('TEKİLLİK HATASI','Gripper Konum Sınırlarına ulaşılmıştır.')
        return None
    SetAngle3(176)
    grinfo2=Label(pencere,text='Gripper Kapalı').grid(column=24,row=71)

    
def Gripper():
    z=int(str(gripper.get()))
    SetAngle3(z)


def kayit():
    global status
    status=False
    stop=False
    kayit = Tk()
    kayit.title("Kayit Ekrani")
    kayit.geometry('520x200')
    kayit.minsize(width=520,height=200)  // GUNCELLEME
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
    
    
    
    

    ##Kayit fonk sonu
def konumsal():
    global angle1
    global angle2
    global gripper
    konum=Tk()
    konum.geometry('750x400')
    konum.title('KONUM BİLGİSİNE GÖRE HAREKET')
    lbl = Label(konum, text="MOTOR 1",fg='blue',bg='yellow',font=("Arial Bold",24),width='10')
    lbl.grid(column=20, row=0)
    lbl = Label(konum, text="MOTOR 2",fg='blue',bg='yellow',font=("Arial Bold",24),width='10')
    lbl.grid(column=21, row=0)
    lbl = Label(konum, text="GRIPPER",fg='blue',bg='yellow',font=("Arial Bold",24),width='10')
    lbl.grid(column=22, row=0)
    angle1 = Entry(konum,width=5)
    angle1.grid(column=20, row=40)
    
    angle2 = Entry(konum,width=5)
    angle2.grid(column=21, row=40)



    btn2= Button(konum,text='Onayla', command=ServoOn,height='2',width='5')
    btn2.grid(column=21,row=41,sticky=W)

    gon= Button(konum,text='Gripper Aç', command=GrOn)
    gon.grid(column=22,row=41)

    goff= Button(konum,text='Gripper Kapat', command=GrOff)
    goff.grid(column=30,row=41,sticky=W)
    gripper=Scale(konum,from_=150,to=180,orient=HORIZONTAL)
    gripper.grid(column=30,row=100)

    grpbutton=Button(konum,text='Move',command=Gripper)
    grpbutton.grid(column=30,row=181)
    konum.mainloop()

def slider():
    global angle1
    global angle2
    global gripper
    
    slide=Tk()
    slide.geometry('750x400')
    slide.title('SLIDER İLE HAREKET')
    lbl = Label(slide, text="MOTOR 1",fg='blue',bg='yellow',font=("Arial Bold",24),width='10')
    lbl.grid(column=20, row=0)
    lbl = Label(slide, text="MOTOR 2",fg='blue',bg='yellow',font=("Arial Bold",24),width='10')
    lbl.grid(column=20, row=3)
    lbl = Label(slide, text="GRIPPER",fg='blue',bg='yellow',font=("Arial Bold",24),width='10')
    lbl.grid(column=22, row=0)
    angle1 = Scale(slide,from_=0,to=180,orient=HORIZONTAL)
    angle1.grid(column=20, row=1)
    
    angle2 = Scale(slide,from_=0,to=180,orient=HORIZONTAL)
    angle2.grid(column=20, row=4)



    btn2= Button(slide,text='Onayla', command=ServoOn,height='2',width='5')
    btn2.grid(column=20,row=5,sticky=W)

    gon= Button(slide,text='Gripper Aç', command=GrOn)
    gon.grid(column=22,row=41)

    goff= Button(slide,text='Gripper Kapat', command=GrOff)
    goff.grid(column=30,row=41,sticky=W)
    gripper=Scale(slide,from_=150,to=180,orient=HORIZONTAL)
    gripper.grid(column=30,row=100)

    grpbutton=Button(slide,text='Move',command=Gripper)
    grpbutton.grid(column=30,row=181)
    slide.mainloop()

def helphareket():  # GUNCELLEME
  helpme= Tk()
  helpme.title('YARDIM')
  helpme.geometry('500x200')
  yardim = ' Öncelikle kontrol potlarını kullanarak robotu istediğiniz konuma getiriniz.\n\
             Ardından control panel menuden konum al a tıklayınız.\n \
             Açılan pencereden Serial Başlat butonuna basın ve kayıt butonunu aktif edin.\n \
             Butona bastığınızda kayıt işlemi tamamlanacak ve bilgi kutucuğu karşınıza çıkacak.\n\
             Eğer açı değerleriniz doğru ise onaylayın ve işleminize devam edin.'
  Label(helpme,text=yardim).grid(column=0,row=0)
  Button(helpme,text='Anladım',command=helpme.destroy).grid(column=0,row=1)
 
def donothing():
    messagebox.showinfo('BİLGİ','SEKME ŞU ANDA BOŞ. YAKINDA İÇERİK EKLENECEK')

pencere = Tk()
##Menu Toolbar
menubar = Menu(pencere)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Yeni", command=donothing)
filemenu.add_command(label="Aç", command=donothing)
filemenu.add_command(label="Kaydet", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Çık", command=pencere.quit)
menubar.add_cascade(label="Dosya", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)

editmenu.add_command(label="Konum Bilgisi", command=konumsal)
editmenu.add_command(label="Slider", command=slider)
editmenu.add_command(label="Klavye", command=donothing)
editmenu.add_command(label="Pot ile", command=donothing)

kayitmenu= Menu(menubar, tearoff=0)
kayitmenu.add_command(label="Hareket Kaydet",command=kayit)
menubar.add_cascade(label="Kayit",menu=kayitmenu)
menubar.add_cascade(label="Hareket", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Hareket?", command=helphareket) # GUNCELLEME
helpmenu.add_command(label="Hakkında", command=donothing)
menubar.add_cascade(label="Yardım", menu=helpmenu)


#Başlık
pencere.title("SIKAR HA Control Panel")
pencere.geometry('550x400')
lbl = Label(pencere, text="SIKAR HA! CONTROL PANEL",fg='blue',bg='yellow',font=("Arial Bold",24)).pack()
def github():
    onay=messagebox.askokcancel('Yönlendirme', 'SIKARHA! Github sayfasına yönlendiriliyorsunuz. Onay ?')
    if onay == True:
         webbrowser.open('https://github.com/OgiBalboa/servo')
    else:
        return None
   

infobtn=Button(pencere,text='GITHUB SAYFASI',fg='yellow',bg='blue',font=("Arial",16),command=github).pack()
signature=Label(pencere,text="ogibalboa was here").pack()
Button(pencere,text='KAPAT',command=pencere.destroy,fg='blue',bg='yellow').pack()
pencere.config(menu=menubar) 
pencere.mainloop()


