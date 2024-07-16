# Cada processo deve conter:
# PID (Process Identifier)
# Estado do Processo (pronto, executando, bloqueado, terminado)
# Contador de Programa (PC)
# Registros
# Memória Alocada
# Instruções

class Process:
    def __init__(self, pid, state, pc, records, allocated_memory, instructions):
        self.pid = pid
        self.state = state
        self.pc = pc
        self.records = records
        self.allocated_memory = allocated_memory
        self.instructions = instructions