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
GPIO.setmode(GPIO.BOARD) 
def konumsal():
    os.chdir('Programlar')
    os.system('python3 konumgonder.py')
    os.chdir("..")
def kayit():
    os.chdir('Programlar')
    os.system('python3 entrykayit.py')
    os.chdir("..")
def slider():
    os.chdir('Programlar')
    os.system('python3 slider.py')
    os.chdir("..")
        
def serkayit():
    os.chdir('Programlar')
    os.system('python3 ser_konum_kayit.py')
    os.chdir("..")
    
def github():
    onay=messagebox.askokcancel('Yönlendirme', 'SIKARHA! Github sayfasına yönlendiriliyorsunuz. Onay ?')
    if onay == True:
         webbrowser.open('https://github.com/marmara-technology/SIKAR-HA')
    else:
        return None


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

serial = Button(pencere,text = 'Serial Konum Kayıt',bg='red',fg='white',command = serkayit,font =("Arial",16)).pack()
infobtn=Button(pencere,text='GITHUB SAYFASI',fg='yellow',bg='blue',font=("Arial",16),command=github).pack()
signature=Label(pencere,text="ogibalboa was here").pack()
pencere.config(menu=menubar) 
pencere.mainloop()



