# Kubilay Erkeç
# kubilay@kubilay.net
# Udemy Eğitimleri: https://www.udemy.com/user/kubilay-erkec/

def Faktoriyel(sayi):
    faktoriyel = 1;
    if sayi < 0:
        raise ValueError("Sayı negatif girilemez")
    elif sayi == 0:
        raise ValueError("Faktoriyel hesabında sıfır değeri girilemez")
    else:
        for i in range(1, sayi + 1):
            faktoriyel = faktoriyel * i
    return faktoriyel

try:
    sayi = int(input("Hesap yapılacak sayıyı giriniz: "))
    print(Faktoriyel(sayi))
except Exception as ex:
    print("HATA: ", ex)