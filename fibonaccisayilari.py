# 0 1 1 2 3 5 8 13 21 34 ... -> 10 tanesi
# kubilay@kubilay.net

kacTane = int(input("kaç tane fibonacci sayısı gösterilsin: "))

if kacTane <= 0:
    raise ValueError("girilen sayı sıfır ve sıfırdan küçük olamaz!")

ilkdeger = 0
ikincideger = 1
say = 0

while say < kacTane:
    print(say + 1, ilkdeger, sep= " = ")
    yenideger = ilkdeger + ikincideger
    ilkdeger = ikincideger
    ikincideger = yenideger
    say += 1