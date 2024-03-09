# Ogrenci-Not-Ekleme-Sistemi
 
web çerçevesi kullanarak bir web uygulaması oluşturmak 
ve kullanıcıların notlarını kaydedip bu notları işleyerek farklı sayfalarda görüntülemelerine imkan tanımaktır.


Notları Listele (/a_sayfasi): Bu sayfa, daha önce kaydedilmiş notları "a.html" adlı bir şablonda görüntüler.<br> 
Notları Gir (/b_sayfasi): Kullanıcıdan aldığı verilerle notları "sınav_dosyalari.txt" adlı dosyaya ekler. <br> 
Notları Başka Yere Kaydet (/c_sayfasi): Bu sayfa, notları başka bir dosyaya kaydetmek için kullanılır. notlari_kayitet() fonksiyonu, "sınav_dosyalari.txt"dosyasındaki notları okuyup bu notları "sonuclar.txt" adlı bir dosyaya kaydeder<br> 
Çıkış Yap (/d_sayfasi): Bu sayfa, kullanıcının uygulamadan çıkış yapmasını sağlar ve tekrar ana sayfaya yönlendirir.


##### Fonksiyonlar:
not_hesapla(satir): Bir satırdaki öğrenci adı ve notları alarak bu bilgileri kullanarak ortalama ve harf notunu hesaplar.<br> 
veri_gonder(): Veri girişi yapılan formdan alınan verileri kullanarak notları "sınav_dosyalari.txt" adlı dosyaya ekler<br> 
ortalamalari_oku(): "sınav_dosyalari.txt" dosyasındaki notları okuyarak ekrana yazdırır.
