import cmd
from ProcessManager import ProcessManager

processManager = ProcessManager()

class CLI(cmd.Cmd):
    prompt = '>> '
    intro = 'Welcome to MyCLI. Type "help" for available commands.'

    def do_create_process(self, line):
        """Create a new process. Passe como argumento o nome do arquivo com as instruções."""
        processManager.createProcess(line)

    def do_list_process(self, line):
        """List all processes."""
        processManager.listProcess()
    
    #retirar depois do teste    
    def do_update_state(self, line):
        """Atualiza o status do processo"""
        x = processManager.updateState(line)
        print(x)

    def do_quit(self, line):
        """Exit the CLI."""
        return True