from multiprocessing import Process
"""
multiprocessing è una libreria per la creazione , la comunicazione e la sincronizzazione
tra processi nella programmazione perallela e concorrente
Process è una classe per creare processi eseguendo una funzione (o metodo ) sprecificara come target
"""

def process_function(data):
    result=data*2
    print(result)

if __name__ == "__main__":
    data_list=[1,2,3,4]
    processes=[]

    for data in data_list:
        p= Process(target=process_function,args=(data, ))
        processes.append(p)
        p.start()#Avvia l'esecuzione del processo separato

        for p in processes:
            p.join()#Blocaa il processo principale fino a quando il processo separato non termina