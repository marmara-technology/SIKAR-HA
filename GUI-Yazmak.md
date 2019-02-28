--TR--
Robotu kontrol etmek için GUI yazmaya başladık. GUI nedir sorusunun yanıtını öncelikle google aracılığıyla öğrenmelisiniz.
GUI nedir biliyorsanız devam edelim.
Python da GUI yazmak için Tkinter kullanılır. Şimdi de Tkinter nasıl kullanılır onu öğrenmemiz gerekmekte. 
Bunun içn şu site yardımcı olacaktır:  http://www.getgnu.org/gnulinux/gnulinux-ipuclari/python-gui-examples-tkinter-tutorial.html

---> Tkinter kullanarak bir arayüz oluşturduk. Bu arayüzde Entry komutunu kullandık. Entry komutu tkinterin kullanıcıdan 
giriş bilgisi almayı sağlıyor
Yazdığımız bu gui de alınan bilgi SetAngle fonksiyonunda kullanılıyor. Bu bilgi integer veri tipinde olmalı.
Aksi halde matematiksel işlemden geçip PWM duty değerine yazılamaz. Ancak bu kısımda bir sorunumuz var.
Çünkü Entry komutu kullanıcıdan string veritipinde bilgi alıyor. Bu veriyi integer a çevirmemiz gerekiyor.
Konsoldan int kullanıcı girişini nasıl alıyorduk ? int(input("Bir sayi yazin")). Aynı yöntemi Entry den denediğimizde :
int(sayi.get()) . Bu komut hata veriyor. İnternette derin araştırmalar yapmama rağmen bir türlü tkinter GUI den integer veri
alma yöntemini bulamamıştım. En sonunda bir forum sitesinden ( kim olduğunu keşke kaydetseydim) bir kişinin yazdığı çözümü buldum :
int(str(sayi.get())) . Sonunda veri integer'a çevirildi. Artık bu veriyi SetAngle fonksiyonuna yerleştirebiliriz.
