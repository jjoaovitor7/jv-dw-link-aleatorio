# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
import platform
import sqlite3
import webbrowser

import definir_cor
import mostrar_urls
import ajuda_redes

def main(self):
    self.title('Deep Web URL Aleatória')
    self.geometry('500x75')
    self.grid_columnconfigure(0, weight = 1)

    so = platform.system()
    try:
        if so == 'Linux':
           self.wm_iconbitmap('@ico/dw_ico.xbm')
    except TclError:
        print('dw_ico.xbm não foi encontrado na pasta ico.')
    try:
        if so == 'Windows':
           self.wm_iconbitmap('ico\dw_ico.ico')
    except TclError:
        print('dw_ico.ico não foi encontrado na pasta ico.')
    
    def tema_preto():
        self.config(bg = definir_cor.COR_PRETA)
        style = ttk.Style()
        style.configure('TLabel', background = definir_cor.COR_PRETA, 
                        foreground = definir_cor.COR_VERDE_CLARO, 
                        font = ('Times New Roman', '14'))
        style.configure('TButton', background = definir_cor.COR_PRETA, 
                        foreground = definir_cor.COR_VERDE_CLARO, 
                        width = 5, relief = tk.RAISED)
    
    def tema_branco():
        self.config(bg = definir_cor.COR_BRANCA)
        style = ttk.Style()
        style.configure('TLabel', background = definir_cor.COR_BRANCA, 
                        foreground = definir_cor.COR_PRETA, 
                        font = ('Times New Roman', '14'))
        style.configure('TButton', background = definir_cor.COR_BRANCA, 
                        foreground = definir_cor.COR_PRETA, 
                        width = 5, relief = tk.RAISED)
   
    tema_preto()

    menubar = tk.Menu(self)
    self.config(menu = menubar)
    
    preferencias = tk.Menu(menubar, tearoff = 0)
    menubar.add_cascade(label = 'Preferências', menu = preferencias)
    
    temas = tk.Menu(menubar, tearoff = 0)
    preferencias.add_cascade(label = 'Temas', menu = temas)

    ajuda = tk.Menu(menubar, tearoff = 0)
    menubar.add_cascade(label = 'Ajuda', menu = ajuda)
    ajuda.add_command(label = 'URLs', command = mostrar_urls.run)
    ajuda.add_command(label = 'Redes', command = ajuda_redes.run)

    lTitulo = ttk.Label(self, text = 'Deep Web URL Aleatória')
    lTitulo.grid(column = 0, row = 0)
    
    lURL = ttk.Label(self, text = 'URL')
    lURL.grid(column = 0, row = 2)
        
    temas.add_command(label = 'Tema Branco', command = tema_branco)
    temas.add_command(label = 'Tema Preto', command = tema_preto)
    
    def botao_go_clicado():        
        conn = sqlite3.connect('urls.db')
        cursor = conn.cursor()
        cursor.execute("""
        SELECT url FROM urls  ORDER BY RANDOM() LIMIT 1;
        """)
        url_ = cursor.fetchall()
        url2_ = str(url_).strip('()[],\'\'')
        lURL.config(text = url_)
        conn.close()
        def clicar_url(event):
            webbrowser.open_new(url2_)
        lURL.bind('<Button-1>', clicar_url)
            
    botao_go = ttk.Button(self, text = 'Go!', 
                         command = botao_go_clicado)
    botao_go.grid(column = 0, row = 4)
    
def run():
    root = tk.Tk()
    main(root)
    root.mainloop()

if __name__ == '__main__':
    run()
