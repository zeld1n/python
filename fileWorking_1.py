import threading
import requests

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


urls=[

    ("https://jsonplaceholder.typicode.com/users","jsonPlaceHolder.txt"),
    ("https://en.wikipedia.org/wiki/Main_Page","wiki.txt"),
    ("https://stackoverflow.com","overFlow.txt")
]

threads=[]
for url,file_name in urls:
    t=threading.Thread(target=download_file, args=(url,file_name))
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

print("Download succesfull")