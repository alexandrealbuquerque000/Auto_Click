
# Alexandre Maia Aquino de Albuquerque

import pyautogui # Para controlar as ações do mouse
import os # Para 'limpar' o terminal
import time # Para controlar o tempo de execução

#Função para ler apenas letras:
def leiastr(msg):
    while True:
        print()
        verif=str(input(msg).strip().replace(" ", ""))
        if verif.isalpha() == False:
            print()
            print("ERRO:""\nDigite apenas letras.")
            continue
        else:
            verif=verif.lower()
            return verif
        
#Função verificadora de números inteiros
def leiaposiint(msg):
    while True:
        try:
            print()
            N=int(input(msg).strip().replace(" ", ""))
        except (ValueError, TypeError, IndexError):
            print()
            print("ERRO:""\nDigite apenas números inteiros positivos.")
            continue
        else:
            if N<0 or ('cliques' in msg and N==0):
                print()
                print("Número inválido.\n\nTente novamente.")
                continue
            elif N==0:
                infinity=1
                N=5
            else:
                infinity=0
            return N, infinity

#Função verificadora de números decimais
def leiaposifloat(msg):
    while True:
        try:
            print()
            N=float(input(msg).strip().replace(" ", ""))
        except (ValueError, TypeError, IndexError):
            print()
            print("ERRO:""\nDigite apenas números.")
            continue
        else:
            if N<=0:
                print()
                print("Número inválido.\n\nTente novamente.")
                continue
            return N

# Função para indicar algum tipo de 'loading'
def loading(msg, numsec):
    os.system("cls")
    print('\n'+msg, end=' ')
    parttmp=0.25
    for count in reversed(range(1, numsec+1)):
        print(count, end='')
        for threepoints in range(3):
            time.sleep(parttmp)
            print('.', end='')
        time.sleep(parttmp)
    print(0)

# Função para guardar as posições do mouse especificadas pelo usuário
def getpos(numclicks):    
    listpos=[]          
    for loop1 in range(numclicks):
        loading('A posição do mouse será salva em', 5)
        x, y=pyautogui.position()
        listpos.append((x, y))

    return listpos

# Função para rodar o programa
def run():
    pyautogui.FAILSAFE = False
    reboot='s'
    while 's' in reboot:
        os.system('cls')
        print('-'*12)
        print(' Auto Click')
        print('-'*12)
        lar, alt=pyautogui.size()
        numclicks, infinity=leiaposiint('Digite quantos cliques deseja fazer: ')
        if numclicks==1:
            tmpclicks=0
        else:
            tmpclicks=leiaposifloat('Digite o intervalo de tempo(segundos) entre os cliques: ')
        numloops, infinity=leiaposiint("Digite quantos 'loopings' deseja fazer (Digite '0' para infinitos 'loopings'): ")
        if numloops==1:
            tmploops=0
        else:
            tmploops=leiaposifloat("Digite o intervalo de tempo(minutos) entre os 'loopings': ")
            tmploops=tmploops*60
        workarea=leiastr("Deseja alternar para a área de trabalho enquanto o programa espera o reinício do 'looping'? ")
        if 's' in workarea:
            workarea=1
        else:
            workarea=0
        listpos=getpos(numclicks)
        loading('As predefinições iniciarão em 10 segundos.\n', 10)
        os.system('cls')
        while True:
            for loop2 in range(numloops):
                for loop3 in listpos:
                    pyautogui.click(loop3)
                    time.sleep(tmpclicks)
                if workarea==1:
                    pyautogui.hotkey('win', 'd')
                time.sleep(tmploops)
                if workarea==1:
                    pyautogui.hotkey('win', 'd')
            if infinity==1:
                continue
            else:
                break
        print('\nProcesso concluído.')
        reboot=leiastr('Deseja reiniciar o programa? ')


run()