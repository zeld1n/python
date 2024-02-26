from multiprocessing import Process,Queue

def process_mult(queue):
    return print((queue.get()*queue.get()*queue.get())/2)

def process_function(n1,n2,op,queue):
    result=eval(f'{n1} {op} {n2}')
    queue.put(result)

if __name__ =="__main__":
    num1=[3,5,3]
    num2=[4,2,3]
    operation=['+','+','*']
    queue=Queue()
    processes=[]

    for i in range(len(num1)):
        n1 = num1[i]
        n2 = num2[i]
        op = operation[i]
        p=Process(target=process_function,args=(n1,n2,op,queue))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("il risultato")
    p1=Process(target=process_mult,args=(queue, ))
    p1.start()
    p1.join()