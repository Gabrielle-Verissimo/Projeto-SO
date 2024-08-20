from Process import Process
from Scheduler import Scheduler
import threading
import time

class ProcessManager:
    def __init__(self):
        self.processList = []
        self.pidCounter = 1
        self.scheduler = Scheduler()
        
    def createProcess(self, instructions):
        process = Process(str(self.pidCounter), 'new', 0, instructions)
        self.processList.append(process)
        self.pidCounter += 1 
        threading.Thread(target=self.runProcess, args=(process, )).start()
    
    def runProcess(self, pid):
        for p in self.processList:
            if p.getPID() == pid:
                p.setState('pronto')
                self.scheduler.readyList.append(p)
        
    def  listProcess(self):
        for p in self.processList:
            print(p)
            
    # def updateState(self, pid, state):
    #     for p in self.processList:
    #         if p.getPID() == pid:
    #             p.setState(state)
    #             return p