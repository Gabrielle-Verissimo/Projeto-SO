from Fila import Fila
import threading
import time
from compilador import MediaCompiler

class Scheduler:

    def __init__(self):
        self.readyList = []
        self.runList = []


    def execute(self, programa):
        compiler = MediaCompiler()
        compiler.execute_command(programa)

        
    # def execute(self, programa):
    #     self.compilador(programa)
           
    #     threading.Thread(target=self.executionTime, args=(process.getPID(), 'pronto')).start()
    
    # def executionTime(self, pid, state):
    #     time.sleep(1)
    #     p = self.updateState(pid, state)
    #     self.scheduler.readyList.append(p)
    