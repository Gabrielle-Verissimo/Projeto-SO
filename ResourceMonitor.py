import random

class ResourceMonitor:
    def __init__(self) -> None:
        pass

    def showResources(self, processList):
        print("PID    %CPU    %MEM")
        print("-" * 20)
        for p in processList:
            cpu = round(random.uniform(0.1, 8.5), 1)
            mem = round(random.uniform(0.1, 8.5), 1)
            print(f"{p.getPID():<5}  {cpu:<5.1f}   {mem:<5.1f}")