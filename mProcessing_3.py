import os
from multiprocessing import Process,current_process,Pipe

def process_id():
    print(f"Server PID: {os.getpid()},Process Name: {current_process().name},Process PID: {current_process().pid}")

def process_function(conn):
    process_id()
    print("Elaboro il dato ricevuto ed invio il risultato")
    data_received=conn.recv()
    result=data_received*2
    conn.send(result)
    conn.close()

if __name__=="__main__":
    process_id()
    print("Creo una connessione e un processo figlio")
    parent_conn,child_conn=Pipe()
    data=5
    p=Process(target=process_function,args=(child_conn,))
    p.start()
    parent_conn.send(data)
    result=parent_conn.recv()
    p.join()
    process_id()
    print("Stampo il risultato ricevuto")
    print(result)