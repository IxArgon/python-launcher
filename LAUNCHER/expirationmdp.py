import subprocess
import sys
scriptname='expirationMDP.ps1'
def launch():
    print("Lancement du script")
    print(scriptname)
    subprocess.Popen(['powershell.exe', 'SCRIPT/expirationMDP.ps1'], stdout=sys.stdout)
