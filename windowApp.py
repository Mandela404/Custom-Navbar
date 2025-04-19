import customtkinter as ctk
import tkinter.messagebox as mb

# Configura o tema e o modo de aparência
ctk.set_appearance_mode("dark")  # Modo escuro
ctk.set_default_color_theme("blue")  # Tema azul

class LoginWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        # Configuração da janela de login
        self.title("Login - ModMenu FPS")
        self.geometry("400x450")
        self.resizable(False, False)

        # Frame centralizado de login
        frame = ctk.CTkFrame(self)
        frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Título
        ctk.CTkLabel(frame, text="Bem-vindo ao ModMenu FPS", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=(0,20))

        # Campo de usuário
        ctk.CTkLabel(frame, text="Usuário:").pack(anchor="w", padx=10)
        self.username_entry = ctk.CTkEntry(frame, placeholder_text="Digite seu usuário")
        self.username_entry.pack(fill="x", padx=10, pady=(0,10))

        # Campo de senha
        ctk.CTkLabel(frame, text="Senha:").pack(anchor="w", padx=10)
        self.password_entry = ctk.CTkEntry(frame, placeholder_text="Digite sua senha", show="*")
        self.password_entry.pack(fill="x", padx=10, pady=(0,10))

        # Botões de login padrão
        btn_frame = ctk.CTkFrame(frame)
        btn_frame.pack(fill="x", padx=10, pady=(0,10))
        ctk.CTkButton(btn_frame, text="Entrar", command=self.authenticate).pack(side="left", expand=True, pady=5)
        ctk.CTkButton(btn_frame, text="Cancelar", fg_color="#a00", hover_color="#d00", command=self.destroy).pack(side="right", expand=True, pady=5)

        # Seção de login social
        ctk.CTkLabel(frame, text="Ou entre com:", font=ctk.CTkFont(size=14)).pack(pady=(15,5))
        social_frame = ctk.CTkFrame(frame)
        social_frame.pack(padx=10)
        ctk.CTkButton(social_frame, text="Google", width=100, command=lambda: self.social_login("Google")).grid(row=0, column=0, padx=5)
        ctk.CTkButton(social_frame, text="Discord", width=100, command=lambda: self.social_login("Discord")).grid(row=0, column=1, padx=5)
        ctk.CTkButton(social_frame, text="Facebook", width=100, command=lambda: self.social_login("Facebook")).grid(row=0, column=2, padx=5)

        # Seção de registro com email
        ctk.CTkFrame(frame).pack(fill="x", pady=10)
        ctk.CTkLabel(frame, text="Registrar conta", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=(10,5))
        ctk.CTkLabel(frame, text="Email:").pack(anchor="w", padx=10)
        self.email_reg_entry = ctk.CTkEntry(frame, placeholder_text="Digite seu email")
        self.email_reg_entry.pack(fill="x", padx=10, pady=(0,10))
        ctk.CTkLabel(frame, text="Senha:").pack(anchor="w", padx=10)
        self.password_reg_entry = ctk.CTkEntry(frame, placeholder_text="Crie uma senha", show="*")
        self.password_reg_entry.pack(fill="x", padx=10, pady=(0,15))
        ctk.CTkButton(frame, text="Cadastrar", command=self.register).pack(padx=10, pady=(0,5))

    def authenticate(self):
        user = self.username_entry.get()
        pwd = self.password_entry.get()
        # Validação simples de exemplo
        if user == "admin" and pwd == "1234":
            mb.showinfo("Sucesso", "Login realizado com sucesso!")
            self.destroy()
            app = ModMenuApp()
            app.mainloop()
        else:
            mb.showerror("Erro", "Usuário ou senha incorretos.")

    def social_login(self, provider):
        mb.showinfo(f"Login {provider}", f"Redirecionando para login via {provider}...")
        # TODO: implementar OAuth real

    def register(self):
        email = self.email_reg_entry.get()
        pwd = self.password_reg_entry.get()
        if '@' in email and len(pwd) >= 4:
            mb.showinfo("Cadastro", "Registro realizado com sucesso! Verifique seu email.")
        else:
            mb.showerror("Erro", "Preencha um email válido e senha (mínimo 4 caracteres).")

class ModMenuApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        # Janela principal fixa
        self.title("ModMenu FPS")
        self.geometry("1000x700")
        self.resizable(False, False)

        # Tabview para módulos, configurações e perfis
        self.tabview = ctk.CTkTabview(self, width=980, height=680)
        self.tabview.pack(padx=10, pady=10)
        self.tabview.add("Mods")
        self.tabview.add("Settings")
        self.tabview.add("Profiles")

        # Cria conteúdo de cada aba
        self.create_mods_tab()
        self.create_settings_tab()
        self.create_profiles_tab()

    def create_mods_tab(self):
        tab = self.tabview.tab("Mods")
        # ... conteúdo igual ao anteriormente definido ...
        pass

    def create_settings_tab(self):
        tab = self.tabview.tab("Settings")
        ctk.CTkLabel(tab, text="Configurações gerais (em breve)").pack(pady=20)

    def create_profiles_tab(self):
        tab = self.tabview.tab("Profiles")
        ctk.CTkLabel(tab, text="Gerenciamento de perfis (em breve)").pack(pady=20)

if __name__ == "__main__":
    login = LoginWindow()
    login.mainloop()
