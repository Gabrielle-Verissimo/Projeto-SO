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
        
    def do_run_process(self, line):
        """Executar processo"""
        processManager.runProcess(line)

    def do_quit(self, line):
        """Exit the CLI."""
        return True