import threading
import requests
import os

urls = [
    ("https://jsonplaceholder.typicode.com/users", "jsonPlaceHolder_serie.txt"),
    ("https://en.wikipedia.org/wiki/Main_Page", "wiki_serie.txt"),
    ("https://stackoverflow.com", "overFlow_serie.txt"),
    ("https://www.google.com", "google_serie.txt"),
    ("https://www.youtube.com", "youtube_serie.txt"),
    ("https://envato.com", "envanto.txt"),
    ("http://amazon.com", "envanto.txt"),
    ("http://facebook.com", "envanto.txt"),
    ("http://google.com", "google.txt"),
    ("http://google.fr", "google.txt"),
    ("http://google.es", "google.txt"),
    ("http://internet.org", "internet.txt"),
    ("http://gmail.com", "gmail.txt"),
    ("http://stackoverflow.com", "stackoverflow.txt"),
    ("http://github.com", "github.txt"),
    ("http://heroku.com", "heroku.txt"),
    ("http://really-cool-available-domain.com", "really-cool-available-domain.txt"),
    ("http://djangoproject.com", "djangoproject.txt"),
    ("http://rubyonrails.org", "rubyonrails.txt"),
    ("http://basecamp.com", "basecamp.txt"),
    ("http://trello.com", "trello.txt"),
    ("http://yiiframework.com", "yiiframework.txt"),
    ("http://shopify.com", "shopify.txt"),
    ("http://another-really-interesting-domain.co", "another-really-interesting-domain.txt"),
    ("http://airbnb.com", "airbnb.txt"),
    ("http://instagram.com", "instagram.txt"),
    ("http://snapchat.com", "snapchat.txt"),
    ("http://youtube.com", "youtube.txt"),
    ("http://baidu.com", "baidu.txt"),
    ("http://yahoo.com", "yahoo.txt"),
    ("http://live.com", "live.txt"),
    ("http://linkedin.com", "linkedin.txt"),
    ("http://netflix.com", "netflix.txt"),
    ("http://wordpress.com", "wordpress.txt"),
    ("http://bing.com", "bing.txt")
]


def download_and_analyze(url, ok_word, file_name):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.text
        else:
            data = "Errore"

        with open(file_name, 'w') as file:
            file.write(data)

        with open(file_name, "r") as myfile:
            content = myfile.read()

        if ok_word in content:
            if not os.path.exists("ok"):
                os.mkdir("ok")
            os.rename(file_name, os.path.join("ok", file_name))
        else:
            if not os.path.exists("ko"):
                os.mkdir("ko")
            os.rename(file_name, os.path.join("ko", file_name))

        print(f"Download completato per {url} e salvato")
    except Exception as e:
        print(f"Errore nel download di {url}: {str(e)}")


ok_word = input("Inserisci la parola da cercare nei file: ")

for url, file_name in urls:
    download_and_analyze(url, ok_word, file_name)

print("Download e analisi completati.")