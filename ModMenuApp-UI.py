# -*- coding: utf-8 -*-
"""
ModMenu UI para BloodStrike usando CustomTkinter
Suporte completo a múltiplos idiomas, tooltips e avisos de banimento.
"""
# Verifica a presença do módulo tkinter antes de importar customtkinter
try:
    import tkinter
except ImportError:
    raise ImportError("O módulo 'tkinter' não está instalado. Instale-o para usar customtkinter.")

import customtkinter as ctk
from PIL import Image

# === Classe Tooltip para exibir descrições ao passar o mouse ===
class Tooltip:
    def __init__(self, widget, text_func):
        self.widget = widget
        self.text_func = text_func
        self.tipwindow = None
        widget.bind("<Enter>", self.show)
        widget.bind("<Leave>", self.hide)
    def show(self, _):
        if self.tipwindow or not self.text_func(): return
        x = self.widget.winfo_rootx() + 20
        y = self.widget.winfo_rooty() + self.widget.winfo_height() + 5
        self.tipwindow = tw = ctk.CTkToplevel(self.widget)
        tw.wm_overrideredirect(True)
        label = ctk.CTkLabel(tw, text=self.text_func(), wraplength=200)
        label.pack(padx=5, pady=5)
    def hide(self, _):
        if self.tipwindow:
            self.tipwindow.destroy()
            self.tipwindow = None

# === Dados de tradução ===
languages = ["pt-br", "en", "fr", "ru"]
lang_map = {"Português-BR":"pt-br", "English":"en", "Français":"fr", "Русский":"ru"}
translations = {
    lang:{
        "title":"ModMenu - BloodStrike",
        "Spoofing":{"pt-br":"Falsificação","en":"Spoofing","fr":"Falsification","ru":"Подделка"}[lang],
        "PvP":{"pt-br":"PvP","en":"PvP","fr":"JcJ","ru":"PvP"}[lang],
        "Visuals":{"pt-br":"Visuais","en":"Visuals","fr":"Visuels","ru":"Визуалы"}[lang],
        "Misc":{"pt-br":"Diversos","en":"Misc","fr":"Divers","ru":"Разное"}[lang],
        "Idioma":{"pt-br":"Idioma","en":"Language","fr":"Langue","ru":"Язык"}[lang]
    } for lang in languages
}

# Opções e traduções
option_keys = {
    "Spoofing":["hwid","ip","rank"],
    "PvP":["aimbot","no_recoil","rapid_fire"],
    "Visuals":["esp","chams","wallhack"],
    "Misc":["bunnyhop","auto_pick","speed_hack"]
}
option_trans = {
    key: {lang: text for lang, text in trans.items()} 
    for key, trans in {
        "hwid":{"pt-br":"HWID","en":"HWID","fr":"ID Matériel","ru":"HWID"},
        "ip":{"pt-br":"IP","en":"IP","fr":"IP","ru":"IP"},
        "rank":{"pt-br":"Spoof Rank","en":"Rank Spoof","fr":"Falsification Rang","ru":"Подделка Ранга"},
        "aimbot":{"pt-br":"Aimbot","en":"Aimbot","fr":"Bot de visée","ru":"Aimbot"},
        "no_recoil":{"pt-br":"Sem Recuo","en":"No Recoil","fr":"Sans Recul","ru":"Без отдачи"},
        "rapid_fire":{"pt-br":"Tiro Rápido","en":"Rapid Fire","fr":"Tir Rapide","ru":"Быстрая стрельба"},
        "esp":{"pt-br":"ESP Inimigo","en":"Enemy ESP","fr":"ESP Ennemi","ru":"ESP Врага"},
        "chams":{"pt-br":"Chams","en":"Chams","fr":"Chams","ru":"Chams"},
        "wallhack":{"pt-br":"Wallhack","en":"Wallhack","fr":"Wallhack","ru":"Wallhack"},
        "bunnyhop":{"pt-br":"Bunnyhop","en":"Bunnyhop","fr":"Bunnyhop","ru":"Bunnyhop"},
        "auto_pick":{"pt-br":"Coleta Automática","en":"Auto Pick","fr":"Ramassage Auto","ru":"Авто сбор"},
        "speed_hack":{"pt-br":"Speed Hack","en":"Speed Hack","fr":"Hack Vitesse","ru":"Хак Скорости"}
    }.items()
}

