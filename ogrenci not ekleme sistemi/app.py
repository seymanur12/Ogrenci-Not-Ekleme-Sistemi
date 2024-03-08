from flask import Flask, render_template,request
import webbrowser
app = Flask(__name__)
@app.route('/')
def ana_sayfa():
    return render_template('w.html')








#! bütün kayitli olan notlari yazdirir : başka bi yere kaydettiğimiz yerden yazsın :
@app.route('/a_sayfasi')
def a_sayfasi():
    webbrowser.open_new_tab('a.html') 
    ortalamalari_oku()
    return render_template('a.html')


def ortalamalari_oku():
    
    """ dosya içeriğini ekranda görmek için"""
    with open("sınav_dosyalari.txt","r",encoding="utf") as file:
        """file üzerinden dosyaya ulaşcaz"""
        """ file içerisinden gelen her satiri tek tek alcaz"""
        for satir in file:
            """ okuduğumuz her satiri not_hesapla() fonksiyonuna göndercez"""
            print(not_hesapla(satir))

#! Notlari gir : ogr adı : soyadı : not1 : not2 : not3 ------------------------
@app.route('/b_sayfasi')
def b_sayfasi():
    webbrowser.open_new_tab('b.html')  
    return render_template('b.html')

@app.route('/veri_gonder', methods=['POST'])
def veri_gonder():
    veri1 = request.form.get('veri1')
    veri2 = request.form.get('veri2')
    veri3 = request.form.get('veri3')
    veri4 = request.form.get('veri4')
    veri5 = request.form.get('veri5')

    with open("sınav_dosyalari.txt", "a",encoding="utf-8") as file:
        # dosya içine bu şekilde yaz 
        file.write( veri1 + '  ' + veri2 + ':' + veri3 +',' + veri4 + ','+ veri5 +'\n')

    # Burada alınan verileri kullanarak istediğiniz işlemleri gerçekleştirin
    # Örneğin, bir veritabanına kaydedebilirsiniz

    # Ardından, belirlediğiniz hedef sayfasına yönlendirme yapın (örneğin, a.html)
    return render_template('v.html')
   

#!--------------------------------------------------------------------------
"""if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)"""




#! Notlari Başka bi yere kayit etsin.....................
@app.route('/c_sayfasi')
def c_sayfasi():
    webbrowser.open_new_tab('c.html')  
    notlari_kayitet()
    return render_template('c.html')


def notlari_kayitet(): #* başka bir dosyaya kayit edicez
      """ her bir listeyi 
      her satiri döngü ile  liste içine aticaz"""
      with open('sınav_dosyalari.txt',"r",encoding="utf-8") as y:
        liste = []

        for i in y:
            liste.append(not_hesapla(i)) 

        with open("sonuclar.txt", "w",encoding="utf-8") as file2:
          """ w moduyla açicaz dosyaya yazma işlemi yapicaz"""
          for i in liste:
              file2.write(i)  
def not_hesapla(satir):
    """ isim bilgisi not bilgisi alcak"""
    """ notlari virgülle birbirinden ayircak"""
    """ """
    satir = satir[:-1]
    """ : ayir 1. index isim   2. index notlar olur"""
    liste = satir.split(':')
    print(liste[0])
    print(liste[1])
    ogrenciAdi = liste[0]
    notlar = liste [1].split(',')

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ortalama = (not1+not1+not3)/3


    if ortalama >= 90 and ortalama <=100:
        harf ="AA"

    elif ortalama >= 85 and ortalama <= 89:
        harf = "BA"
    elif ortalama >=65 :
        harf =" CC"
    else:
        harf = "FF"

    return ogrenciAdi + ":"+ harf + "\n"












#! çıkış yap : ana sayfaya atsın : her sayfada olucak 
@app.route('/d_sayfasi')
def d_sayfasi():
    webbrowser.open_new_tab('d.html') 
    return render_template('w.html')

if __name__ == "__main__":
    webbrowser.open_new('http://127.0.0.1:5000/')
    app.run()
