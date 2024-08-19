# Cada processo deve conter:
# PID (Process Identifier)
# Estado do Processo (pronto, executando, bloqueado, terminado)
# Contador de Programa (PC)
# Registros
# Memória Alocada
# Instruções

class Process:

    def __init__(self, pid, state, pc, instructions):
        self.pid = pid
        self.state = state
        self.pc = pc
        # self.records = records
        # self.allocated_memory = allocated_memory
        self.instructions = instructions



    def getPID(self):
        return self.pid

    def getState(self):
        return self.state

    def getPC(self):
        return self.pc

    def getInstructions(self):
        return self.instructions

    def setPID(self, pid):
        self.pid = pid

    def setState(self, state):
        self.state = state

    def setPC(self, pc):
        self.pc = pc

    def setInstructions(self, instructions):
        self.instructions = instructions
        
    def __str__(self):
        return (f"PID: {self.pid}, State: {self.state}, PC: {self.pc}, "
                #f"Records: {self.records}, Allocated Memory: {self.allocated_memory} KB, "
                f"Instructions: {self.instructions}")



