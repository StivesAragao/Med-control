import json
import os

DB_FILE = "remedios.json"

def listar_remedios():
    """Lê o arquivo JSON e retorna a lista de remédios."""
    if not os.path.exists(DB_FILE):
        return []
    try:
        with open(DB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def salvar_remedio(nome, horario):
    """Adiciona um novo remédio ao JSON."""
    remedios = listar_remedios()
    remedios.append({"nome": nome, "horario": horario})
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(remedios, f, indent=4, ensure_ascii=False)

def excluir_remedio(nome_alvo):
    """Remove um remédio da lista pelo nome exato."""
    remedios = listar_remedios()
    # Cria uma nova lista filtrando (removendo) o nome escolhido
    novos_remedios = [r for r in remedios if r['nome'] != nome_alvo]
    
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(novos_remedios, f, indent=4, ensure_ascii=False)

def atualizar_remedio(nome_antigo, novo_nome, novo_horario):
    """Procura o remédio antigo e atualiza seus dados."""
    remedios = listar_remedios()
    for r in remedios:
        if r['nome'] == nome_antigo:
            r['nome'] = novo_nome
            r['horario'] = novo_horario
            break
            
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(remedios, f, indent=4, ensure_ascii=False)