import random
import time

kullanici1Skor = 0
kullanici2Skor = 0

while True:
    kullanici1 = random.randint(1,6)
    print("Kullanıcı 1: ", kullanici1)
    time.sleep(1)
    kullanici2 = random.randint(1,6)
    print("Kullanıcı 2: ", kullanici2)
    time.sleep(1)
    if kullanici1 > kullanici2:
        print("Kullanıcı 1 kazandı.")
        kullanici1Skor += 1
    elif kullanici2 > kullanici1:
        print("Kullanıcı 2 kazandı.")
        kullanici2Skor += 1
    else:
        print("Berabere bitti.")

    #Kullanıcı 1 : 5 - 3 : Kullanıcı 2
    if kullanici1Skor == 5 or kullanici2Skor == 5:
        print("Kullanıcı 1 :",kullanici1Skor, " - ", kullanici2Skor, ": Kullanıcı 2")
        break