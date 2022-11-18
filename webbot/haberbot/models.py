from django.db import models
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import re
import requests

# Create your models here.


class bot(models.Model):
    chromeAyarlar = webdriver.ChromeOptions()

    chromeAyarlar.add_argument("--incognito")


    ## hızlandırmak için bazı ayarlar

    chromeAyarlar.headless = True  # browser arkada çalışır bu sayede görüntü gösterilmez ve sistem kaynaklarından tasarruf sağlanır
    prefs = {"profile.managed_default_content_settings.images": 2}  # imajlar yüklenmez ve bu sayede bantgenişliğinden tasarruf sağlanır
    chromeAyarlar.add_experimental_option("prefs", prefs)


    driver = webdriver.Chrome(options=chromeAyarlar)
    # driver.maximize_window() #pencereyi tam ekran yapmak için komut
    # driver.delete_all_cookies() #çerezleri silmek için kullanılan komut

    # üstteki yoruma alınan satırlar gereksiz


    driver.get("https://www.aa.com.tr/tr/gundem")
    driver.implicitly_wait(10) #10 saniye gecikme beklemesi yapar eğer on saniyeden önce site açılırsa işleme başlamasını sağlayan kod



    urlKategori = ["dunya","ekonomi","spor","analiz","kultur","podcast"]

    liste = []

    i = 0 

        
    for kategori in urlKategori:
        driver.get(f"https://www.aa.com.tr/tr/{kategori}")
        htmlCode = driver.page_source
        soup = BeautifulSoup(htmlCode, "html.parser") 

        mansetler = soup.find_all('h4')  # site yapısı incelendiğinde manşetlerin h4 tagi içinde olduğu görülmektedir
        for manset in mansetler:
            liste.append(
                    {'url': manset.parent['href'],  # h4 a taginin içinde olduğu için parent elemente gidip linki alıyoruz
                    'baslik': manset.text})

    print(liste)

