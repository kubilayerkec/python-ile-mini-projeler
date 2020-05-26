def kare(k):
    print("Karenin alanı: {}".format(k * k))
def dikdortgen(u,k):
    print("Dikdörtgenin alanı: {}".format(u * k))
def dikucgen(t,y):
    dikucgenAlani = (t * y) / 2
    print("Dik üçgenin alanı: {}".format(dikucgenAlani))
def paralelKenar(t,y):
    print("Paralel kenarın alanı: {}".format(t * y))

while True:
    print("""
    0: Çık
    1: Kare
    2: Diktörgen
    3: Dik Üçgen
    4: Paralel Kenar
    """)
    secim = int(input("Alanını hesaplamak istediğiniz geometrik şekli seçiniz: "))

    if secim == 1:
        kenar = int(input("Karenin bir kenarını giriniz: "))
        kare(kenar)
    elif secim == 2:
        kisakenar = int(input("Dikdörtgenin kısa kenarını giriniz: "))
        uzunkenar = int(input("Dikdörtgenin uzun kenarını giriniz: "))
        dikdortgen(uzunkenar, kisakenar)
    elif secim == 3:
        taban = int(input("Üçgenin taban uzunluğunu giriniz: "))
        yukseklik = int(input("Üçgenin yükseklik uzunluğunu giriniz: "))
        dikucgen(taban,yukseklik)
    elif secim == 4:
        taban = int(input("Paralel kenarın taban uzunluğunu giriniz: "))
        yukseklik = int(input("Paralel kenarın yüksekliğini giriniz: "))
        paralelKenar(taban,yukseklik)
    elif secim == 0:
        break