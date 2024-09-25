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
        
    # async def execute(self):
    #     if len(self.readyList) < 2:
    #         process = self.readyList.pop(0)
    #         self.runList.append(process)

    #     else:
    #         process = self.readyList.pop(0)
    #         self.runList.append(process)
    #         await asyncio.sleep(1)
        
    def run(self):
        process = self.readyList.pop(0)
        self.runList.append(process)
        if len(self.readyList) < 2:    
            print(f'Executando processo: {process}')
            time.sleep(1)
        else:
            print('entrou aqui')
            time.sleep(1)
            self.readyList.append
    
    def appendReadyList(self, p):
        p.setState('pronto')
        self.readyList.append(p)
        
    def appendRunList(self, p):
        p.setState('executando')
        self.runList.append(p)