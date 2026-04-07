import re
import customtkinter as ctk
from tkinter import messagebox
from src.database import salvar_remedio, listar_remedios

# Configuração visual (Foco em Acessibilidade para Idosos)
ctk.set_appearance_mode("light")  
ctk.set_default_color_theme("blue")

class AppRemedios(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configurações da Janela
        self.title("Controle de Medicamentos")
        self.geometry("450x700") # Aumentei um pouco a altura para caber o novo botão

        # Título
        self.label_titulo = ctk.CTkLabel(self, text="MEUS REMÉDIOS", font=("Arial", 32, "bold"))
        self.label_titulo.pack(pady=30)

        # Campo: Nome do Remédio
        self.label_nome = ctk.CTkLabel(self, text="Qual o nome do remédio?", font=("Arial", 16))
        self.label_nome.pack()
        self.entry_nome = ctk.CTkEntry(self, placeholder_text="Ex: Dipirona", width=350, height=50, font=("Arial", 18))
        self.entry_nome.pack(pady=10)

        # Campo: Horário
        self.label_horario = ctk.CTkLabel(self, text="Que horas deve tomar?", font=("Arial", 16))
        self.label_horario.pack()
        self.entry_horario = ctk.CTkEntry(self, placeholder_text="Ex: 08:00", width=350, height=50, font=("Arial", 18))
        self.entry_horario.pack(pady=10)

        # Botão SALVAR (Verde e Grande)
        self.botao_salvar = ctk.CTkButton(self, text="SALVAR REMÉDIO", 
                                          command=self.acao_botao_salvar,
                                          fg_color="#27ae60", hover_color="#219150",
                                          width=350, height=70, font=("Arial", 20, "bold"))
        self.botao_salvar.pack(pady=20)

        # Botão VER LISTA (Azul)
        self.btn_listar = ctk.CTkButton(self, text="VER MEUS REMÉDIOS", 
                                        command=self.abrir_lista,
                                        width=350, height=50, font=("Arial", 16))
        self.btn_listar.pack(pady=10)

        # Texto de feedback (Abaixo dos botões)
        self.label_aviso = ctk.CTkLabel(self, text="", font=("Arial", 14, "bold"))
        self.label_aviso.pack(pady=20)

    def acao_botao_salvar(self):
        """Lógica para validar e salvar o remédio."""
        nome = self.entry_nome.get().strip()
        horario = self.entry_horario.get().strip()

        # Validação com Expressão Regular (padrão HH:MM)
        padrao_hora = re.compile(r'^([01]?[0-9]|2[0-3]):[0-5][0-9]$')

        if not nome:
            messagebox.showwarning("Atenção", "Por favor, digite o nome do remédio.")
            return

        if not padrao_hora.match(horario):
            messagebox.showerror("Horário Inválido", "Use o formato de 24h (Ex: 08:30 ou 22:00)")
            return

        # Se passar nas validações, salva no JSON
        salvar_remedio(nome, horario)
        
        # Feedback visual
        self.label_aviso.configure(text=f"✅ {nome} salvo para às {horario}!", text_color="green")
        
        # Limpa os campos
        self.entry_nome.delete(0, 'end')
        self.entry_horario.delete(0, 'end')

    def abrir_lista(self):
        """Cria uma nova janela para listar os remédios cadastrados."""
        janela_lista = ctk.CTkToplevel(self)
        janela_lista.title("Lista de Agendamentos")
        janela_lista.geometry("400x500")
        janela_lista.attributes("-topmost", True) # Faz a janela aparecer na frente

        ctk.CTkLabel(janela_lista, text="Remédios Agendados", font=("Arial", 20, "bold")).pack(pady=20)
        
        remedios = listar_remedios()
        
        if not remedios:
            ctk.CTkLabel(janela_lista, text="Nenhum remédio cadastrado ainda.").pack(pady=20)
        else:
            # Criamos um frame com scroll caso a lista seja grande
            scroll_frame = ctk.CTkScrollableFrame(janela_lista, width=350, height=350)
            scroll_frame.pack(pady=10, padx=10)

            for r in remedios:
                texto = f"💊 {r['nome']} ➔ {r['horario']}"
                ctk.CTkLabel(scroll_frame, text=texto, font=("Arial", 16)).pack(pady=5, anchor="w")

if __name__ == "__main__":
    app = AppRemedios()
    app.mainloop()