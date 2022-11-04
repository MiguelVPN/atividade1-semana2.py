import threading
from threading import Thread
num = [[], []]

for c in range(1,8):
    numero = int(input(f'Digite o {c}° valor :'))
    if numero % 2 == 0:
        num[0].append(numero)
    else:
        num[1].append(numero)


def execucao():

    for o in range (2):
        print(f"{threading.currentThread().getName()} Executando...")
    

if __name__=="__main__":
    N = 2
    print(f"{threading.currentThread().getName()} iniciando...")

    print(f"{threading.currentThread().getName()} Criando Threads...")
    threads = []
    for o in range(1):

        thread = Thread(target=execucao)
        thread.start()
        threads.append(thread)
        print(f'os valores pares digitados foram:{sorted(num[0])}')

    for o in range(2):

        thread = Thread(target=execucao)
        thread.start()
        threads.append(thread)
        print(f'os valores impares digitados foram:{sorted(num[1])}')


        for thread in threads:
            thread.join()

            print(f"{threading.currentThread().getName()} finalizando...")