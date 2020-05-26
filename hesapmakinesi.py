# Kubilay Erkeç
# kubilay@kubilay.net
# Udemy Eğitimleri: https://www.udemy.com/user/kubilay-erkec/

def hesapMakinesi(sayi1, sayi2, islem):
    sonuc = 0
    if islem == 1:
        sonuc = sayi1 + sayi2
    elif islem == 2:
        sonuc = sayi1 - sayi2
    elif islem == 3:
        sonuc = sayi1 / sayi2
    elif islem == 4:
        sonuc = sayi1 * sayi2
    elif islem == 5:
        sonuc = sayi1 ** sayi2
    return sonuc

print("İşlemler:","1 -> Toplama","2 -> Çıkarma", "3 -> Bölme", "4 -> Çarpma", "5 -> üs alma", sep="\n")
ilksayi = int(input("İşlem yapılacak ilk sayıyı giriniz: "))
ikincisayi = int(input("İşlem yapılacak ikinci sayıyı giriniz: "))
islem = int(input("İşlemin ne olduğunu giriniz: "))

islemsonucu = hesapMakinesi(ilksayi, ikincisayi, islem)
print("işlem sonucu: ", islemsonucu)