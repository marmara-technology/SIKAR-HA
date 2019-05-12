import serial

while True :
    try:
        tries=0
        if tries ==0:
            try:
              ser= serial.Serial('/dev/ttyACM0',9600)
              print("başarılı 1")
              break
            except:
                tries = 1
        if tries == 1:
            try:
                ser = serial.Serial('/dev/ttyACM1',9600)
                print("başarılı 2")
                break
            except:
                tries = 2
        if tries == 2:
            try:
                ser=serial.Serial('/dev/ttyACM2',9600)
                print("başarılı 3")
                break
            except:
                 print("HATA ! Lütfen Arduino serial kablosunu kontrol ediniz")
    except:
        print("BAŞARISIZ")

print("BAŞARILI")