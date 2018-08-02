
"""menu:
    1-İsme göre arama yap, roket isminin sonuçlarını getir
    2-Tarihe göre arama yap, tarih aralığı veya yıl içinde olan tüm roket fırlatmalarını getir
    3-Başarı durumuna göre arama yap:
        3-1: Launch success olan roketler
        3-2: Landing success olan roketler
        3-3: Reuse success olan roketler

#kullanılacak bilgiler:
    flight_number: 1-66 arası
    mission_name: fırlatma ismi
    land_success: karaya iniş başarısı
    reused: tekrar kullanılmış mı
    reuse parts: hangi bölümleri yeniden kullanılabilmiş
    launch_date_unix: timestamp olarak fırlatma tarihi
    launch_date_utc: greenwich zamanına göre fırlatma
    launch_date_local: yerel zaman göre fırlatma

# fonksiyonlar
    load(): api dan verileri çağırma işlemi
    search (): arama fonksiyonu, sçeilen işleme göre hangi value hangi key de aranmalı
            örneğin isim seçildiyse mission_name
            tarih seçildiyse launch_date
            başarı seçildiyse
                    1- launch success
                    2- land success
                    3- reuse success

    sonuc_goster(): işleme göre sonucu gösterme fonksiyonu
                    belki başarılı ise kutlamalı, başarısız ise üzgün surat falan olabilir.



log olarak kaydedilecek kısım:
    kullanıcının seçtiği işlem
    çağrılan veri
    gösterilen veri
"""

import requests
import json

class SpaceX():
    rocket_name = None
    launch_year = None
    launch_success = None
    rockets_list = []
    data = []

    def __init__(self):
        self.session = requests.session()
        while True:
            self.menu()

    def menu(self):
        print("Welcome")
        menu = self.kontrol(input("""Please select your operation.
			            0-for exit 
                        1-Search by the rocket name 
                        2- Search by the launch year 
                        3-Search by the launch success              
                          """))

        if menu == "1":
            rocket_name = input("Please write the rocket name you want to search")
            self.name_search(rocket_name)
        elif menu == "2":
            launch_year = input("Please write the year you want to search")
            self.year_search(launch_year)
        elif menu == "3":
            success_type = self.kontrol(input("""
                        1- Show rockets with launch success
                        2- Show rockets with land success
                        3- Show rockets with reuse success
                        """))
            self.rocket_success(success_type)
        else:
            print("Error")


    def kontrol(self, key):
        if int(key.isnumeric()) and int(key)<4 and int(key)>=0 :
            return key
        else:
            key = input("Try again: ")
            return self.kontrol(key)

    def load(self):

        self.data = self.session.get('https://api.spacexdata.com/v2/launches/')
        content = self.data.content.decode("utf-8")
        self.data = json.loads(content)
        return self.data

    def name_search(self,keyword):
        self.load()
        for i in self.data:
            if i["mission_name"] == keyword:
                return self.rockets_list.append(i)

    def year_search(self,keyword):

        self.load()
        for year in self.data:
            if year['launch_year'] == keyword:
                self.rockets_list.append(year)


    def show_result(self):

        for show in self.rockets_list:
            self.rockets_list.append(SpaceX**({
                "Flight_number": self.data.get('flight_number')
            }))
            yield show

    def rocket_success(self,success_type):
        pass





space = SpaceX()

space.load()
space.show_result()
space.menu()
space.load()

