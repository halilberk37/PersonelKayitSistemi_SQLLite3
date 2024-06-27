# PersonelKayitSistemi_SQLLite3
 
Personel Takip Uygulaması
Bu uygulama, SQLite3 veritabanı kullanarak personel bilgilerini takip etmek amacıyla oluşturulmuştur. Uygulama, kullanıcıların personel bilgilerini eklemelerine, listelemelerine ve silmelerine olanak tanır. Projenin temel işlevleri Python ile yazılmıştır.

İçindekiler
Özellikler
Kurulum
Kullanım
Veritabanı Yapısı
Fonksiyonlar
Geliştirme ve Katkı

Özellikler
Kayıt Ekleme: Yeni personel bilgilerini veritabanına ekleme.
Kayıt Listeleme: Mevcut personel kayıtlarını listeleme.
Kayıt Silme: Veritabanından personel kayıtlarını silme.
Kurulum
Python'u İndirin ve Kurun: Proje Python 3 gerektirir. Python web sitesinden en son sürümü indirin ve kurun.

Gerekli Kütüphaneleri Kurun: Bu proje sqlite3 kütüphanesini kullanır. Python ile birlikte gelir, bu nedenle ekstra bir yükleme gerekmez.

Proje Dosyalarını İndirin: Bu projeyi kendi bilgisayarınıza klonlayın veya indirin.
git clone https://github.com/kullanici_adiniz/personel-takip-uygulamasi.git

Veritabanı Dosyasını Kontrol Edin: Uygulama, belirtilen yolda personel_bilgi.db adlı bir veritabanı dosyasını kullanır. Bu dosyanın doğru yerde olduğundan emin olun.
Kullanım
Uygulamayı Başlatın: Python dosyasını çalıştırarak uygulamayı başlatın.

python personel_takip.py
Menüden Bir Seçenek Seçin: Uygulama çalıştırıldığında, aşağıdaki menü ile karşılaşacaksınız:

1-KAYIT EKLE
2-KAYITLARI LİSTELE
3-KAYIT SİL
Kayıt Ekleme: 1 seçeneğini seçerek yeni bir personel kaydı ekleyin. Sizden sırasıyla personel sicil numarası, adı soyadı, bölümü, maaşı ve yılı girmeniz istenecektir.

Kayıtları Listeleme: 2 seçeneğini seçerek mevcut personel kayıtlarını listeleyin.

Kayıt Silme: 3 seçeneğini seçerek personel kayıtlarını sicil numarasına göre silin.

Veritabanı Yapısı
Veritabanı, Kayit adında bir tablo içerir. Bu tablo, aşağıdaki sütunlara sahiptir:

psicilno (INTEGER): Personelin sicil numarası.
padsoy (TEXT): Personelin adı ve soyadı.
pbol (TEXT): Personelin çalıştığı bölüm.
pmaas (REAL): Personelin maaşı.
pyil (INTEGER): Personelin çalışmaya başladığı yıl.
Fonksiyonlar
ekle(Psno, Padsoy, Pbol, Pmaas, Pyil): Yeni bir personel kaydı ekler.
listele(): Mevcut tüm personel kayıtlarını listeler.
sil(sno): Belirtilen sicil numarasına sahip personel kaydını siler.
Kod Açıklamaları
ekle Fonksiyonu
Bu fonksiyon, yeni bir personel kaydı eklemek için kullanılır. Psno, Padsoy, Pbol, Pmaas ve Pyil parametreleri, sırasıyla personel sicil numarası, adı soyadı, bölümü, maaşı ve çalışmaya başladığı yılı temsil eder.

def ekle(Psno, Padsoy, Pbol, Pmaas, Pyil):
    con = baglanti.cursor()
    con.execute("insert into Kayit values(?,?,?,?,?)", (Psno, Padsoy, Pbol, Pmaas, Pyil))
    baglanti.commit()
    baglanti.close()
    print("Kayıt işlemi gerçekleşti")
listele Fonksiyonu
Bu fonksiyon, veritabanındaki mevcut personel kayıtlarını listeler ve ekrana bastırır.

def listele():
    veriler = baglanti.cursor().execute("SELECT * from Kayit")
    print(veriler.fetchall())
    baglanti.commit()
    baglanti.close()
    
sil Fonksiyonu
Bu fonksiyon, belirtilen sicil numarasına sahip personel kaydını veritabanından siler.
def sil(sno):
    conn = baglanti.cursor()
    conn.execute("Delete from Kayit where psicilno=?", (sno,))
    baglanti.commit()
    baglanti.close()
    print("Kayıt Başarı ile silindi")
Geliştirme ve Katkı
Bu projeye katkıda bulunmak isterseniz aşağıdaki adımları takip edebilirsiniz:

Bu projeyi fork edin.
Kendi dalınızı (feature/harika-ozellik) oluşturun.
Yaptığınız değişiklikleri dalınıza (git checkout -b feature/harika-ozellik) ekleyin.
Değişikliklerinizi commitleyin (git commit -m 'Harika bir özellik ekledim').
Dalınıza pushlayın (git push origin feature/harika-ozellik).
Bir Pull Request oluşturun.
