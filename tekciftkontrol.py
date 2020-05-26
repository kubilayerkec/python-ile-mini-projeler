def tekCiftKontrol(sayi):
    if((sayi % 2) == 0):
        print("sayı çift")
    else:
        print("sayı tek")

sayiKullanici = int(input("bir sayı giriniz: "))
tekCiftKontrol(sayiKullanici)