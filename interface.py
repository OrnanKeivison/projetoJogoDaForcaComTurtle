from turtle import textinput
import turtle
import time
from time import sleep
turtle = turtle.Turtle()
main = turtle.screen
escritor = turtle.clone()
turtle.speed(5) 
escritor.shape('turtle')
escritor.hideturtle()

def forca():
    global turtle
    #posiciona tartaruga
    turtle.pu()
    turtle.goto(-212.13,212.13)
    turtle.right(-90)
    turtle.fd(50)
    turtle.pd()

    #desenha forca
    turtle.fd(25)
    turtle.right(-90)
    turtle.fd(100)
    turtle.left(90)
    turtle.fd(250)

def cabeca():
    global turtle
    #posiciona tartaruga
    turtle.pu()
    turtle.goto(-212.13,212.13)
    turtle.left(90)
    turtle.pd()
    #desenha cabeça
    turtle.circle(25)

def braco1():
    global turtle
    turtle.pu()
    turtle.goto(-212.13,212.13)
    turtle.pd()
    #desenha os braço
    turtle.right(45)
    turtle.fd(50)
    turtle.pu()
    turtle.backward(50)
    turtle.pd()

def braco2():
    global turtle
    turtle.pu()
    turtle.goto(-212.13,212.13)
    turtle.pd()
    #desenha os braço
    turtle.right(90)
    turtle.fd(50)

def corpo():
    #desenha o corpo 
    global turtle
    turtle.pu()
    turtle.goto(-212.13,212.13)
    turtle.right(-45)
    turtle.pd()

    turtle.fd(100)

def pernas():
    global turtle
    turtle.pu()
    turtle.goto(-212.13,112.13)
    turtle.pd()
   
    #desenha as pernas
    turtle.right(-45)
    turtle.fd(50)
    turtle.pu()
    turtle.backward(50)
    turtle.pd()
    turtle.right(90)
    turtle.fd(50)

#Mostra regras no inicio ao usuario
def inicio():
    from time import sleep
    escritor.pu()
    escritor.write('=======================', align ='left')
    escritor.right(90)
    escritor.fd(10)
    escritor.write('   FORCA DE PALAVRAS   ', align ='left')
    escritor.fd(10)
    escritor.write('=======================', align ='left')
    escritor.fd(15)
    escritor.write('Seu objetivo é tentar acertar a palavra secreta', align ='left')
    escritor.fd(15)
    escritor.write('Você terá que tentar uma letra por vez', align ='left')
    escritor.fd(15)
    escritor.write('Você pode errar até 5 vezes', align ='left')
    escritor.fd(15)
    escritor.write('para sair, digite a qualquer momento "sair"', align ='left')
    sleep(5)
    forca()
    escritor.clear()

#define o tema da forca
def escolher_tema():
    from os import system
    from time import sleep
    global palavras, dica0, dica1, dica2 
    
    while True:
        tema = textinput("Escolha o tema que você deseja jogar:", "[1] programação, [2] frutas, [3] séries")
        
        if (tema == '1'): 
            palavras = ['ALGORITMOS', 'PYTHON', 'HTML'] 

            dica0 = 'é a primeira matéria do curso relacionada a programação'  
            dica1 = 'é uma liguagem orientada a objetos'  
            dica2 = 'é uma linguagem de marcação' 

            return palavras, dica0, dica1, dica2 
        
            break 
        
        elif (tema == '2'): 
            palavras = ['MARACUJÁ', 'PITAYA', 'KIWI'] 

            dica0 = 'é uma delícia no mousse' 
            dica1 = 'a fruta do dragão' 
            dica2 = 'é verde e tem pontinhos' 

            return palavras, dica0, dica1, dica2 
        
            break 

        elif (tema == '3'):
            palavras = ['FRIENDS', 'BRIDGERTON', 'MANIFEST']

            dica0 = 'bebem muito café' 
            dica1 = 'série de época com orquestra pop' 
            dica2 = 'voo 828' 

            return palavras, dica0, dica1, dica2 
        
            break 

        else:
            print('número inválido, tente novamente (:') 

#escolhe a palavra a ser trabalhada na forca
def escolher_palavra():
    from random import randint #importa do random o comando randint
    global palavras, palavra, dica #pega as variaveis retornadas na função anterior que foram declaras no escopo
    x = randint(0,2)
    palavra = palavras[x] #escolhe um item na lista de palavras utilizando sua posição como referência
    
    if (x == 0):
        dica = dica0
    elif (x == 1):
        dica = dica1
    elif (x == 2):
        dica = dica2
    return palavra, dica #retorna a palavra no escopo

#analiza uma letra digitada
def analiza_letra():
    escritor.home()
    escritor.right(90)
    global letra, palavra, letras_escolhidas, erros, dica #pega a letra e outras variaveis no escopo

    if(len(letra) == 1 and letra != ' ' and letra.isalpha()): #verifica se o usuario digitou uma só letra
        if (letra in palavra): # verifica se a letra esta na palavra
            pos = 0
            while(pos < len(palavra)): #repete a quantidade de letras na palavra 
                if letra == palavra[pos]: #se a lettra for igual a letra da posição na palavra
                    estadoAtual[pos] = letra #adiciona no estado atual
                pos += 1 #encrementa um 
            escritor.write('a palavra ficou assim:', align = 'left')
            escritor.fd(15)
            escritor.write(estadoAtual, align = 'left')

        elif (letra not in palavra):
            escritor.fd(15)
            escritor.write(f'{letra} não faz parte da palavra', align = 'left')
            if erros < 2:
                escritor.fd(15)
                escritor.write(f'dica: a palavra tem {len(palavra)} letras', align = 'left')
            elif erros == 3 or erros == 4:
                escritor.fd(15)
                escritor.write('toma mais uma dica: '+ dica, align = 'left')
            erros += 1

    elif(letra == 'SAIR'):
        erros = 7
    else:
        escritor.fd(15)
        escritor.write('carácter inválido, tente novamente', align = 'left')

    
    return letras_escolhidas, erros,

#analisa se o estado atual da palavra está completo
def verifica_acerto(estado):
    global palavra
    
    estadoo = ''
    for l in estado:
        estadoo = estadoo+l

    if (estadoo == palavra):
        return True
    else:
        return False

'''
inicio()

escolher_tema()

escolher_palavra()

#print(palavra) #apenas para testes 

estadoAtual = ['_']*len(palavra)
letras_escolhidas = []

erros = 0

while True:
    letra = textinput("JOGO DA FORCA", "Digite uma letra:")
    letra = letra.upper()
    
    if (letra not in letras_escolhidas):
        analiza_letra()
    else:
        escritor.home()
        escritor.write('você já tentou essa letra, tente novamente', align ='left')
    
    letras_escolhidas.append(letra)
    
    if (verifica_acerto(estadoAtual)):
        escritor.home()
        escritor.fd(15)
        escritor.write('parabéns, vc acertou!!!', align ='left')
        break
    elif (erros == 5):
        escritor.home()
        escritor.fd(15)
        escritor.write('vc perdeu:(', align ='left')
        break
    elif (erros == 7):
        escritor.home()
        escritor.fd(15)
        escritor.write ('até mais!!!', align ='left')
        pernas()
        break
    if(erros == 1):
        cabeca()
    
    elif(erros == 2):
        braco1()
    
    elif(erros == 3):
        braco2()

    elif(erros == 4):
        corpo()


    sleep(3)
    escritor.clear()
'''
forca()
cabeca()
braco1()
braco2()
corpo()
pernas()
main.mainloop()


