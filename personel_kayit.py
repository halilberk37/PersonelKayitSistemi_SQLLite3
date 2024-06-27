import sqlite3


def listele():
    veriler = baglanti.cursor().execute("SELECT * from Kayit")
    print(veriler.fetchall())
    baglanti.commit()
    baglanti.close()

def ekle(Psno,Padsoy,Pbol,Pmaas,Pyil):
    con = baglanti.cursor()
    con.execute("insert into Kayit values(?,?,?,?,?)",(Psno,Padsoy,Pbol,Pmaas,Pyil))
    baglanti.commit()
    baglanti.close()
    print("Kayıt işlemi gerçekleşti")

def sil(sno):
    conn = baglanti.cursor()
    conn.execute("Delete from Kayit where psicilno=?",(sno,))
    baglanti.commit()
    baglanti.close()
    print("Kayıt Başarı ile silindi")

Menu = """

1-KAYIT EKLE
2-KAYITLARI LİSTELE
3-KAYIT SİL

"""

baglanti = sqlite3.connect("C:/Users/halil/Desktop/Yazılım ve Tasarım/Python Main/Personel Takip Project SQLite3/personel_bilgi.db")

if baglanti:
    print("bağlantı başarılı")
else:
    print("Bağlantı başarısız")

print(Menu)
print("Lütfen bir seçenek seçiniz")
islem_no = int(input())

if (islem_no==1):
    Psno = input("personel SicilNo Giriniz:")
    Padsoy = input("personel Adı Soyadı Giriniz:")
    Pbol = input("personel bölüm Giriniz:")
    Pmaas = float(input("personel Maaş Giriniz:"))
    Pyil = int(input("personel Yıl Giriniz:"))

    ekle(Psno,Padsoy,Pbol,Pmaas,Pyil)
elif (islem_no==2):
    listele()
elif (islem_no==3):
    sno = int(input("Silinecek Personel Sicil Noyu Giriniz"))
    sil(sno)