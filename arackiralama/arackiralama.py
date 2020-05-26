# Kubilay Erkeç
# kubilay@kubilay.net
# Udemy Eğitimleri: https://www.udemy.com/user/kubilay-erkec/

class Tasit():
    def __init__(self, ID, marka, model, renk, fiyat):
        self.ID = ID
        self.Marka = marka
        self.Model = model
        self.Renk = renk
        self.Fiyat = fiyat
        self.Ozellikler = []
    def indirim(self, oran):
        self.Fiyat = self.Fiyat - (self.Fiyat / 100 * oran)

class Otomobil(Tasit):
    pass

class Minibus(Tasit):
    Surucu = ""
    def indirim(self, oran):
        if oran > 25:
            print("En fazla %25 indirim uygulanabilir.")
        else:
            self.Fiyat = self.Fiyat - (self.Fiyat / 100 * oran)
