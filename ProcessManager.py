from Process import Process

class ProcessManager:
    def __init__(self):
        self.processList = []
        self.pidCounter = 1
        
    def createProcess(self, instructions):
        process = Process(str(self.pidCounter), 'new', 0, instructions)
        self.processList.append(process)
        self.pidCounter += 1 
    
    def  listProcess(self):
        for p in self.processList:
            print(p)
            
    #tirar o retorno depois dos testes
    def updateState(self, pid):
        p = ''
        for p in self.processList:
            if p.getPID() == pid:
                return p