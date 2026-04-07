import threading
import time
from datetime import datetime
from src.gui import AppRemedios
from src.database import listar_remedios
from src.notifications import disparar_alerta

def verificar_horarios():
    """Função que roda em segundo plano vigiando o relógio."""
    alertados = [] # Para não disparar o mesmo alerta várias vezes no mesmo minuto
    
    while True:
        agora = datetime.now().strftime("%H:%M")
        remedios = listar_remedios()
        
        for remedio in remedios:
            # Se o horário bater e ainda não avisamos neste minuto
            if remedio['horario'] == agora and remedio['nome'] not in alertados:
                disparar_alerta(remedio['nome'])
                alertados.append(remedio['nome'])
        
        # Limpa a lista de alertados quando o minuto muda
        if datetime.now().strftime("%S") == "00":
            alertados.clear()
            
        time.sleep(10) # Verifica a cada 10 segundos para não pesar no PC

if __name__ == "__main__":
    # Criamos uma "Thread" (uma tarefa paralela) para o relógio
    threading.Thread(target=verificar_horarios, daemon=True).start()
    
    # Inicia a interface gráfica normalmente
    app = AppRemedios()
    app.mainloop()