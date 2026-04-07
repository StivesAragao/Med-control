from src.database import salvar_remedios, listar_remedios

print("Salvando remedio...")
salvar_remedios("Dipirona", "14:00")

lista = listar_remedios()
print(f"Remedios cadastrados: {lista}")