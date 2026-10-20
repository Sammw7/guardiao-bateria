#!/data/data/com.termux/files/usr/bin/python
import os, json, subprocess
try:
  r = subprocess.check_output(["termux-battery-status"]).decode()
  b = json.loads(r)['percentage']
  if b <= 20:
    os.system("termux-vibrate -d 1000")
    os.system(f"termux-notification --title 'BATERIA BAIXA! 🔋' --content '{b}% - carrega agora!' --priority high --icon battery-alert")
  else:
    os.system(f"termux-notification --title 'Guardiao Bateria' --content '{b}% - bateria de boa!' --icon battery-charging-80")
except Exception as e:
  os.system(f"termux-notification --title 'Erro' --content '{e}'")
