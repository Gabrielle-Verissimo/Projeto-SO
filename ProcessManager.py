from Process import Process
from Scheduler import Scheduler
import threading
import time

class ProcessManager:
    def __init__(self):
        self.processList = []
        self.pidCounter = 1
        self.scheduler = Scheduler ()
        
    def createProcess(self, instructions):
        process = Process(str(self.pidCounter), 'new', 0, instructions)
        self.processList.append(process)
        self.pidCounter += 1 
        threading.Thread(target=self.delayedUpdateState, args=(process.getPID(), 'pronto')).start()
    
    def delayedUpdateState(self, pid, state):
        time.sleep(1)
        p = self.updateState(pid, state)
        self.scheduler.readyList.append(p)
        
    def  listProcess(self):
        for p in self.processList:
            print(p)
            
    def updateState(self, pid, state):
        for p in self.processList:
            if p.getPID() == pid:
                p.setState(state)
                return p
    
    def runProcess(self, pid):
        self.scheduler.execute()