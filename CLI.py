import cmd
from ProcessManager import ProcessManager

processManager = ProcessManager()

class CLI(cmd.Cmd):
    prompt = '>> '
    intro = 'Digite "help" para ver os comandos disponíveis.'

    def do_create_process(self, line):
        """Cria uma novo processo. Passe como argumento o nome do arquivo com as instruções."""
        processManager.createProcess(line)
        
    def do_list_process(self, line):
        """Lista todos os processos"""
        processManager.listProcess()
        
    def do_run_process(self, line):
        """Executar processo. Recebe o pid do processo como argumento."""
        processManager.runProcess(line)
        
    def do_finish_process(self, line):
        """Finaliza um processo. Recebe o pid do processo como argumento."""
        processManager.finishProcess(line)

    def do_show_resources(self, line):
        """Mostra os recursos do pc"""
        processManager.showResourcesMonitor()
    
    def do_quit(self, line):
        """Encerra o CLI"""
        return True