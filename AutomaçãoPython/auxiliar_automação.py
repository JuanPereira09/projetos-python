# -*- coding: utf-8 -*-
import pyautogui
import time 

time.sleep(3) #Tempo para o usuário posicionar o mouse

pyautogui.scroll(10000)

print(pyautogui.position()) #Mostra a posição do mouse na tela ao executar
#Usar esse comando para descobrir as posições dos cliques na tela