# Descrições para tooltips e avisos de banimento
descriptions = {
    "hwid":{"pt-br":"Muda seu HWID para evitar bans antigos","en":"Changes your HWID to evade old bans","fr":"Change votre HWID pour éviter les bans","ru":"Меняет ваш HWID для обхода банов"},
    "rank":{"pt-br":"Finge outro rank para atrair inimigos","en":"Spoofs another rank to deceive enemies","fr":"Falsifie un autre rang pour tromper","ru":"Подделывает ранг чтобы обмануть"}
}
warn_keys = ["hwid","ip","rank"]

# Armazenamento de widgets para atualização de idioma
toggle_widgets = {}
tooltip_objs = {}
warning_objs = {}
current_lang = 'pt-br'

# Inicialização da janela principal
root = ctk.CTk()
root.title(translations[current_lang]['title'])
root.geometry("1024x768")
root.minsize(800,600)
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
root.grid_columnconfigure(1,weight=1)
root.grid_rowconfigure(0,weight=1)

# === Sidebar ===
sidebar = ctk.CTkFrame(root, width=200, corner_radius=0)
sidebar.grid(row=0, column=0, sticky="nswe")
sidebar.grid_rowconfigure(len(option_keys)+3,weight=1)
ctk.CTkLabel(sidebar, text="ModMenu", font=ctk.CTkFont(size=20,weight="bold")).grid(row=0, column=0, pady=20)

# Função para alternar seção ativa
def show_section(sec_name):
    frames[sec_name].tkraise()

# Botões de seção
for idx, sec in enumerate(option_keys, start=1):
    btn = ctk.CTkButton(
        sidebar,
        text=translations[current_lang][sec],
        command=lambda s=sec: show_section(s)
    )
    btn.grid(row=idx, column=0, sticky="we", padx=20, pady=5)

# === Painel de conteúdo ===
content = ctk.CTkFrame(root)
content.grid(row=0, column=1, sticky="nswe", padx=10, pady=10)
content.grid_columnconfigure(0,weight=1)
content.grid_rowconfigure(0,weight=1)
frames = {}
for sec in option_keys:
    frame = ctk.CTkFrame(content)
    frame.grid(row=0, column=0, sticky="nswe")
    ctk.CTkLabel(frame, text=translations[current_lang][sec], font=ctk.CTkFont(size=18,weight="bold")).pack(pady=10)
    for key in option_keys[sec]:
        var = ctk.BooleanVar(value=False)
        sw = ctk.CTkSwitch(frame, text=option_trans[key][current_lang], variable=var)
        sw.pack(anchor='w', padx=20, pady=5)
        toggle_widgets[key] = sw
        # Tooltip descriptivo
        if key in descriptions:
            icon = ctk.CTkLabel(frame, text='?', font=ctk.CTkFont(weight="bold"))
            icon.pack(anchor='e', padx=(0,20))
            tooltip_objs[key] = Tooltip(icon, lambda k=key: descriptions[k][current_lang])
        # Warning
        if key in warn_keys:
            wicon = ctk.CTkLabel(frame, text='⚠', font=ctk.CTkFont(weight="bold"))
            wicon.pack(anchor='e', padx=(0,20))
            warning_objs[key] = Tooltip(wicon, lambda k=key: {"pt-br":"Atenção: risco de banimento","en":"Warning: ban risk","fr":"Attention: risque de ban","ru":"Внимание: риск бана"}[current_lang])
    frames[sec] = frame

# Exibe seção padrão
show_section(list(option_keys.keys())[0])

# === Seleção de idioma ===
lang_label = ctk.StringVar(value=translations[current_lang]['Idioma'])
ctk.CTkLabel(sidebar, textvariable=lang_label).grid(row=len(option_keys)+1, column=0, pady=(20,0))
opt = ctk.CTkOptionMenu(
    sidebar,
    values=list(lang_map.keys()),
    command=lambda choice: change_language(choice)
)
opt.set("Português-BR")
opt.grid(row=len(option_keys)+2, column=0, padx=20, pady=(0,20))

# Função para troca de idioma
def change_language(choice):
    global current_lang
    current_lang = lang_map[choice]
    # Atualiza título
    root.title(translations[current_lang]['title'])
    # Atualiza botões de seção
    for idx, sec in enumerate(option_keys, start=1):
        sidebar.grid_slaves(row=idx, column=0)[0].configure(text=translations[current_lang][sec])
    # Atualiza label de idioma
    lang_label.set(translations[current_lang]['Idioma'])
    # Atualiza switches
    for key, sw in toggle_widgets.items():
        sw.configure(text=option_trans[key][current_lang])
    # Tooltips e avisos já referenciam current_lang dinamicamente

# Inicia loop principal
if __name__ == '__main__':
    root.mainloop()
