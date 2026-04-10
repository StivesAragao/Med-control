import re
import customtkinter as ctk
from tkinter import messagebox
from src.database import salvar_remedio, listar_remedios, excluir_remedio, atualizar_remedio

class AppRemedios(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Controle de Medicamentos")
        self.geometry("450x700")

        # Variável para a Máscara de Hora (00:00)
        self.hora_var = ctk.StringVar()
        self.hora_var.trace_add("write", self.formatar_hora)

        # UI Principal
        ctk.CTkLabel(self, text="MEUS REMÉDIOS", font=("Arial", 32, "bold")).pack(pady=30)

        ctk.CTkLabel(self, text="Nome do remédio:", font=("Arial", 16)).pack()
        self.entry_nome = ctk.CTkEntry(self, width=350, height=50, font=("Arial", 18))
        self.entry_nome.pack(pady=10)

        ctk.CTkLabel(self, text="Horário (HH:MM):", font=("Arial", 16)).pack()
        self.entry_horario = ctk.CTkEntry(self, textvariable=self.hora_var, placeholder_text="00:00", width=350, height=50, font=("Arial", 18))
        self.entry_horario.pack(pady=10)

        self.botao_salvar = ctk.CTkButton(self, text="SALVAR REMÉDIO", command=self.acao_botao_salvar,
                                          fg_color="#27ae60", hover_color="#219150", width=350, height=70, font=("Arial", 20, "bold"))
        self.botao_salvar.pack(pady=20)

        self.btn_listar = ctk.CTkButton(self, text="GERENCIAR LISTA", command=self.abrir_lista, width=350, height=50)
        self.btn_listar.pack(pady=10)

    def formatar_hora(self, *args):
        """Aplica a máscara 00:00 e limita a 5 caracteres."""
        puro = "".join(filter(str.isdigit, self.hora_var.get())) # Pega só números
        
        if len(puro) > 4:
            puro = puro[:4]
            
        if len(puro) >= 3:
            formatado = f"{puro[:2]}:{puro[2:]}"
        else:
            formatado = puro
            
        self.hora_var.set(formatado)

    def acao_botao_salvar(self):
        nome = self.entry_nome.get().strip()
        horario = self.hora_var.get().strip()
        padrao_hora = re.compile(r'^([01]?[0-9]|2[0-3]):[0-5][0-9]$')

        if nome and padrao_hora.match(horario):
            salvar_remedio(nome, horario)
            messagebox.showinfo("Sucesso", f"{nome} salvo!")
            self.entry_nome.delete(0, 'end')
            self.hora_var.set("")
        else:
            messagebox.showerror("Erro", "Verifique o nome e se o horário está completo (Ex: 08:00)")

    def abrir_lista(self):
        janela_lista = ctk.CTkToplevel(self)
        janela_lista.title("Gerenciar Remédios")
        janela_lista.geometry("500x550")
        janela_lista.attributes("-topmost", True)

        remedios = listar_remedios()
        if not remedios:
            ctk.CTkLabel(janela_lista, text="Nenhum remédio cadastrado.").pack(pady=20)
            return

        scroll = ctk.CTkScrollableFrame(janela_lista, width=450, height=450)
        scroll.pack(pady=10, padx=10)

        for r in remedios:
            frame = ctk.CTkFrame(scroll)
            frame.pack(fill="x", pady=5, padx=5)

            lbl = ctk.CTkLabel(frame, text=f"💊 {r['nome']} às {r['horario']}", font=("Arial", 14))
            lbl.pack(side="left", padx=10)

            # Botão Excluir
            btn_del = ctk.CTkButton(frame, text="Excluir", width=60, fg_color="#c0392b", 
                                    command=lambda n=r['nome']: self.confirmar_exclusao(n, janela_lista))
            btn_del.pack(side="right", padx=5)

            # Botão Editar
            btn_edit = ctk.CTkButton(frame, text="Editar", width=60, 
                                     command=lambda n=r['nome'], h=r['horario']: self.janela_editar(n, h, janela_lista))
            btn_edit.pack(side="right", padx=5)

    def confirmar_exclusao(self, nome, janela):
        if messagebox.askyesno("Excluir", f"Remover {nome}?"):
            excluir_remedio(nome)
            janela.destroy()
            self.abrir_lista()

    def janela_editar(self, nome_antigo, hora_antiga, janela_pai):
        janela_edit = ctk.CTkToplevel(self)
        janela_edit.title(f"Editando {nome_antigo}")
        janela_edit.geometry("350x300")
        
        # Garante que ela nasça na frente e capture o foco
        janela_edit.attributes("-topmost", True)
        janela_edit.focus_force() 
        janela_edit.grab_set()

        entry_n = ctk.CTkEntry(janela_edit, width=250)
        entry_n.insert(0, nome_antigo)
        entry_n.pack(pady=10)

        entry_h = ctk.CTkEntry(janela_edit, width=250)
        entry_h.insert(0, hora_antiga)
        entry_h.pack(pady=10)

        def salvar_edicao():
            atualizar_remedio(nome_antigo, entry_n.get(), entry_h.get())
            janela_edit.destroy()
            janela_pai.destroy()
            self.abrir_lista()

        ctk.CTkButton(janela_edit, text="Salvar Alteração", command=salvar_edicao).pack(pady=10)