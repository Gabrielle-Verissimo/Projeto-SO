import time

class Scheduler:

    def __init__(self):
        self.readyList = []
        self.runList = []

    def appendReadyList(self, p):
        self.readyList.append(p)
        
    def appendRunList(self, p):
        self.runList.append(p)

    # Método FIFO (First In, First Out)
    def fifo(self):
        while self.readyList:
            process = self.readyList.pop(0)  # Remove o primeiro processo da lista de prontos
            print(f"Executando processo: {process.getPID()}")
            # Simula a execução do processo e adiciona na lista de processos em execução
            self.runList.append(process)
            process.setState('executando')
            # Após execução, remove da runList
            time.sleep(process.getBurstTime() / 1000)
            self.runList.remove(process)
            process.setState('concluído')
            print(f"Processo {process.getPID()} concluído")

    # Método Round-Robin
    def roundRobin(self, quantum):
        while self.readyList:
            process = self.readyList.pop(0)  # Remove o primeiro processo da lista de prontos
            remaining_burst = process.getBurstTime()
            print(f"Executando processo: {process.getPID()}")
            # Simula execução do processo até o fim do quantum ou até o término do burst time
            if remaining_burst <= quantum:
                print(f"Processo {process.getPID()} executado por {remaining_burst} unidades de tempo e concluído")
                self.runList.append(process)
                process.setState('executando')
                self.runList.remove(process)
                process.setState('concluído')
            else:
                print(f"Processo {process.getPID()} executado por {quantum} unidades de tempo")
                process.setBurstTime(remaining_burst - quantum)  # Reduz o burst time do processo
                self.readyList.append(process)  # Reinsere o processo ao final da fila de prontos

    # Método SJF (Shortest Job First)
    def sjf(self):
        while self.readyList:
            # Ordena a lista de prontos pelo burst time
            self.readyList.sort(key=lambda p: p.getBurstTime())
            process = self.readyList.pop(0)  # Remove o processo com menor burst time
            print(f"Executando processo: {process.getPID()}")
            # Simula a execução do processo
            self.runList.append(process)
            process.setState('executando')
            # Após execução, remove da runList
            self.runList.remove(process)
            process.setState('concluído')
            print(f"Processo {process.getPID()} concluído")
