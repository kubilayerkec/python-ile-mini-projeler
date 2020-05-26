# Kubilay Erkeç
# kubilay@kubilay.net
# Udemy Eğitimleri: https://www.udemy.com/user/kubilay-erkec/

# armstrong sayısı: 153 -> 1*1*1 + 5*5*5 + 3*3*3 => 1 + 125 + 27 = 153

sayi = int(input("kontrol edilecek sayı: "))
toplam = 0
gecici = sayi
while gecici > 0:
    digit = gecici % 10
    toplam += digit ** 3
    gecici //= 10

if sayi == toplam:
    print("bu sayı armstrong sayısıdır")
else:
    print("bu sayı armstrong sayısı değildir")
