import pyautogui

#Variáveis
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

#Abrir o navegador Chrome:
pyautogui.press("win")
pyautogui.PAUSE = 1
pyautogui.write("chrome")
pyautogui.PAUSE = 1
pyautogui.press("enter")
pyautogui.PAUSE = 1

pyautogui.write(link)
pyautogui.PAUSE = 1
pyautogui.press("enter")