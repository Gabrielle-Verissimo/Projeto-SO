from Fila import Fila
import threading
import time
class Scheduler:
    def __init__(self):
        self.readyList = []
        self.runList = []
        
    # def execute(self):
    #     for p in self.readyList:
           
    #     threading.Thread(target=self.executionTime, args=(process.getPID(), 'pronto')).start()
    
    # def executionTime(self, pid, state):
    #     time.sleep(1)
    #     p = self.updateState(pid, state)
    #     self.scheduler.readyList.append(p)
    