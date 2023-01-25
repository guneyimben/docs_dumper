import urllib.request
import os
import requests

def download_file(url, destination_path):
    # URL'den dosya aç ve oku
    with urllib.request.urlopen(url) as url:
        # Hedef dizine dosyayı yaz
        with open(destination_path, 'wb') as f:
            f.write(url.read())

def download_from_wordlist(wordlist_path):
    # İndirilen dosyaların sayısını saklamak için sayaç
    counter = 0
    # Kelime listesini aç
    with open(wordlist_path, 'r') as f:
        # Her satırı oku
        for line in f:
            # Satır başı/sonu boşluklarını sil
            url = line.strip()
            # Dosya adını URL'den al
            filename = os.path.basename(url)
            # Dosyayı indir
            download_file(url, filename)
            print(f"{url} adresinden dosya indirildi")
            counter += 1
            # Sayacın 10'a ulaşıp ulaşmadığını kontrol et
            if counter % 10 == 0:
                # IP değiştir
                change_ip()

#def change_ip():
    # VPN veya proxy hizmetinden yeni bir IP iste
    #requests.get("http://your-vpn-or-proxy-service.com/change_ip")
    #print("IP adresi değiştirildi")

# Fonksiyonu örnek bir kelime listesiyle test et
wordlist_path = "links.txt"
download_from_wordlist(wordlist_path)