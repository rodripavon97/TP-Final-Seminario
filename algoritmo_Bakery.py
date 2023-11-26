import threading

class Bakery:
    def __init__(self, num_processes):
        self.num_processes = num_processes
        self.entering = [False] * num_processes
        self.number = [0] * num_processes

    def lock(self, process_id):
        self.entering[process_id] = True
        self.number[process_id] = max(self.number) + 1
        self.entering[process_id] = False

        for i in range(self.num_processes):
            while self.entering[i]:
                pass
            while self.number[i] != 0 and (
                (self.number[i], i) < (self.number[process_id], process_id)
                or (self.number[i] == self.number[process_id] and i < process_id)
            ):
                pass

    def unlock(self, process_id):
        self.number[process_id] = 0

# Uso del algoritmo en tres procesos (hilos)
num_processes = 3
bakery_lock = Bakery(num_processes)

def process(process_id):
    i = 0
    while i < 3:
        # Sección no crítica

        # Entrar a la sección crítica
        bakery_lock.lock(process_id)
        # Sección crítica
        print(f"Process {process_id} is in critical section.")
        # Salir de la sección crítica
        bakery_lock.unlock(process_id)
        print(f"Process {process_id} is outside critical section.")

        # Sección no crítica
        i += 1

# Crear hilos para los procesos
threads = [threading.Thread(target=process, args=(i,)) for i in range(num_processes)]

# Iniciar los hilos
for thread in threads:
    thread.start()

# Esperar a que todos los hilos terminen
for thread in threads:
    thread.join()
