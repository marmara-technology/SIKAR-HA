import webbrowser
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

def Arduino():
    
    arduino=Tk()
    arduino.title('ROBOTU KONUMLANDIRINIZ')
    arduino.geometry('500x500')
    Label(arduino,text='Robotu konumlandırdıktan sonra kayıt butonuna basın').grid(column=0,row=0)
    ser= serial.Serial('/dev/ttyACM1',9600)
    print('Selamalekum')
    global counter
    counter = 0
    while 1:
        if (ser.in_waiting>0 and counter==0):
            base=int(ser.readline())
            counter=1
         
        if (ser.in_waiting>0 and counter==1):
            yatay = int(ser.readline())
            counter=2
        if (ser.in_waiting>0 and counter==2):
            dikey = int(ser.readline())
            counter = 3
        if (counter==3):
            messagebox.showinfo(' KAYIT TAMAMLANDI',' Alınan açılar : '+ base+yatay+dikey)
            counter = 0
            break
        


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
editmenu.add_command(label="Arduino", command=Arduino)
editmenu.add_command(label="Pot ile", command=donothing)

kayitmenu= Menu(menubar, tearoff=0)
kayitmenu.add_command(label="Hareket Kaydet",command=kayit)
menubar.add_cascade(label="Kayit",menu=kayitmenu)
menubar.add_cascade(label="Hareket", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Hareket?", command=donothing)
helpmenu.add_command(label="Hakkında", command=donothing)
menubar.add_cascade(label="Yardım", menu=helpmenu)


#Başlık
pencere.title("SIKAR HA Control Panel")
pencere.geometry('550x170')
lbl = Label(pencere, text="SIKAR HA! CONTROL PANEL",fg='blue',bg='yellow',font=("Arial Bold",24)).pack()
def github():
    onay=messagebox.askokcancel('Yönlendirme', 'SIKARHA! Github sayfasına yönlendiriliyorsunuz. Onay ?')
    if onay == True:
         webbrowser.open('https://github.com/OgiBalboa/servo')
    else:
        return None
   
def serkayit():
    os.system('python3 ser_konum_kayit.py')
serial = Button(pencere,text = 'Serial Konum Kayıt',bg='red',fg='white',command = serkayit,font =("Arial",16)).pack()
infobtn=Button(pencere,text='GITHUB SAYFASI',fg='yellow',bg='blue',font=("Arial",16),command=github).pack()
signature=Label(pencere,text="ogibalboa was here").pack()
pencere.config(menu=menubar) 
pencere.mainloop()



