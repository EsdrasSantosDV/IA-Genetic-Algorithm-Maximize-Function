import tkinter
from tkinter import *
import os
import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random as rd
from matplotlib.figure import Figure
import math

#FUNCAO
def f(x, y):
    return 21.5 + x*math.sin(4*math.pi*x) + y*math.sin(20*math.pi*y)

#INTERVALO
# Definição dos intervalos para x e y
x_interval = (-3.1, 12.1)
y_interval = (4.1, 5.8)



def submit_button_event():
    tamanho_cromossomo = int(form_tamanho_cromossomo.get())
    tamanho_da_populacao = int(form_tamanho_da_populacao.get())
    probabilidade_de_cruzamento = float(form_probabilidade_de_cruzamento.get())
    mutacao_probabilidade = float(form_mutacao_probabilidade.get())
    quantidade_geracoes = int(form_quantidade_geracoes.get())
    if check_var.get():
        tamanho_torneio = int(form_tamanho_torneio.get())
    else:
        tamanho_torneio = None

    tamanho_elitismo = int(form_tamanho_elitismo.get())
    tamanho_elitismo = int(form_tamanho_elitismo.get())  # Adicione esta linha

    # Salvar o selection_method e crossover_type
    selection_method = "tournament" if check_var.get() else "roulette"
    crossover_type = crossover_var.get()

    # Exibir logs dos valores inseridos
    print("Tamanho do cromossomo:", tamanho_cromossomo)
    print("Tamanho da população:", tamanho_da_populacao)
    print("Probabilidade de cruzamento:", probabilidade_de_cruzamento)
    print("Probabilidade de mutação:", mutacao_probabilidade)
    print("Quantidade de gerações:", quantidade_geracoes)
    print("Tamanho do torneio:", tamanho_torneio)
    print("Tamanho do elitismo:", tamanho_elitismo)
    print("Selection method:", selection_method)
    print("Crossover type:", crossover_type)

def toggle_torneio_visibility():
    if check_var.get():
        label_tamanho_torneio.place(x=500, y=200)
        form_tamanho_torneio.place(x=650, y=200)
    else:
        label_tamanho_torneio.place_forget()
        form_tamanho_torneio.place_forget()


def on_crossover_selection():
    selected_crossover = crossover_var.get()



window = Tk()
window.title("IA-TRABALHO-GRUPO-ESDRAS-JOAO-OTAVIO-FELIPE MENDES")
window.geometry('1920x1080')
window.configure(background="gray")

label_form=tkinter.Label(window,text="Dados das Entradas",background="gray")
label_tamanho_cromossomo = tkinter.Label(window, text="Tamanho do Cromossomo:",background="gray")
label_tamanho_da_populacao = tkinter.Label(window, text="Tamanho da População:",background="gray")
label_probabilidade_de_cruzamento = tkinter.Label(window, text="Probabilidade de Cruzamento:",background="gray")
label_mutacao_probabilidade = tkinter.Label(window, text="Probabilidade de Mutação:",background="gray")
label_quantidade_geracoes = tkinter.Label(window, text="Quantidade de Geracoes:",background="gray")
label_tamanho_torneio =  tkinter.Label(window, text="Tamanho do Torneio:",background="gray")
label_tamanho_elitismo = tkinter.Label(window, text="Tamanho do Elitismo:", background="gray")
form_tamanho_elitismo = tkinter.Entry()
#INPUTS
form_tamanho_cromossomo=tkinter.Entry()
form_tamanho_da_populacao=tkinter.Entry()
form_probabilidade_de_cruzamento=tkinter.Entry()
form_mutacao_probabilidade=tkinter.Entry()
form_quantidade_geracoes=tkinter.Entry()
form_tamanho_torneio=tkinter.Entry()

#LOCALIZAÇÃO
label_form.place(x=200,y=10)
label_tamanho_da_populacao.place(x=100,y=50)
form_tamanho_da_populacao.place(x=325,y=50)
label_tamanho_cromossomo.place(x=100,y=80)
form_tamanho_cromossomo.place(x=325,y=80)
label_probabilidade_de_cruzamento.place(x=100,y=110)
form_probabilidade_de_cruzamento.place(x=325,y=110)
label_quantidade_geracoes.place(x=100,y=140)
form_quantidade_geracoes.place(x=325,y=140)
label_mutacao_probabilidade.place(x=100,y=170)
form_mutacao_probabilidade.place(x=325,y=170)
label_tamanho_elitismo.place(x=100, y=200)
form_tamanho_elitismo.place(x=325, y=200)
#CHECKBOX
check_var = tkinter.BooleanVar()
check_torneio = tkinter.Checkbutton(window, text="Torneio", variable=check_var, command=toggle_torneio_visibility, background="gray")
check_torneio.place(x=100, y=230)
label_tamanho_torneio.place_forget()
form_tamanho_torneio.place_forget()

#RADIO BUTTON
crossover_var = StringVar(value="one_point")
radio_one_point = Radiobutton(window, text="Cruzamento de um ponto", variable=crossover_var, value="one_point", command=on_crossover_selection, background="gray")
radio_two_points = Radiobutton(window, text="Cruzamento de dois pontos", variable=crossover_var, value="two_points", command=on_crossover_selection, background="gray")
radio_one_point.place(x=100, y=260)
radio_two_points.place(x=300, y=260)

#SUBMIT
submit_button = tkinter.Button(window, text="Submit", command=submit_button_event)
submit_button.place(x=350, y=300)


window.mainloop()
