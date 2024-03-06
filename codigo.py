import pyautogui

#Variáveis
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

#abrir o navegador Chrome:
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write(link)

