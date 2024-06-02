import pandas as pd
from Personel import Personel
from Doktor import Doktor
from Hemsire import Hemsire
from Hasta import Hasta
from Hasta import timedelta
def main():
    try:
        # Personel nesneleri oluşturuluyor
        personel1 = Personel(1, "Ahmet", "Yılmaz", "IT", 5000)
        personel2 = Personel(2, "Ayşe", "Demir", "HR", 6000)
        print(personel1)
        print(personel2)

        # Doktor nesneleri oluşturuluyor
        doktor1 = Doktor(3, "Mehmet", "Öz", "Cerrahi", 10000, "Genel Cerrah", 15, "Acıbadem")
        doktor2 = Doktor(4, "Selin", "Kaya", "Dahiliye", 12000, "İç Hastalıkları", 10, "Medicana")
        doktor3 = Doktor(5, "Kerem", "Sağlam", "Kardiyoloji", 11000, "Kalp Cerrahisi", 8, "Memorial")
        print(doktor1)
        print(doktor2)
        print(doktor3)

        # Hemşire nesneleri oluşturuluyor
        hemsire1 = Hemsire(6, "Elif", "Çelik", "Acil", 7000, 40, "BLS", "Acıbadem")
        hemsire2 = Hemsire(7, "Burcu", "Altun", "Yoğun Bakım", 7500, 36, "ACLS", "Medicana")
        hemsire3 = Hemsire(8, "Canan", "Yıldız", "Pediatri", 7300, 38, "PALS", "Memorial")
        print(hemsire1)
        print(hemsire2)
        print(hemsire3)

        # Hasta nesneleri oluşturuluyor
        hasta1 = Hasta(1, "Ali", "Vural", "1995-04-15", "Grip", "İlaç Tedavisi")
        hasta2 = Hasta(2, "Zeynep", "Kara", "1989-08-20", "Kırık", "Fizik Tedavi")
        hasta3 = Hasta(3, "Deniz", "Aydın", "1992-12-01", "Baş Ağrısı", "Dinlenme")
        print(hasta1)
        print(hasta2)
        print(hasta3)

        # Tüm nesnelerin bilgileriyle bir DataFrame oluşturuluyor
        data = [
            [personel1.get_personel_no(), personel1.get_ad(), personel1.get_soyad(), personel1.get_departman(), personel1.get_maas(), None, None, None, None, None, None, None, None, None, None],
            [personel2.get_personel_no(), personel2.get_ad(), personel2.get_soyad(), personel2.get_departman(), personel2.get_maas(), None, None, None, None, None, None, None, None, None],
            [doktor1.get_personel_no(), doktor1.get_ad(), doktor1.get_soyad(), doktor1.get_departman(), doktor1.get_maas(), doktor1.get_uzmanlik(), doktor1.get_deneyim_yili(), doktor1.get_hastane(), None, None, None, None, None, None],
            [doktor2.get_personel_no(), doktor2.get_ad(), doktor2.get_soyad(), doktor2.get_departman(), doktor2.get_maas(), doktor2.get_uzmanlik(), doktor2.get_deneyim_yili(), doktor2.get_hastane(), None, None, None, None, None, None],
            [doktor3.get_personel_no(), doktor3.get_ad(), doktor3.get_soyad(), doktor3.get_departman(), doktor3.get_maas(), doktor3.get_uzmanlik(), doktor3.get_deneyim_yili(), doktor3.get_hastane(), None, None, None, None, None, None],
            [hemsire1.get_personel_no(), hemsire1.get_ad(), hemsire1.get_soyad(), hemsire1.get_departman(), hemsire1.get_maas(), None, None, None, hemsire1.get_calisma_saati(), hemsire1.get_sertifika(), hemsire1.get_hastane(), None, None, None],
            [hemsire2.get_personel_no(), hemsire2.get_ad(), hemsire2.get_soyad(), hemsire2.get_departman(), hemsire2.get_maas(), None, None, None, hemsire2.get_calisma_saati(), hemsire2.get_sertifika(), hemsire2.get_hastane(), None, None, None],
            [hemsire3.get_personel_no(), hemsire3.get_ad(), hemsire3.get_soyad(), hemsire3.get_departman(), hemsire3.get_maas(), None, None, None, hemsire3.get_calisma_saati(), hemsire3.get_sertifika(), hemsire3.get_hastane(), None, None, None],
            [None, hasta1.get_ad(), hasta1.get_soyad(), None, None, None, None, None, None, None, None, hasta1.get_hasta_no(), hasta1.get_dogum_tarihi(), hasta1.get_hastalik(), hasta1.get_tedavi()],
            [None, hasta2.get_ad(), hasta2.get_soyad(), None, None, None, None, None, None, None, None, hasta2.get_hasta_no(), hasta2.get_dogum_tarihi(), hasta2.get_hastalik(), hasta2.get_tedavi()],
            [None, hasta3.get_ad(), hasta3.get_soyad(), None, None, None, None, None, None, None, None, hasta3.get_hasta_no(), hasta3.get_dogum_tarihi(), hasta3.get_hastalik(), hasta3.get_tedavi()]
        ]

        df = pd.DataFrame(data, columns=[
            'personel_no', 'ad', 'soyad', 'departman', 'maas', 'uzmanlik', 'deneyim_yili', 'hastane',
            'calisma_saati', 'sertifika', 'hastane', 'hasta_no', 'dogum_tarihi', 'hastalik', 'tedavi'
        ])

        # Boş değerlerin 0 ile doldurulması
        df.fillna({'dogum_tarihi': 0, 'departman': 0, 'maas': 0, 'uzmanlik': 0, 'deneyim_yili': 0, 'hastane': 0, 'calisma_saati': 0, 'sertifika': 0, 'hasta_no': 0, 'hastalik': 0, 'tedavi': 0}, inplace=True)

        # Doğum tarihi sütununu datetime tipine dönüştürme
        df['dogum_tarihi'] = pd.to_datetime(df['dogum_tarihi'])

        # Doktorları uzmanlık alanlarına göre gruplandırma ve sayma
        doktor_uzmanlik_gruplari = df[df['uzmanlik'] != 0 ].groupby('uzmanlik').size()
        print("\nUzmanlık alanlarına göre doktor sayıları:")
        print(doktor_uzmanlik_gruplari)

        # 5 yıldan fazla deneyime sahip doktorların sayısını bulma
        deneyimli_doktorlar = df[(df['deneyim_yili'] > 5) & (df['deneyim_yili'] != 0)]
        print(f"\n5 yıldan fazla deneyime sahip doktorların sayısı: {len(deneyimli_doktorlar)}")

        # Hasta adına göre alfabetik sıralama
        hasta_df = df[df['hasta_no'] != 0]
        hasta_df_sıralanması = hasta_df.sort_values(by='ad')
        print("\nAlfabetik sıraya göre hastalar:")
        print(hasta_df_sıralanması[['hasta_no', 'ad', 'soyad']])

       

        # Maaşı 7000 TL üzerinde olan personeller
        yuksek_maas_personeller = df[(df['maas'] > 7000) & (df['maas'] != 0)]
        print("\nMaaşı 7000 TL üzerinde olan personeller:")
        print(yuksek_maas_personeller[['personel_no', 'ad', 'soyad', 'departman', 'maas']])

        # 1990 ve sonrası doğumlu hastalar
        yeni_dogumlu_hastalar = df[df['dogum_tarihi'] >= '1990-01-01']
        print("\n1990 ve sonrası doğumlu hastalar:")
        print(yeni_dogumlu_hastalar[['hasta_no', 'ad', 'soyad', 'dogum_tarihi']])

        # Yeni DataFrame oluşturma
        yeni_df = df[['ad', 'soyad', 'departman', 'maas', 'uzmanlik', 'deneyim_yili', 'hastalik', 'tedavi']]
        print("\nYeni DataFrame:")
        print(yeni_df)
        
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

if __name__ == "__main__":
    main()
