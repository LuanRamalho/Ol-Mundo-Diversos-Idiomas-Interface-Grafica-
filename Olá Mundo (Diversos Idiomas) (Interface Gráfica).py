import tkinter as tk
from tkinter import messagebox

def exibir_mensagem(op):
    mensagens = {
        1: "Olá Mundo. (Língua Portuguesa)",
        2: "Hola mundo. (Língua Espanhola)",
        3: "Bonjour le monde. (Língua Francesa)",
        4: "Ciao mondo. (Língua Italiana)",
        5: "Hello World. (Língua Inglesa)",
        6: "Hallo Welt. (Língua Alemã)",
        7: "Hej Verden. (Língua Dinamarquesa)",
        8: "Hallo Wereld. (Língua Holandesa)",
        9: "Hei Verden. (Língua Norueguesa)",
        10: "Hej världen. (Língua Sueca)",
        11: "Hei maailma. (Língua Finlandesa)",
        12: "Halló heimur. (Língua Islandesa)",
        13: "Γειά σου Κόσμε (Geiá sou Kósme) (Língua Grega).",
        14: "Salve Mundo. (Língua Latina)",
        15: "Salut Lume. (Língua Romena)",
        16: "Witaj świecie. (Língua Polonesa)",
        17: "Ahoj svet. (Língua Eslovaca)",
        18: "Здраво Свете (Zdravo Svete). (Língua Sérvia)",
        19: "Pozdravljen svet. (Língua Eslovena)",
        20: "Pozdrav svijete. (Língua Croata)",
        21: "Helló Világ. (Língua Húngara)",
        22: "Selam Dünya. (Língua Turca)",
        23: "Привіт Світ (Pryvit Svit). (Língua Ucraniana)",
        24: "Привет мир (Privet mir) (Língua Russa).",
        25: "(shlom lech oalm) שלום עולם. (Língua Hebraica)",
        26: "(marhaban bialealam) مرحبا بالعالم. (Língua Árabe)",
        27: "(Nǐ hǎo shìjiè) 你好 世界. (Língua Chinesa)",
        28: "(hellowoldeu) 헬로월드. (Língua Coreana)",
        29: "(Konnichiwa sekai) こんにちは世界. (Língua Japonesa)",
        30: "नमस्ते दुनिया (namaste duniya). (Língua Hindi)",
    }
    mensagem = mensagens.get(op, "Opção inválida.")
    messagebox.showinfo("Mensagem", mensagem)

# Criando a janela principal
janela = tk.Tk()
janela.title("Exibir Mensagem em Várias Línguas")
janela.geometry("800x600")
janela.configure(bg="#e6f7ff")

# Título
titulo = tk.Label(janela, text="Escolha uma língua para exibir a mensagem", font=("Arial", 16, "bold"), bg="#cce7ff", fg="#003366")
titulo.pack(pady=20)

# Criando os botões para cada idioma
botoes_frame = tk.Frame(janela, bg="#e6f7ff")
botoes_frame.pack(pady=10)

for i in range(1, 31):
    botao = tk.Button(
        botoes_frame,
        text=f"Língua {i}",
        font=("Arial", 12),
        bg="#cce7ff",
        fg="#003366",
        width=15,
        command=lambda i=i: exibir_mensagem(i),
    )
    botao.grid(row=(i - 1) // 5, column=(i - 1) % 5, padx=5, pady=5)

# Rodar o aplicativo
janela.mainloop()
