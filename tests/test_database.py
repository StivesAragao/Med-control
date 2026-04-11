from src.database import salvar_remedio, listar_remedios
def test_salvar_e_listar():
    salvar_remedio("Teste", "10:00")
    lista = listar_remedios()
    assert any(r['nome'] == "Teste" for r in lista)