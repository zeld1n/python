siti_web = [
    'https://envato.com',
    'http://amazon.com',
    'http://facebook.com',
    'http://google.com',
    'http://google.fr',
    'http://google.es',
    'http://internet.org',
    'http://gmail.com',
    'http://stackoverflow.com',
    'http://github.com',
    'http://heroku.com',
    'http://really-cool-available-domain.com',
    'http://djangoproject.com',
    'http://rubyonrails.org',
    'http://basecamp.com',
    'http://trello.com',
    'http://yiiframework.com',
    'http://shopify.com',
    'http://another-really-interesting-domain.co',
    'http://airbnb.com',
    'http://instagram.com',
    'http://snapchat.com',
    'http://youtube.com',
    'http://baidu.com',
    'http://yahoo.com',
    'http://live.com',
    'http://linkedin.com',
    'http://yandex.ru',
    'http://netflix.com',
    'http://wordpress.com',
    'http://bing.com',
]
import requests
import time
from multiprocessing import Process, current_process
from threading import Thread
from queue import Queue


def effettua_request(url):
    try:
        response = requests.get(url)  # Effettua la richiesta GET all'URL specificato
        response.raise_for_status()  # Solleva un'eccezione in caso di errore nella risposta
        #print("Risposta:", response.text)  # Stampa il contenuto della risposta
        print("OK ",url)
    except requests.exceptions.RequestException as e:
        print("Errore durante la richiesta:", e)

def esecuzione1Processo1url(siti_web):
    startTime=time.time()
    

    processes = []
    for url in siti_web:
        process = Process(target=effettua_request, args=(url,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    endTime=time.time()
    print("Tempo di esecuzione: ",endTime-startTime)

def esecuzioneinserio(siti_web):
    startTime=time.time()
    for i in range(len(siti_web)):
        effettua_request(siti_web[i])
    endTime=time.time()
    print("Tempo di esecuzione in serie: ",endTime-startTime)



def worker(queue):
    while True:
        a=queue.get()
        effettua_request(a)
        queue.task_done()
def esecuzione4ProcessiQueue(siti_web):
    queue = Queue()
    startTime=time.time()
    for url in (siti_web):
        queue.put(url)
    process=[Thread(target=worker,args=(queue,)) for _ in range(4)]
    
    [processes.start() for processes in process]

    queue.join()

    endTime=time.time()
    print("Tempo di esecuzione in paralello: ",endTime-startTime)

if __name__ == '__main__':
# Esempio di utiliz
    esecuzioneinserio(siti_web)
    esecuzione1Processo1url(siti_web)
    esecuzione4ProcessiQueue(siti_web)
