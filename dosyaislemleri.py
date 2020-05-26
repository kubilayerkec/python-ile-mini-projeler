from datetime import datetime

def kayitEkle(metin):
    dosya = open("c:\\pythonlog\\{}.txt".format(
        datetime.strftime(datetime.today(),"%Y-%m-%d")
    ),"a")
    metin = metin + "\n"
    dosya.write(metin)
    dosya.close()

def kayitlariOku():
    dosya = open("c:\\pythonlog\\{}.txt".format(
        datetime.strftime(datetime.today(),"%Y-%m-%d")
    ),"r")
    dosyaicerigi = dosya.read()
    print(dosyaicerigi)
    dosya.close()

def logKaydi(log, userid):
    metin = "{} -> ({}) {}".format(
        datetime.strftime(datetime.today(),"%Y-%m-%d %H:%M:%S"),
        userid,
        log)
    kayitEkle(metin)

try:
    print(15/0)
except Exception as ex:
    logKaydi("HATA: {}".format(ex), 5)