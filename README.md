# Med-Control 💊

**Autor:** Stives Aragão  
**Versão:** 1.2.2  
**Status:** Finalizado (Projeto Acadêmico - UniCEUB)

📋 Descrição do Problema Real
Muitas pessoas, especialmente idosos ou pacientes com tratamentos complexos, enfrentam dificuldades em manter a pontualidade na ingestão de medicamentos. O esquecimento ou a confusão de horários pode comprometer a eficácia do tratamento e a saúde do paciente.

🚀 Proposta da Solução
O **Med-Control** é uma aplicação desktop simples e intuitiva que permite ao usuário cadastrar seus remédios e horários. A aplicação monitora o relógio do sistema em tempo real e emite notificações visuais e sonoras (via sistema operacional) quando chega o momento de cada dose.

✨ Funcionalidades Principais
- **CRUD Completo:** Cadastro, listagem, edição e exclusão de medicamentos.
- **Máscara de Horário:** Entrada de dados padronizada (HH:MM) para evitar erros do usuário.
- **Notificações em Tempo Real:** Sistema de monitoramento em segundo plano (Threading).
- **Persistência de Dados:** Armazenamento local em formato JSON.

🛠️ Tecnologias Utilizadas
- **Python 3.13**
- **CustomTkinter:** Interface gráfica moderna.
- **Plyer:** Notificações nativas do sistema.
- **Pytest:** Testes automatizados de banco de dados.
- **Flake8:** Linting e análise estática de código.
- **GitHub Actions:** Integração Contínua (CI).

🔧 Instruções de Instalação e Execução
1. Clone o repositório:
   ```bash
   git clone [https://github.com/StivesAragao/med-control.git](https://github.com/StivesAragao/med-control.git)

2. Instale as dependências:
   ```bash 
   pip install -r requirements.txt

3. Execute a aplicação:
   ```bash 
   python main.pyas

🧪 Instruções de Testes e Lint
- Para rodar os testes automatizados:
  ```
  python -m pytest

- Para rodar a análise estática (Lint):
  ```
  python -m flake8 src/
