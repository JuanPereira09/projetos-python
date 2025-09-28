# -*- coding: utf-8 -*-
# Automação de tarefas Python
#Passo 1: Entrar no sistema da empresa: https://dlp.hashtagtreinamentos.com/python/intensivao/login
#Passo 2: Fazer login
#Passo 3: Baixar a base de dados
#Passo 4: Cadastrar um novo produto
#Passo 5: Repetir para todos os produtos

#pyautogui -> Biblioteca de automação de tarefas

#pyautogui.click -> Clica em um ponto da tela
#pyautogui.write -> Escreve um texto
#pyautogui.press -> Pressiona uma tecla
#pyautogui.hotkey -> Pressiona uma combinação de teclas

import pyautogui
pyautogui.PAUSE = 0.7 #Pausa de 0.5 segundos entre cada comando
import time #Biblioteca de tempo para fazer pausas

#Passo 1: Entrar no sistema da empresa: https://dlp.hashtagtreinamentos.com/python/intensivao/login

pyautogui.press("win") #Pressiona a tecla windows
pyautogui.write("chrome") #Escreve o nome do programa
pyautogui.press("enter") #Pressiona a tecla enter
time.sleep(2) #Espera 2 segundos para o chrome abrir
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login") #Escreve a URL
pyautogui.press("enter") #Pressiona a tecla enter

#Passo 2: Fazer login 

time.sleep(3.5) #Espera 3 segundos para a página carregar
pyautogui.click(x=721, y=407) #Clica no campo de email
pyautogui.write("emailteste@gmail.com") #Escreve o email
pyautogui.click(x=779, y=509) #Clica no campo de senha
pyautogui.write("Senha1234") #Escreve a senha
#Ou voce pode usar o tab para ir para o campo de senha
#por exemplo agora para logar
pyautogui.press("tab") #Pressiona a tecla tab
pyautogui.press("enter") #Pressiona a tecla enter

#Passo 3: Baixar a base de dados
import pandas

tabela = pandas.read_csv(r"C:\Users\Juan\Documents\Python FIles\AutomaçãoPython\produtos.csv") #Ler a base de dados e armazena em uma vari�vel

print(tabela) 

#Passo 4: Cadastrar um novo produto

#pyautogui.click(x=819, y=296) #Clica em código do produto
#time.sleep(2) #Espera 2 segundos para a página carregar

#codigo = "MOLO000251"
#pyautogui.write(codigo) #Escreve o código do produto
#pyautogui.press("tab") #Pressiona a tecla tab

#marca = "Logitech"
#pyautogui.write(marca) #Escreve a marca do produto
#pyautogui.press("tab") #Pressiona a tecla tab

#tipo = "Mouse"
#pyautogui.write(tipo) #Escreve o tipo do produto
#pyautogui.press("tab") #Pressiona a tecla tab

#categoria = "1"
#pyautogui.write(categoria) #Escreve a categoria do produto
#pyautogui.press("tab") #Pressiona a tecla tab

#preco_unitario = "25.95"
#pyautogui.write(preco_unitario) #Escreve o preço unitário do produto
#pyautogui.press("tab") #Pressiona a tecla tab

#custo = "6.50"
#pyautogui.write(custo) #Escreve o custo do produto
#pyautogui.press("tab") #Pressiona a tecla tab

#obs = ""
#pyautogui.write(obs) #Escreve a observação do produto
#pyautogui.press("tab") #Pressiona a tecla tab
#pyautogui.press("enter") #Pressiona a tecla enter para salvar o produto

#time.sleep(1)
#pyautogui.scroll(10000) #Rola a tela para cima (Positivo sobe a tela, negativo desce a tela)

#Passo 5: Repetir para todos os produtos

for linha in tabela.index: #Para cada linha na tabela
    pyautogui.click(x=819, y=296) #Clica em código do produto
    time.sleep(2) #Espera 2 segundos para a página carregar

    codigo = tabela.loc[linha]["codigo"]
    pyautogui.write(codigo) #Escreve o código do produto
    pyautogui.press("tab") #Pressiona a tecla tab

    marca = tabela.loc[linha]["marca"]
    pyautogui.write(marca) #Escreve a marca do produto
    pyautogui.press("tab") #Pressiona a tecla tab

    tipo = tabela.loc[linha]["tipo"]
    pyautogui.write(tipo) #Escreve o tipo do produto
    pyautogui.press("tab") #Pressiona a tecla tab
    
    categoria = tabela.loc[linha]["categoria"]
    pyautogui.write(str(categoria)) #Escreve a categoria do produto
    pyautogui.press("tab") #Pressiona a tecla tab

    preco_unitario = tabela.loc[linha]["preco_unitario"]
    pyautogui.write(str(preco_unitario)) #Escreve o preço unitário do produto
    pyautogui.press("tab") #Pressiona a tecla tab

    custo = tabela.loc[linha]["custo"]
    pyautogui.write(str(custo)) #Escreve o custo do produto
    pyautogui.press("tab") #Pressiona a tecla tab

    obs = tabela.loc[linha]["obs"]  
    if str(obs) != "nan": #Se a observação não for nula
        pyautogui.write(obs) #Escreve a observação do produto

    pyautogui.press("tab") #Pressiona a tecla tab
    pyautogui.press("enter") #Pressiona a tecla enter para salvar o produto

    time.sleep(1)
    pyautogui.scroll(10000) #Rola a tela para cima (Positivo sobe a tela, negativo desce a tela)

