#!/data/data/com.termux/files/usr/bin/python
import time, json, subprocess, os

avisado_20 = False
avisado_100 = False

while True:
    try:
        r = subprocess.check_output(["termux-battery-status"]).decode()
        j = json.loads(r)
        b = j['percentage']
        status = j['status']
        
        # Se chegar em 20% ou menos, avisa
        if b <= 20 and not avisado_20:
            os.system("termux-vibrate -d 1500")
            os.system(f"termux-notification --title 'BATERIA BAIXA! 🪫' --content '{b}% - Coloca pra carregar agora!' --priority high --alert-once --id baixa")
            os.system("termux-tts-speak 'Bateria baixa, vinte porcento'")
            avisado_20 = True
            avisado_100 = False
        elif b > 25:
            avisado_20 = False
            os.system("termux-notification --id baixa --remove")
            
        # Se carregar até 100%, avisa também
        if b >= 100 and status == "FULL" and not avisado_100:
            os.system(f"termux-notification --title 'Bateria Cheia! 🔋' --content 'Pode tirar do carregador!' --priority high --id cheia")
            avisado_100 = True
        elif b < 95:
            avisado_100 = False
            
    except:
        pass
    
    # espera 15 minutos (900 segundos)
    time.sleep(900)
