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

#Realizar login (email e senha)
pyautogui.click(x=1043, y=405)
pyautogui.write("automatizadorpython@email.com")
pyautogui.press("tab")
pyautogui.write("123456789@")
pyautogui.click(x=1274, y=568)

#Pausa para carregamento
time.sleep(3)

#Importar dados
import pandas
tabela = pandas.read_csv('automacao-produtos/produtos.csv')

#Escrevendo os produtos

for linha in tabela.index:

    codigo = tabela.loc[linha, "codigo"]
    
    pyautogui.click(x=1077, y=293)

    pyautogui.write(codigo)
    pyautogui.press("tab")
 
    pyautogui.write("Marca")
    pyautogui.press("tab")

    pyautogui.write("Tipo")
    pyautogui.press("tab")

    pyautogui.write("Categoria")
    pyautogui.press("tab")

    pyautogui.write("Preco")
    pyautogui.press("tab")

    pyautogui.write("Custo")
    pyautogui.press("tab")

    pyautogui.write("OBS")

    pyautogui.click(x=1190, y=939)

    pyautogui.scroll(5000)

