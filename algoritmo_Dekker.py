import threading

class Dekker:
    def __init__(self):
        self.flag = [False, False]  # Flags para indicar el deseo de entrar a la sección crítica
        self.turn = 0  # Indica el turno del proceso actual

    def lock(self, process_id):
        other = 1 - process_id  # ID del otro proceso

        self.flag[process_id] = True  # Indica el deseo de entrar a la sección crítica
        while self.flag[other]:
            if self.turn == other:
                self.flag[process_id] = False
                while self.turn == other:
                    pass
                self.flag[process_id] = True

    def unlock(self, process_id):
        self.turn = 1 - process_id
        self.flag[process_id] = False

# Uso del algoritmo en dos procesos (hilos)
dekker_lock = Dekker()

def process_0():
    # Sección no crítica
    # ...

    # Entrar a la sección crítica
    dekker_lock.lock(0)
    # Sección crítica
    print("Process 0 is in critical section.")
    # Salir de la sección crítica
    dekker_lock.unlock(0)

    # Sección no crítica
    # ...

def process_1():
    # Sección no crítica
    # ...

    # Entrar a la sección crítica
    dekker_lock.lock(1)
    # Sección crítica
    print("Process 1 is in critical section.")
    # Salir de la sección crítica
    dekker_lock.unlock(1)

    # Sección no crítica
    # ...

# Crear hilos para los dos procesos
thread_0 = threading.Thread(target=process_0)
thread_1 = threading.Thread(target=process_1)

# Iniciar los hilos
thread_0.start()
thread_1.start()

# Esperar a que ambos hilos terminen
thread_0.join()
thread_1.join()
