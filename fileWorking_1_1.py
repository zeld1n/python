import threading
import requests
from time import time
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
        download_file(url,file_name)
    end = time()
    print("Tempo di esecuzione serie ", end - start)

def download_thread(urls):
    start=time()
    threads = []
    for url, file_name in urls:
        t = threading.Thread(target=download_file, args=(url, file_name))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()
    end=time()
    print("Tempo di esecuzione thread ",end-start)

urls=[

    ("https://jsonplaceholder.typicode.com/users","jsonPlaceHolder_serie.txt"),
    ("https://en.wikipedia.org/wiki/Main_Page","wiki_serie.txt"),
    ("https://stackoverflow.com","overFlow_serie.txt"),
    ("https://www.google.com","google_serie.txt"),
    ("https://www.youtube.com","youtube_serie.txt")
]
urls2=[
    ("https://jsonplaceholder.typicode.com/users", "jsonPlaceHolder_thread.txt"),
    ("https://en.wikipedia.org/wiki/Main_Page", "wiki_thread.txt"),
    ("https://stackoverflow.com", "overFlow_thread.txt"),
    ("https://www.google.com", "google_thread.txt"),
    ("https://www.youtube.com", "youtube_thread.txt")


]
download_serie(urls)

download_thread(urls2)




print("Download succesfull")