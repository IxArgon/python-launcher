import subprocess
import sys
scriptname='policy.bat'
def launch():
    print("Lancement du script")
    print(scriptname)
    subprocess.Popen(['cmd.exe', 'SCRIPT/policy.bat'], stdout=sys.stdout)