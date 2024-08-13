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


    def __str__(self):
        return (f"PID: {self.pid}, State: {self.state}, PC: {self.pc}, "
                f"Records: {self.records}, Allocated Memory: {self.allocated_memory} KB, "
                f"Instructions: {self.instructions}")
    # decodifica as instruções
    def decode_instruction(self, instruction):
        parts = instruction.split()
        op = parts[0]
        args = parts[1:]
        return op, args
    
    # Executa a instrução
    # Recebe o operador e os argumentos da operação
    def execute(self, op, args):
        if op in self.instructions:
            # Exexuta o metodo relacionado a operações e passa os argumentos para ele.
            self.instructions[op](*args)
        else:
            raise Exception(f"Unknown instruction: {op}")

    # Busca a proxima instrução nalista de instruções que o usuario inserir
    def fetch(self):
        instruction = self.user_inst_memory['program'][self.pc]  # Busca a instrução atual
        self.pc += 1  # Incrementa o contador de programa
        return instruction  # Retorna a instrução buscada
    
    # Inicia a VM
    def run(self, user_instruction):
        while self.pc < len(user_instruction):
            instruction = self.fetch()
            op, args = self.decode_instruction(instruction)
            self.execute(op, args)


