# SIKAR HA! GELİŞTİRİCİ GÜNLÜKLERİ
# --TR--
versiyon 0.0.1 26 Şubat 2019 / Servoya açı parametresi verilip kaydedilir ve servonun "0" pozisyonundan kayıtlı pozisyona döngüde olması sağlanır.

## Update- v0.0.2 28 Şubat 2019
"SIKAR HA!" için GUI yazmaya başladık. İlk hali ControlPanelv1 dosyasındadır. Açıklamaları GUI adlı branch'dan bulabilirsiniz.

## Update v0.0.3 4 Mart 2019 
GUI temel fonksiyonları yerine getirmek üzere kodlandı. "ControlPanelv1.2". 
İerlemeye devam etmeden önce robotun mekanik kısmına çalışmak gerekiyor.
Mekanik kısım tamamlandıktan sonra yeni bir güncelleme ile görüşmek üzere.

## Update v0.0.4 10 Mart 2019
Robotun mekanik parçaları geldi. GUI'de şu değişiklikler yapıldı : 
1. Menu toolbar eklendi.
1. Mainmenu düzenlendi, github sayfa linki koyuldu.
1. Slider ile konum bilgisi gönderme penceresi eklendi.
1. Diğer menü fonksiyonları için taslaklar oluşturuldu.
          
## Update v0.1.0 26 Mart 2019
Yeni sürüm ! Daha öncelerde robotu RasPi kullanarak hareket ettirdik. Şimdi ise Arduino'yu bir motor
sürücü gibi kullanarak robotumuzu kontrol edeceğiz. Bu yeni kontrol programında öncelikle Arduino'yu potla robotu kontrol
etmek üzere kodluyoruz. Bu kodlar repodaki " Arduino Motor Sürme " adlı dosyada bulunmakta. 
Arduino kodları basit bir pot ile servo kontrol etme kodlarıdır. Ancak bundan farklı olarak Serial heaberleşme ile RasPi ye 
motorların konum bilgilerini gönderiyoruz. 
#### Bunun için şöyle bir algoritma gerçekleştirdik :
1. Arduino kayıt butonuna basıldığında 4 motordan 4 farklı bilgiyi Raspi ye gönderecek.
2. Raspi ise bu 4 bilgiyi motorlar için oluşturduğumuz register değişkenlerine aktaracak.
 Bunu gerçekleştirmek için iki kontrolcü arasında senkronizasyonu doğru sağlamış olmamız gerekiyor. 
 Yazdığımız kodda senkronizasyon sağlamak için Raspi ye counter değeri yazdık. Bu sayıcı arduinodan gelen bilgi sayısını kontrol
 edecek böylece gelen bilgiler sırayla ve birbirine karışmadan registerlara aktarılacak:
Arduino - Motorun açı değerini gönder delay(100) saniye bekle Raspi- ilk bilgiyi registera yaz ve sayıcıyı 1 arttır.

## Update v0.1.1 27 Nisan 2019
Bu zamana kadar robotu potansiyometre ile kontrol etmiştik. Artık robotu daha kolay kontrol etmek ve daha ince hareketleri gerçekleştirmek üzere Joystick kullanacağız ! Robotu joystick ile kontrol etmek için hala Arduino'yu bir motor sürücü olarak kullanıyoruz. Bununla beraber motorların pozisyonlarını da serial port aracılığıyla Raspberry Pi üzerine aktarıyoruz. Sonraki güncelleme de bu pozisyonları işlemek üzere kullanacağız. !
