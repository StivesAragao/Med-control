import threading
import time
from datetime import datetime
from src.gui import AppRemedios
from src.database import listar_remedios
from src.notifications import disparar_alerta

def verificar_horarios():
    """Função que roda em segundo plano vigiando o relógio."""
    alertados = []
    
    while True:
        agora = datetime.now().strftime("%H:%M")
        remedios = listar_remedios()
        
        for remedio in remedios:
            if remedio['horario'] == agora and remedio['nome'] not in alertados:
                disparar_alerta(remedio['nome'])
                alertados.append(remedio['nome'])
        
        if datetime     .now().strftime("%S") == "00":
            alertados.clear()
            
        time.sleep(10)

if __name__ == "__main__":
    threading.Thread(target=verificar_horarios, daemon=True).start()    
    app = AppRemedios()
    app.mainloop()