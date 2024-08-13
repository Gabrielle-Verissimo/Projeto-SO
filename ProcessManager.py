from Process import Process

class ProcessManager:
    def __init__(self):
        self.processList = []
        self.pidCounter = 1
        
    def createProcess(self, instructions):
        process = Process(self.pidCounter, 'new', 0, ['eax, ebx'], 1024, instructions)
        self.processList.append(process)
        self.pidCounter += 1 
    
    def  listProcess(self):
        for p in self.processList:
            print(p)