#importar tkinter (criando uma janela)
from tkinter import *
from tkinter import ttk

#cores
cor1 = '#080808' #preto
cor2 = '#ffffff' #branco
cor3 = '#965d8c' #rosa escuro meio vinho mas não tanto mas nao tao escuro tbm, na vdd nao é muito rosa tbm
cor4 = '#8a6e86' #roxo cinza KKKKKKKK
cor5 = '#6f68cc' #azul clarinho

#criando a janela
janela = Tk() 
janela.title('Calculadora') #título da janela
janela.geometry('235x318') #tamanho janela
janela.config(bg=cor3)

#criando frames/ dividir a tela
frame_tela = Frame(janela, width=235, height=50, bg=cor4) #width: largura/ height: altura/ bg: cor
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268, bg=cor2)
frame_corpo.grid(row=1, column=0)

#botões / width: largura/ height: altura/ bg: cor botão/ fg: cor da letra
b_1 = Button(frame_corpo, text= 'C',width=11, height=2, bg=cor3, fg=cor2, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0) #posição
b_2 = Button(frame_corpo, text= '%',width=5, height=2, bg=cor3, fg=cor2, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE )
b_2.place(x=120, y=0) 
b_3 = Button(frame_corpo, text= '/',width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_3.place(x=180, y=0) 
b_4 = Button(frame_corpo, text= '7',width=5, height=2, bg=cor3, fg=cor2, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52) 
b_5 = Button(frame_corpo, text= '8',width=5, height=2, bg=cor3, fg=cor2, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_5.place(x=60, y=52) 
b_6 = Button(frame_corpo, text= '9',width=5, height=2, bg=cor3, fg=cor2, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_6.place(x=120, y=52) 
b_7 = Button(frame_corpo, text= '*',width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_7.place(x=180, y=52) 
b_8 = Button(frame_corpo, text= '4',width=5, height=2, bg=cor3, fg=cor2, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104) 
b_9 = Button(frame_corpo, text= '5',width=5, height=2, bg=cor3, fg=cor2, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_9.place(x=60, y=104) 
b_10 = Button(frame_corpo, text= '6',width=5, height=2, bg=cor3, fg=cor2, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_10.place(x=120, y=104) 
b_11 = Button(frame_corpo, text= '-',width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_11.place(x=180, y=104) 
b_12 = Button(frame_corpo, text= '1',width=5, height=2, bg=cor3, fg=cor2, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156) 
b_13 = Button(frame_corpo, text= '2',width=5, height=2, bg=cor3, fg=cor2, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_13.place(x=60, y=156) 
b_14 = Button(frame_corpo, text= '3',width=5, height=2, bg=cor3, fg=cor2, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_14.place(x=120, y=156) 
b_15 = Button(frame_corpo, text= '+',width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_15.place(x=180, y=156) 
b_16 = Button(frame_corpo, text= '0',width=11, height=2, bg=cor3, fg=cor2, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=208) 
b_17 = Button(frame_corpo, text= '.',width=5, height=2, bg=cor3, fg=cor2, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_17.place(x=120, y=208) 
b_18 = Button(frame_corpo, text= '=',width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_18.place(x=180, y=208) 

janela.mainloop() #janela ficar aberta