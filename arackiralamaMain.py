import arackiralama
araclar = []
kasa = 0

def aracEkle():
    ID = int(input("Aracın ID'sini giriniz: "))
    marka = input("Aracın markasını giriniz: ")
    model = input("Aracın modelini giriniz: ")
    renk = input("Aracın rengini giriniz: ")
    fiyat = int(input("Aracın fiyatını giriniz: "))
    otomobil = arackiralama.Otomobil(ID, marka,model, renk, fiyat)
    araclar.append(otomobil)

def minibusEkle():
    ID = int(input("Minibüsün ID'sini giriniz: "))
    marka = input("Minibüsün markasını giriniz: ")
    model = input("Minibüsün modelini giriniz: ")
    renk = input("Minibüsün rengini giriniz: ")
    fiyat = int(input("Minibüsün fiyatını giriniz: "))
    minibus = arackiralama.Minibus(ID, marka,model, renk, fiyat)
    minibus.Surucu = "Hasan Tahsin"
    araclar.append(minibus)

def aracFiyatGuncelle(ID, YeniFiyat):
    IDS = [i.ID for i in araclar]
    if ID in IDS:
        for arac in araclar:
            if ID == arac.ID:
                arac.Fiyat = YeniFiyat
                print("{} id numaralı aracın yeni fiyatı: {}".format(arac.ID, YeniFiyat))
    else:
        print("Bu ID değerine sahip araç bulunamadı")

def aracKirala(ID):
    global kasa
    IDS = [i.ID for i in araclar]
    if ID in IDS:
        for arac in araclar:
            if ID == arac.ID:
                kasa += arac.Fiyat
    else:
        print("Bu ID değerine sahip araç bulunamadı")

while True:
    print("ARAÇ KİRALAMA PROGRAMI:")
    print(
        "0: Programdan Çık",
        "1: Otomobil Ekle",
        "2: Minibus Ekle",
        "3: Araçları Listele",
        "4: Araç Fiyatı Güncelle",
        "5: Aracı Kiraya Ver",
        "6: Kasayı Göster",
        sep="\n")
    secim = int(input("Seçiminizi giriniz:"))
    if secim == 0:
        break
    elif secim == 1:
        aracEkle()
    elif secim == 2:
        minibusEkle()
    elif secim == 3:
        for arac in araclar:
            print(arac.Marka, arac.Model, arac.Fiyat, arac.Renk)
    elif secim == 4:
        ID = int(input("Değişiklik yapmak istediğiniz aracın ID değerini giriniz: "))
        yeniFiyat = int(input("Aracın yeni fiyatını giriniz: "))
        aracFiyatGuncelle(ID, yeniFiyat)
    elif secim == 5:
        ID = int(input("Kiraya verilen aracın ID değerini giriniz: "))
        aracKirala(ID)
    elif secim == 6:
        print("Kasa: ", kasa)