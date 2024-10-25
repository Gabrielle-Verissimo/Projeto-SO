from Process import Process
from Scheduler import Scheduler
import random
import threading
from ResourceMonitor import ResourceMonitor

class ProcessManager:
    def __init__(self):
        self.processList = []
        self.pidCounter = 1
        self.scheduler = Scheduler()
        self.lock = threading.Lock()
        self.resourceMonitor = ResourceMonitor()
        
    def createProcess(self, instructions):
        process = Process(str(self.pidCounter), 'new', 0, random.randint(30, 10000), instructions)
        self.processList.append(process)
        self.pidCounter += 1 
    
    def runProcess(self, pid):
        for p in self.processList:
            if p.getPID() == pid:
                p.setState('pronto')
                self.scheduler.appendReadyList(p)
                threading.Thread(target=self.runScheduler).start() #cria uma thread para não bloquear o console
                
    def runScheduler(self):
        f = random.randint(0, 1)
        with self.lock:  # Bloqueia a execução até que o processo atual termine
            if f == 0:
                self.scheduler.roundRobin()
            else:
                self.scheduler.fifo()
    
    def  listProcess(self):
        for p in self.processList:
            print(p)
            
    def finishProcess(self, pid):
        for p in self.processList:
            if p.getPID() == pid:
                self.processList.remove(p)
                self.scheduler.readyList.remove(p)
                self.scheduler.runList.remove(p)
                
    def showResourcesMonitor(self):
        self.resourceMonitor.showResources(self.processList)