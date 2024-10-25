
class Process:

    def __init__(self, pid, state, pc, burstTime, instructions):
        self.pid = pid
        self.state = state
        self.pc = pc
        self.burstTime = burstTime # tempo que leva para ser concluído em ms
        self.instructions = instructions



    def getPID(self):
        return self.pid

    def getState(self):
        return self.state

    def getPC(self):
        return self.pc
    
    def getBurstTime(self):
        return self.burstTime

    def getInstructions(self):
        return self.instructions

    def setPID(self, pid):
        self.pid = pid

    def setState(self, state):
        self.state = state

    def setPC(self, pc):
        self.pc = pc
        
    def setBurstTime(self, burstTime):
        self.burstTime = burstTime

    def setInstructions(self, instructions):
        self.instructions = instructions
        
    def __str__(self):
        return (f"PID: {self.pid}, State: {self.state}, PC: {self.pc}, "
                #f"Records: {self.records}, Allocated Memory: {self.allocated_memory} KB, "
                f"Instructions: {self.instructions}")



