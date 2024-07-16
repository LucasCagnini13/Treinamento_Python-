import pyautogui
import time
import pandas

#pause para cada comando do pyautogui
pyautogui.PAUSE = 1

#entrar no navegador opera e acessar o site do gmail
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")
time.sleep(5)
pyautogui.write("https://mail.google.com/mail/u/1/#inbox")
pyautogui.press("enter")

#aguardar para entrar no site e clicar na caixa de inscrever email
time.sleep(15)
pyautogui.click(x=-1190, y=-1)
time.sleep(10)

#ler base de dados
tabela = pandas.read_csv("emails.csv")

#colocar imformações da base de dados no email
#a quantidade de emails enviados será proporcional as linhas da tabela
for elemento in tabela.index:

    pyautogui.write(tabela.loc[elemento,"emails"])
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.write(tabela.loc[elemento,"assuntos"])
    pyautogui.press("tab")
    pyautogui.write(tabela.loc[elemento,"mensagem"])
    pyautogui.press("tab")
    pyautogui.press("enter")

    time.sleep(7)
    pyautogui.click(x=-1190, y=-1)
 

