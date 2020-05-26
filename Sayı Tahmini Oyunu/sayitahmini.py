# Kubilay Erkeç
# kubilay@kubilay.net
# Udemy Eğitimleri: https://www.udemy.com/user/kubilay-erkec/

import random
uretilenSayi = random.randint(1,100)
tahminHakki = 5

while True:
    tahmin = int(input("Lütfen Tahmininizi Giriniz: "))
    if tahmin == uretilenSayi:
        print("Tebrikler! Kazandınız.")
        break
    elif tahmin > uretilenSayi:
        tahminHakki -= 1
        print("Yanlış tahmin, tahmininizi küçültünüz. ")
        print("Kalan tahmin adedi: ", tahminHakki)
    elif tahmin < uretilenSayi:
        tahminHakki -= 1
        print("Yanlış tahmin, tahmininizi büyütünüz. ")
        print("Kalan tahmin adedi: ", tahminHakki)
    if tahminHakki == 0:
        print("Hakkınız bitmiştir.", "Bilgisayarın ürettiği sayı: ", uretilenSayi)
        break