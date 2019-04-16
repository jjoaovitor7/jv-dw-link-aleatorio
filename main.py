from tkinter import *
import random

janela = Tk()
janela.title("Deep Web Link Aleatório")
janela.geometry("280x100")
janela.configure(bg="black")

menubar = Menu(janela)
janela.config(menu=menubar)
opcaomenu1 = Menu(menubar)
menubar.add_cascade(label='Temas', menu=opcaomenu1)

def mostrarLinks():
         janelaURL = Tk()
         janelaURL.title('Links')
         url1 = Label(janelaURL, text="Facebook - facebookcorewwwi.onion", font=("Comic Sans MS", "10"))
         url2 = Label(janelaURL, text="notEvil - hss3uro2hsxfogfq.onion", font=("Comic Sans MS", "10"))
         url3 = Label(janelaURL, text="The Chess - theches3nacocgsc.onion", font=("Comic Sans MS", "10"))
         url4 = Label(janelaURL, text="Internet Archive - archivecrfip2lpi.onion", font=("Comic Sans MS", "10"))
         url5 = Label(janelaURL, text="DuckDuckGo - 3g2upl4pq6kufc4m.onion", font=("Comic Sans MS", "10"))
         url6 = Label(janelaURL, text="TorPaste - 5y5ek6tlzttcxgvlknf5mxybbsntfqsq2q2fngdbfmskgghukfkn5uqd.onion", font=("Comic Sans MS", "10"))
         url7 = Label(janelaURL, text="Bible4u - bible4u2kjgjvbxs.onion", font=("Comic Sans MS", "10"))
         url8 = Label(janelaURL, text="Torch - xmh57jrzrnw6insl.onion", font=("Comic Sans MS", "10"))
                                                                          
         url1.grid(column=0, row=0)
         url2.grid(column=0, row=1)
         url3.grid(column=0, row=3)
         url4.grid(column=0, row=4)
         url5.grid(column=0, row=5)
         url6.grid(column=0, row=6)
         url7.grid(column=0, row=7)
         url8.grid(column=0, row=8)
    
opcaomenu2 = Menu(menubar)
menubar.add_cascade(label='Links', menu=opcaomenu2)
opcaomenu2.add_command(label='Mostrar Links', command=mostrarLinks)

titulo = Label(janela, text="Deep Web Link Aleatório", font=("Comic Sans MS", "10", "bold", "italic"))
titulo.grid(column=0, row=0, sticky=W)
titulo.configure(bg="black", fg="#00ff00")

url = Label(janela, text="URL", font=("Comic Sans MS", "9"))
url.grid(column=0, row=2)
url.configure(bg="black", fg ="#00ff00")

def clicado():
        sitesDW = ["Facebook - facebookcorewwwi.onion", "notEvil - hss3uro2hsxfogfq.onion", "The Chess - theches3nacocgsc.onion", "Internet Archive - archivecrfip2lpi.onion", "DuckDuckGo - 3g2upl4pq6kufc4m.onion", "TorPaste - 5y5ek6tlzttcxgvlknf5mxybbsntfqsq2q2fngdbfmskgghukfkn5uqd.onion", "Bible4u - bible4u2kjgjvbxs.onion/", "Torch - xmh57jrzrnw6insl.onion"]
        siteDW = random.choice(sitesDW)
        url.configure(text=siteDW)
        
siteBotao = Button(janela, text="Go!", command=clicado)
siteBotao.grid(column=0, row=4)
siteBotao.configure(bg="black", fg="#00ff00")

def TemaBranco():
        janela.configure(bg="white")
        titulo.configure(bg="white", fg="black")
        url.configure(bg="white", fg="black")
        siteBotao.configure(bg="white", fg="black")

def TemaPreto():
        janela.configure(bg="black")
        titulo.configure(bg="black", fg="#00ff00")
        url.configure(bg="black", fg="#00ff00")
        siteBotao.configure(bg="black", fg="#00ff00")

opcaomenu1.add_command(label='Tema Branco', command=TemaBranco)
opcaomenu1.add_command(label='Tema Preto', command=TemaPreto)

janela.mainloop()