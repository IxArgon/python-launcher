import subprocess
import sys
scriptname='createuser.ps1'
def launch():
    print("Lancement du script")
    print(scriptname)
    subprocess.Popen(["runas","/user:Administrateur",'powershell.exe', 'SCRIPT/createuser.ps1'], stdout=sys.stdout)
#Modifie l'user Administrateur par une variable récupérer dans appli.pyw