from plyer import notification

def disparar_alerta(nome_remedio):
    """Manda uma notificação nativa do Windows/Mac."""
    notification.notify(
        title="HORA DO REMÉDIO! 💊",
        message=f"Está na hora de tomar seu: {nome_remedio}",
        app_name="Controle de Medicamentos",
        timeout=10  # O aviso some depois de 10 segundos
    )