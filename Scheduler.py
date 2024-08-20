import threading
import time
import asyncio

# async def hello():
#     print('Hello ...')
#     await asyncio.sleep(1)
#     print('... World!')

# async def main():
#     await asyncio.gather(hello(), hello())

# asyncio.run(main())
class Scheduler:
    def __init__(self):
        self.readyList = []
        self.runList = []
        
    async def execute(self):
        if len(self.readyList) < 2:
            process = self.readyList.pop(0)
            self.runList.append(process)
            while(1):
                print(f'Executando processo: {process}')
        else:
            process = self.readyList.pop(0)
            self.runList.append(process)
            await asyncio.sleep(1)
        
    def run_process(self):
        while self.readyList:
            # Move o primeiro processo da lista de prontos para a lista de execução
            process = self.readyList.pop(0)
            process.setState('executando')
            self.runList.append(process)
            
            # Simula a execução do processo por 100ms
            #print(f"Executando processo: {process}")
            #print(process.getState())
            time.sleep(1)
            process.setState('pronto')
            # Move o processo de volta para a lista de prontos
            self.runList.remove(process)
            self.readyList.append(process)
            #print(f"Processo {process} voltou para a lista de prontos")

    # def start(self):
    #     thread = threading.Thread(target=self.run_process)
    #     thread.daemon = True
    #     thread.start()
    