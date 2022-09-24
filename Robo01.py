import pyautogui as p

# cord = p.moveTo(321, 745, duration = 3) # move o mouse até o local da cordenada mas não clica
# p.click(cord) # clica na cordenada

# localização do mouse (cordenadas x, y)
# p.sleep(2) # espera dois segundos
# print(p.position()) # depois pega a posição do mouse

p.hotkey('win', 'r') # recebe teclas de atalho do teclado
p.sleep(1)
p.typewrite('notepad') # escreve um texto
p.sleep(2)
p.press('enter')
p.sleep(2)
p.typewrite('Oi. Eu sou um bot.')
p.sleep(2)
valor = p.getActiveWindow() # pega a tela ativa
valor.close() # fecha a janela
p.press('right') # pressiona para a direita
p.sleep(2)
p.press('enter')
