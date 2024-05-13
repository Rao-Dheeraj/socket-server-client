import subprocess

class CommandExecutor:
    @staticmethod
    def execute_command(command):
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            return result.returncode, result.stdout, result.stderr
        except Exception as e:
            return -1, '', str(e)
