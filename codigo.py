import pyautogui
import time

pyautogui.PAUSE = 0.3


#                               - LISTA DE COMANDOS -
# pyautogui.PAUSE -> definir o tempo de resposta para cada comando, sem ele vai muito rapido e pode bugar
# pyautogui.click -> clicar com o mouse
# pyautogui.press -> pressionar uma tecla
# pyautogui.write -> escrever
# pyautogui.scroll -> rola o scroll do mouse. numero positivo sobe, negativo desce
# pyautogui.hotkey -> atalho do teclado (ex: Ctrl, C)
# time.sleep()
# pyautogui.click para passar paramentros como quantidade de clicks ou com qual botao do mouse clicar) -> pyautogui.click(clicks= x, button = 'left or right')
# tabela.index, no python, index é linha
# tabela.loc[ primereiro parametro é linha, segundo coluna]
# PASSO A PASSO 
                                                # PASSO 1 : Abrir o sistema
 
# O sistema abre no google chorme, para acessarmos o google, apertamos a tecla windows e depois escrevemos chorme, segue abaixo.

pyautogui.press('win')

# digitar o texto chorme
pyautogui.write('chorme')

# apertar enter
pyautogui.press('enter')

# entrar no link do sistema: https://dlp.hashtagtreinamentos.com/python/intensivao/login

pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

# pedir pro computador esperar 3s, pois sites podem demorar para abrir, depende do servidor, internet etc, como o meu é rapido vou colocar 1s
time.sleep(1)

#                                                         PASSO 2: Fazer login
    
# Clicar no campo de email
# Usar o pyautogui.position para descobrir a posiçao em que ele precisar clicar, fiz isso no codigo auxiliar.py, depois ir para a senha
# Usar tab para mudar a caixa onde iremos responder, isso tambem servira mais pra frente para cadastrar os produtos, faça pyautogui.press('tab')

pyautogui.click(x=1129, y=470)    #posição da caixa para selecionarmos, só precisa a primeira, depois só mudar no tab

pyautogui.write('casagrandesaqua24@gmail.com')
pyautogui.press('tab')             # passa para o campo senha
pyautogui.write('Fe131104*')

pyautogui.press('tab')             # passa para o botão logar
pyautogui.press('enter')


#                                               PASSO 3: Impotar a base de dados dos produtos



# improvisando porque algo bugou aqui pra mim,peguei do gpt, mas aqui seria somente um tabela.read_csv('produtos_csv')

import os
import pandas as pd

script_dir = os.path.dirname(os.path.abspath(__file__))  # Diretório do script
file_path = os.path.join(script_dir, "produtos.csv")     # Caminho completo do arquivo

tabela = pd.read_csv(file_path)
print(tabela)


#                                                  PASSO 4: Cadastrar um produto


    #codigo,marca,tipo,categoria,preco_unitario,custo,obs



# CODIGO
for linha in tabela.index:                      # Vai percorrer as linhas da tabela, usaremos um loc para pegar o item que esta na linha que o 'for' esta percorrendo e depois especificar a coluna
    pyautogui.click(x=1097, y=329)              
    codigo = tabela.loc[linha,'codigo']
    
     # Preciso transformar em string pois nao pode usar numero, apenas texto, então crio uma variavel, adiciono o item com o loc e no write transformo em string
    pyautogui.write(str(codigo))                
    pyautogui.press('tab')


# MARCA
    marca = tabela.loc[linha,'marca']
    pyautogui.write(str(marca))
    pyautogui.press('tab')

# TIPO 
    tipo = tabela.loc[linha,'tipo']
    pyautogui.write(str(tipo))
    pyautogui.press('tab')

# CATEGORIA
    categoria = tabela.loc[linha,'categoria']
    pyautogui.write(str(categoria))
    pyautogui.press('tab')

# PREÇO
    preco_unitario = tabela.loc[linha,'preco_unitario']
    pyautogui.write(str(preco_unitario))
    pyautogui.press('tab')

# CUSTO
    custo = tabela.loc[linha,'custo']
    pyautogui.write(str(custo))
    pyautogui.press('tab')


# OBS
    obs =str(tabela.loc[linha,'obs'])
    if obs != 'nan':                                    # se nao tiver observação, transformamos o valor nulo 'nan' em uma string vazia, caso tenha, ela é adicionada normalmente.
        pyautogui.write(obs)
    pyautogui.press('tab')
    pyautogui.press('enter')                               # apertar o botão de enviar
    
    # numero positivo = scroll pra cima
    # numero negativo = scroll desce
    pyautogui.scroll(10000)        

# passo 5: Repetir o passo 4 ate acabar os produtos

 
