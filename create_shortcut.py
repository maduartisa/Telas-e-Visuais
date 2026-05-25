import os
from win32com.client import Dispatch

# Caminhos
script_path = r"c:\Users\maria de jesus\Desktop\Projeto\Telas e Visuais\Telas-e-Visuais\5_appdp.py"
python_path = r"c:\Users\maria de jesus\Desktop\Projeto\Telas e Visuais\Telas-e-Visuais\venv64\Scripts\python.exe"

desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
shortcut_path = os.path.join(desktop, '5_appdp.lnk')

shell = Dispatch('WScript.Shell')
shortcut = shell.CreateShortcut(shortcut_path)
shortcut.Targetpath = python_path
shortcut.Arguments = f'"{script_path}"'
shortcut.WorkingDirectory = os.path.dirname(script_path)
shortcut.IconLocation = python_path
shortcut.Description = 'Atalho para 5_appdp.py (venv64)'
shortcut.save()

print('Atalho criado em:', shortcut_path)
