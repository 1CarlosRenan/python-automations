import pyautogui
from time import sleep

# 1 - Clicar e digitar meu usuario
pyautogui.click(1336, 545, duration=0.5)
pyautogui.write('carlos')
# 2 - Clicar e digitar minha senha
pyautogui.click(1328, 562, duration=0.5)
pyautogui.write('123456')
# 3 - Clicar em “Entrar”
pyautogui.click(1197, 591, duration=0.5)
# 4 - Extrair cada produto
with open('produtos.txt', 'r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]

        # 4.1 - clicar e digitar produto
        pyautogui.click(1016, 527, duration=0.5)
        pyautogui.write(produto)

        # 4.2 - clicar e digitar quantidade
        pyautogui.click(1011, 555, duration=0.5)
        pyautogui.write(quantidade)

        # 4.3 - clicar e digitar preco
        pyautogui.click(1009, 581, duration=0.5)
        pyautogui.write(preco)

        # 4.4 - clicar em registrar
        pyautogui.click(924, 737, duration=0.5)

        sleep(1)
