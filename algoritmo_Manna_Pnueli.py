import threading

class MannaPnueli:
    def __init__(self):
        self.flag = [False, False]  # Flags para indicar el deseo de entrar a la sección crítica
        self.turn = 0  # Indica el turno del proceso actual

    def lock(self, process_id):
        other = 1 - process_id  # ID del otro proceso

        self.flag[process_id] = True  # Indica el deseo de entrar a la sección crítica
        self.turn = other  # Establece el turno del otro proceso

        # Espera hasta que sea su turno y el otro proceso no desee entrar
        while self.flag[other] and self.turn == other:
            pass

    def unlock(self, process_id):
        self.flag[process_id] = False  # Indica que no desea entrar a la sección crítica más

# Uso del algoritmo en dos procesos (hilos)
manna_pnueli_lock = MannaPnueli()

def process_0():
    i = 0
    while i < 3:
        # Sección no crítica

        # Entrar a la sección crítica
        manna_pnueli_lock.lock(0)
        # Sección crítica
        print("Process 0 is in critical section.")
        # Salir de la sección crítica
        manna_pnueli_lock.unlock(0)
        print("Process 0 is outside critical section.")

        # Sección no crítica
        i += 1
   

def process_1():
    i = 0
    while i < 3:
        # Sección no crítica

        # Entrar a la sección crítica
        manna_pnueli_lock.lock(1)
        # Sección crítica
        print("Process 1 is in critical section.")
        # Salir de la sección crítica
        manna_pnueli_lock.unlock(1)
        print("Process 1 is outside critical section.")

        # Sección no crítica
        i += 1

# Crear hilos para los dos procesos
thread_0 = threading.Thread(target=process_0)
thread_1 = threading.Thread(target=process_1)

# Iniciar los hilos
thread_0.start()
thread_1.start()

# Esperar a que ambos hilos terminen
thread_0.join()
thread_1.join()
