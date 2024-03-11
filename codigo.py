import pyautogui
import time

#Variáveis
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.PAUSE = 0.5

#Abrir o navegador Chrome:1
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")   

pyautogui.write(link)
pyautogui.press("enter")

#Pausa para carregamento
time.sleep(3)

#Realizar login (email e senha)
pyautogui.press("tab")
pyautogui.write("automatizadorpython@email.com")
pyautogui.press("tab")
pyautogui.write("123456789@")
pyautogui.press("tab")
pyautogui.press("enter")

#Pausa para carregamento
time.sleep(3)

#Importar dados
import pandas
tabela = pandas.read_csv('produtos.csv')

#Escrevendo os produtos

for linha in tabela.index:
    
    pyautogui.click(x=1077, y=293)

    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")
 
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")

    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))

    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)

