import pyautogui
import time

#Variáveis
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.PAUSE = 0.5

#Abrir o navegador Chrome:
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write(link)
pyautogui.press("enter")

#Pausa para carregamento
time.sleep(3)

#Realizar login
pyautogui.click(x=1043, y=405)