from threading import Thread
import requests
from time import time
from queue import Queue
def download_file(url,file_name):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data=response.text
        else:
            data="Errore"

        with open(file_name,'a') as file:
            file.write(data)
        print(f"Download completato per {url} e salvato in {file_name}")
    except Exception as e:
        print(f"Errore nel download di {url}: {str(e)}")

def download_serie(urls):
    start = time()
    for url,file_name in urls:
        download_file(url,"serie_"+file_name)
    end = time()
    print("Tempo di esecuzione serie ", end - start)

def worker(queue,url):
    for link,fName in url:
        a=queue.get()
        download_file(a,"thread_"+fName)
        queue.task_done()

urls=[

    ("https://jsonplaceholder.typicode.com/users","jsonPlaceHolder_serie.txt"),
    ("https://en.wikipedia.org/wiki/Main_Page","wiki_serie.txt"),
    ("https://stackoverflow.com","overFlow_serie.txt"),
    ("https://www.google.com","google_serie.txt"),
    ("https://www.youtube.com","youtube_serie.txt"),
    ("https://envato.com","envanto.txt"),
    ("http://amazon.com","envanto.txt"),
    ("http://facebook.com","envanto.txt"),
    ("http://google.com","google.txt"),
    ("http://google.fr","google.txt"),
    ("http://google.es","google.txt"),
    ("http://internet.org","internet.txt"),
    ("http://gmail.com","gmail.txt"),
    ("http://stackoverflow.com","stackoverflow.txt"),
    ("http://github.com","github.txt"),
    ("http://heroku.com","heroku.txt"),
    ("http://really-cool-available-domain.com","really-cool-available-domain.txt"),
    ( "http://djangoproject.com","djangoproject.txt"),
    ( "http://rubyonrails.org","rubyonrails.txt"),
    ( "http://basecamp.com","basecamp.txt"),
    ( "http://trello.com","trello.txt"),
    ( "http://yiiframework.com","yiiframework.txt"),
    (  "http://shopify.com","shopify.txt"),
    ( "http://another-really-interesting-domain.co","another-really-interesting-domain.txt"),
    (  "http://airbnb.com","airbnb.txt"),
    ("http://instagram.com","instagram.txt"),
    ( "http://snapchat.com","snapchat.txt"),
    ( "http://youtube.com","youtube.txt"),
    ( "http://baidu.com","baidu.txt"),
    ("http://yahoo.com","yahoo.txt"),
    ( "http://live.com","live.txt"),
    ( "http://linkedin.com","linkedin.txt"),
    ( "http://netflix.com","netflix.txt"),
    ("http://wordpress.com","wordpress.txt"),
    ( "http://bing.com","bing.txt")
]
if "__main__"==__name__:
    queue=Queue()
    start = time()
    for url, file_name in urls:
        queue.put(url,file_name)

    thread=[Thread(target=worker,args=(queue,urls,)) for _ in range(4)]

    [threads.start() for threads in thread]
    queue.join()
    end = time()
    print("Tempo di esecuzione thread ", end - start)


    download_serie(urls)
    print("Download succesfull")