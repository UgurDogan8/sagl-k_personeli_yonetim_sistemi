from datetime import  timedelta

class Hasta:
    def __init__(self, hasta_no, ad, soyad, dogum_tarihi, hastalik, tedavi):
        self.__hasta_no = hasta_no
        self.__ad = ad
        self.__soyad = soyad
        self.__dogum_tarihi = dogum_tarihi
        self.__hastalik = hastalik
        self.__tedavi = tedavi

    def get_hasta_no(self):
        return self.__hasta_no

    def set_hasta_no(self, hasta_no):
        self.__hasta_no = hasta_no

    def get_ad(self):
        return self.__ad

    def set_ad(self, ad):
        self.__ad = ad

    def get_soyad(self):
        return self.__soyad

    def set_soyad(self, soyad):
        self.__soyad = soyad

    def get_dogum_tarihi(self):
        return self.__dogum_tarihi

    def set_dogum_tarihi(self, dogum_tarihi):
        self.__dogum_tarihi = dogum_tarihi

    def get_hastalik(self):
        return self.__hastalik

    def set_hastalik(self, hastalik):
        self.__hastalik = hastalik

    def get_tedavi(self):
        return self.__tedavi

    def set_tedavi(self, tedavi):
        self.__tedavi = tedavi

    def tedavi_suresi_hesapla(self):
        # Basit bir örnek: Bağışıklık sistemini güçlendirici ilaçlar için 14 gün, ameliyatlar için 30 gün süre verelim
        if self.__hastalik == "grip":
            return timedelta(days=14)
        elif self.__hastalik == "kırık":
            return timedelta(days=30)
        else:
            return timedelta(days=10)  # Varsayılan olarak 7 gün süre verelim

    def __str__(self):
        return f'Hasta No: {self.__hasta_no}, Ad: {self.__ad}, Soyad: {self.__soyad}, Dogum Tarihi: {self.__dogum_tarihi}, Hastalik: {self.__hastalik}, Tedavi: {self.__tedavi}'
