import time

class Scheduler:

    def __init__(self):
        self.readyList = []
        self.runList = []
        self.readySJF = []
        self.runSJF = []

    def appendReadyList(self, p):
        self.readyList.append(p)
        
    def appendRunList(self, p):
        self.runList.append(p)

    # Método FIFO (First In, First Out)
    def fifo(self):
        while self.readyList:
            process = self.readyList.pop(0)  # Remove o primeiro processo da lista de prontos
            self.runList.append(process)
            process.setState('executando')
            print(f"Executando processo: {process.getPID()}")
            time.sleep(process.getBurstTime() / 1000)
            self.runList.remove(process)
            process.setState('concluído')
            print(f"Processo {process.getPID()} concluído")

    # Método Round-Robin
    def roundRobin(self, quantum=4):
        while self.readyList:
            process = self.readyList.pop(0)  # Remove o primeiro processo da lista de prontos
            self.runList.append(process)
            process.setState('executando')
            print(f"Executando processo: {process.getPID()}")
            time.sleep(quantum / 1000)
            # Simula execução do processo até o fim do quantum ou até o término do burst time
            if process.getBurstTime() <= quantum:
                self.runList.remove(process)
                process.setState('concluído')
            else:
                process.setBurstTime(process.getBurstTime() - quantum)  # Reduz o burst time do processo
                self.readySJF.append(process)  # Reinsere o processo ao final da fila de prontos do SJF

    # Método SJF (Shortest Job First)
    def sjf(self):
        while self.readySJF:
            # Ordena a lista de prontos pelo burst time
            self.readySJF.sort(key=lambda p: p.getBurstTime())
            process = self.readyList.pop(0)  # Remove o processo com menor burst time
            self.runSJF.append(process)
            process.setState('executando')
            print(f"Executando processo: {process.getPID()}")
            self.runSJF.remove(process)
            process.setState('concluído')
            print(f"Processo {process.getPID()} concluído")