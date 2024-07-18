# Cada processo deve conter:
# PID (Process Identifier)
# Estado do Processo (pronto, executando, bloqueado, terminado)
# Contador de Programa (PC)
# Registros
# Memória Alocada
# Instruções

class Process:

    def __init__(self, pid, state, pc, records, allocated_memory):
        self.pid = pid
        self.state = state
        self.pc = pc
        self.records = records
        self.allocated_memory = allocated_memory
        self.user_inst_memory = {} 
        self.instructions = {
            'load_video': self.load,
            'PLAY': self.play,
            'PAUSE': self.pause,
            'NEXT': self.next,
            'BACK': self.back,
            'STOP':self.stop,
            'VOLUME': self.volume,


            }

    # Instruções

    # Carrega o filme
    # receber file ou URL ?
    def load(self, file):
        pass
    
    # Inicia o filme
    def play(self):
        pass

    # Para a reprodução do filme
    def stop(self):
        pass

    # Pausa o filme
    def pause(self):
        pass

    # Avança uma certa quantidade de tempo
    def next(self):
        pass

    # Volta uma certa quantidade de tempo
    def back(self):
        pass

    # Ajusta o valor do volume
    def volume(self, valor):
        pass


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


