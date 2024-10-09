import pyautogui
import time

#------------SISTEMA PARA MARCAR E-MAIL ANTIGOS COMO LIDOS------------#

while True:                                    # LOOP INFINITO
    pyautogui.click(-444, 1291, duration=0.3)  # SELECT ALL
    pyautogui.click(-4, 1291, duration=0.3)    # SELECT
    pyautogui.click(73, 1323, duration=0.3)    # READ ALL
    pyautogui.press("F5")                      # RECARREGA A PAGINA
    time.sleep(0.5)                            # TEMPO DE ESPERA
    pyautogui.press("Enter")                   # SE DER POP-UP DE ERRO ELE CONTINUA
    time.sleep(5)                              # TEMPO DE ESPERA

# Link do acesso para teste https://cadastro-produtos-devaprender.netlify.app/index.html tela 70/30
# pip install mouseinfo -> Pegar as coordenadas do mouse
# python > from mouseinfo import mouseInfo > mouseInfo()