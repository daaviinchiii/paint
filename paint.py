from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import filedialog  
import pyscreenshot as ImageGrab
from tkinter.ttk import *
from tkinter import ttk

# Cria o objeto (janela) com o nome janela
janela = Tk()

# Adiciona um titulo à janela
janela.title("Pinta")

# Dimensões da janela
janela.geometry("700x655")

style = ttk.Style()
style.configure("BW.Button", foreground="black", background="white")
def show():
    color = askcolor()[1]  
    pinta_cor(color)

def pinta_cor(cor):
    global cor_atual  
    cor_atual = cor

def pinta_linha(event):
    global cor_atual
    # Coordenadas do ponteiro do rato.
    x1, y1, x2, y2 = (event.x - 1), (event.y - 0), (event.x + 0), (event.y + 0)
     
    # tipo de desenho create_line
    cv.create_line(x1, y1, x2, y2, fill=cor_atual)

def pinta_bola(event):
    global cor_atual
    # Coordenadas do ponteiro do rato.
    x, y = event.x, event.y
     
    # Desenha um círculo com raio 12
    cv.create_oval(x-12, y-12, x+12, y+12, fill=cor_atual, outline='')

def pinta_bola_pequena(event):
    global cor_atual
    # Coordenadas do ponteiro do rato.
    x, y = event.x, event.y
     
    # Desenha um círculo com raio 12
    cv.create_oval(x-2, y-2, x+2, y+2, fill=cor_atual, outline='')

def pinta_quadrado(event):
    global cor_atual
    # Coordenadas do ponteiro do rato.
    x, y = event.x, event.y
     
    # Desenha um círculo com raio 12
    cv.create_rectangle(x, y, x+12, y+12, fill=cor_atual, outline='')
def pinta_linha(event):
    global cor_atual
    # Coordenadas do ponteiro do rato.
    x, y = event.x, event.y
     
    # Desenha um círculo com raio 12
    cv.create_line(x, y-12, x+12, y, fill=cor_atual)
def trocar_pinta_borracha(event):
    # Coordenadas do ponteiro do rato.
    x, y = event.x, event.y
     
    # Desenha um círculo com raio 12
    cv.create_rectangle(x, y, x+12, y+12, fill='#f0f0f0', outline='')

def reset():
    cv.delete("all")


def open_popup():
    top = Toplevel(janela)
    top.geometry("550x250")
    top.title("Caneta")
    Button(top, text='bola', image=grande, command=lambda: [trocar_pinta_bola(), top.destroy()]).place(x=40, y=80)
    Button(top, text='linha', image=linha, command=lambda: [trocar_pinta_linha(), top.destroy()]).place(x=150, y=80)
    Button(top, text='quadrado', image=quadrado, command=lambda: [trocar_pinta_quadrado(), top.destroy()]).place(x=260, y=80)
    Button(top, text='bolapequena', image=pequena, command=lambda: [trocar_pinta_bola_pequena(), top.destroy()]).place(x=370, y=80)

pequena = PhotoImage(file="resource/pequena.png")
quadrado = PhotoImage(file="resource/quadrado.png")
grande = PhotoImage(file="resource/grande.png")
linha = PhotoImage(file="resource/linha.png")

def trocar_pinta_bola():
    cv.bind("<B1-Motion>", pinta_bola)

def trocar_pinta_linha():
    cv.bind("<B1-Motion>", pinta_linha)

def trocar_pinta_bola_pequena():
    cv.bind("<B1-Motion>", pinta_bola_pequena)

def pinta_borracha():
    cv.bind("<B1-Motion>", trocar_pinta_borracha)

def trocar_pinta_quadrado():
    cv.bind("<B1-Motion>", pinta_quadrado)
# Cria um canvas para desenhar
cv = Canvas(janela, width=700, height=550)

# Chama a função pinta houver um
# click e arrasto simultaneo no botão esquerdo do rato
cv.bind("<B1-Motion>", pinta_linha)
# ooo

def save_canvas():
    # Captura a tela atual
    screenshot = ImageGrab.grab(bbox=(cv.winfo_rootx(), cv.winfo_rooty(),
                                       cv.winfo_rootx() + cv.winfo_width(),
                                       cv.winfo_rooty() + cv.winfo_height()))
    file_path = filedialog.asksaveasfilename( initialfile="print.png")
    if file_path:
        screenshot.save(file_path)

# Cria um botão para salvar a captura de tela
botao5 = Button(janela, text='Salvar', command=save_canvas)

# Restante do seu código...


# Cria um label
lbl = Label(janela, text="Click e Arraste para desenhar.")
botao = Button(janela, text='Cor', command=show)
botao4 = Button(janela, text='Caneta', command=open_popup)
botao3 = Button(janela, text='reset',command=reset)
botao2 = Button(janela, text='borracha',command=pinta_borracha)
botao5 = Button(janela, text='Salvar', command=save_canvas)
# Coloca o label e o canvas na janela
lbl.pack()
cv.pack()
botao2.pack(side=LEFT)
botao3.pack(side=LEFT)
botao4.pack(side=LEFT)
botao5.pack(side=LEFT)
botao.pack(side=LEFT)

cor_atual = "black"

janela.mainloop()