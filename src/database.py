import json
import os

DB_FILE = "remedios.json"

def listar_remedios():
    """Lê todos os remédios cadastrados."""
    if not os.path.exists(DB_FILE):
        return []
    
    with open(DB_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def salvar_remedio(nome, horario):
    """Salva um novo remédio no arquivo JSON."""
    dados = listar_remedios()
    
    novo_remedio = {
        "nome": nome,
        "horario": horario
    }
    
    dados.append(novo_remedio)
    
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)