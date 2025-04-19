import customtkinter as ctk
import tkinter.messagebox as mb

# Configura o tema e o modo de aparência
ctk.set_appearance_mode("dark")  # Modo escuro
ctk.set_default_color_theme("blue")  # Tema azul

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
        # Frame horizontal: sidebar + conteúdo principal
        container = ctk.CTkFrame(tab)
        container.pack(fill="both", expand=True)

        # Sidebar de filtros
        sidebar = ctk.CTkFrame(container, width=200)
        sidebar.pack(side="left", fill="y", padx=(10,5), pady=10)
        ctk.CTkLabel(sidebar, text="Filters", font=ctk.CTkFont(size=18, weight="bold")).pack(pady=(5,10))
        filters = ["All", "Popular", "PvP", "Visual", "Movement", "Combat", "Utility"]
        for f in filters:
            btn = ctk.CTkButton(sidebar, text=f, width=180, fg_color=None, hover_color="#334154")
            btn.pack(pady=5)

        # Área principal: header de busca + lista de mods
        main_area = ctk.CTkFrame(container)
        main_area.pack(side="right", fill="both", expand=True, padx=(5,10), pady=10)

        # Header com ícone de edição, search e close
        header = ctk.CTkFrame(main_area, height=50)
        header.pack(fill="x", pady=(0,10))
        self.edit_btn = ctk.CTkButton(header, text="✏️", width=40, command=self.edit_filters)
        self.edit_btn.pack(side="left", padx=5)
        self.search_entry = ctk.CTkEntry(header, placeholder_text="Search...", width=200)
        self.search_entry.pack(side="left", padx=5)
        self.close_btn = ctk.CTkButton(header, text="✖", width=40, command=self.destroy)
        self.close_btn.pack(side="right", padx=5)

        # ScrollableFrame para exibir módulos em grid
        self.mod_scroll = ctk.CTkScrollableFrame(main_area, width=740, height=600)
        self.mod_scroll.pack(fill="both", expand=True)

        # Lista de funcionalidades criativas (>40)
        modules = [
            "Wallhack", "Aimbot", "ESP", "Triggerbot", "No Recoil",
            "Speed Hack", "Fly", "Invisibility", "AutoFarm", "Quick Heal",
            "Auto Reload", "Silent Aim", "Radar", "Bunny Hop", "No Clip",
            "Teleport", "Infinite Health", "Custom Crosshair", "Third Person", "Fast Switch",
            "Auto Block", "Fast Break", "Auto Place", "Auto Fish", "Night Vision",
            "Thermal Vision", "Anti Cheat Bypass", "Macro", "Auto Respawn", "Multi Jump",
            "Ultra Jump", "Zoom", "Chams", "Fog Removal", "Smoke ESP",
            "Sound Amplifier", "Chat Filter", "Auto Jump", "Silent Walk", "Brightness",
            "Drop Hack", "XRay", "Packet Control", "Auto Sneak", "Teleport Anchor",
            "Dynamic FOV", "Recoil Control", "Custom HUD", "Auto Chat", "Skin Changer"
        ]

        # Cria botões e toggles em grid de 5 colunas
        cols = 5
        for index, name in enumerate(modules):
            r = index // cols
            c = index % cols
            frame = ctk.CTkFrame(self.mod_scroll, width=140, height=80)
            frame.grid(row=r, column=c, padx=10, pady=10)
            # Label com nome do módulo
            ctk.CTkLabel(frame, text=name).pack(anchor="n", pady=(5,0))
            # Cria switch sem comando inicial
            switch = ctk.CTkSwitch(frame, text="")
            switch.pack(anchor="s", pady=(0,5))
            # Configura callback agora que 'switch' existe
            switch.configure(command=lambda n=name, s=switch: self.toggle_module(n, s))

    def create_settings_tab(self):
        tab = self.tabview.tab("Settings")
        ctk.CTkLabel(tab, text="Configurações gerais (em breve)").pack(pady=20)

    def create_profiles_tab(self):
        tab = self.tabview.tab("Profiles")
        ctk.CTkLabel(tab, text="Gerenciamento de perfis (em breve)").pack(pady=20)

    # Callback para editar filtros
    def edit_filters(self):
        mb.showinfo("Edit Filters", "Função de edição de filtros em desenvolvimento.")

    # Callback ao alternar qualquer módulo
    def toggle_module(self, name, switch):
        state = "ativado" if switch.get() else "desativado"
        mb.showinfo(name, f"Módulo '{name}' {state}!")

if __name__ == "__main__":
    app = ModMenuApp()
    app.mainloop()
