from time import sleep
from os import system

#Mostra regras no inicio ao usuario
def inicio():
    from os import system
    from time import sleep
    print('=======================')
    print('   FORCA DE PALAVRAS   ')
    print('=======================')
    print('Seu objetivo é tentar acertar a palavra secreta')
    print('Você terá que tentar uma letra por vez')
    print('Você pode errar até 5 vezes')
    print('para sair, digite a qualquer momento "sair"')
    sleep(3)
    system('cls') or None

#define o tema da forca
def escolher_tema():
    from os import system
    from time import sleep
    global palavras, dica0, dica1, dica2 #define variáveis vo escopo do código 
    
    while True:#enquanto for verdade (loop infinito)
        tema  = input(''' agora, escolha o tema que você deseja jogar: 
                        [1] programação
                        [2] frutas
                        [3] séries
                        ''') #pergunta qual tema o usuário deseja jogar na forca 
        sleep(3)
        system('cls') or None
        
        if (tema == '1'): #se o usuario digitar '1'
            palavras = ['ALGORITMOS', 'PYTHON', 'HTML'] #define as palavras que podem ser escolhidas 

            dica0 = 'é a primeira matéria do curso relacionada a programação'  #define dica para palavra 0
            dica1 = 'é uma liguagem orientada a objetos'  #define dica para palavra 1
            dica2 = 'é uma linguagem de marcação' #define dica para palavra 2

            return palavras, dica0, dica1, dica2 #retorna variaveis ao escopo 
        
            break #para o loop
        
        elif (tema == '2'): #se o usuario digitar '2'
            palavras = ['MARACUJÁ', 'PITAYA', 'KIWI'] #define as palavras que podem ser escolhidas

            dica0 = 'é uma delícia no mousse' #define dica para palavra 0
            dica1 = 'a fruta do dragão' #define dica para palavra 1 
            dica2 = 'é verde e tem pontinhos' #define dica para palavra 2

            return palavras, dica0, dica1, dica2 #retorna variaveis ao escopo 
        
            break #para o loop

        elif (tema == '3'): #se o usuario digitar '3'
            palavras = ['FRIENDS', 'BRIDGERTON', 'MANIFEST'] #define as palavras que podem ser escolhidas

            dica0 = 'bebem muito café' #define dica para palavra 0
            dica1 = 'série de época com orquestra pop' #define dica para palavra 1
            dica2 = 'voo 828' #define dica para palavra 2

            return palavras, dica0, dica1, dica2 #retorna variaveis ao escopo
        
            break #para o loop

        else: # se a opção digitada não for 1, 2 ou 3
            print('número inválido, tente novamente (:') #manda o usuario tentar novamente e não para o loop
  
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
    global letra, palavra, letras_escolhidas, erros, dica #pega a letra e outras variaveis no escopo

    if(len(letra) == 1 and letra != ' ' and letra.isalpha()): #verifica se o usuario digitou uma só letra
        if (letra in palavra): # verifica se a letra esta na palavra
            pos = 0
            while(pos < len(palavra)): #repete a quantidade de letras na palavra 
                if letra == palavra[pos]: #se a lettra for igual a letra da posição na palavra
                    estadoAtual[pos] = letra #adiciona no estado atual
                pos += 1 #encrementa um 
            print('a palavra ficou assim:')
            print(estadoAtual)

        elif (letra not in palavra):
            print(f'{letra} não faz parte da palavra')
            if erros < 2:
                print(f'dica: a palavra tem {len(palavra)} letras')
            elif erros == 3 or erros == 4:
                print('toma mais uma dica:',dica)
            erros += 1

    elif(letra == 'SAIR'):
        erros = 2007
    else:
        print('carácter inválido, tente novamente')

    
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


inicio()

escolher_tema()

escolher_palavra()

#print(palavra) #apenas para testes 

estadoAtual = ['_']*len(palavra)
letras_escolhidas = []

erros = 0

while True:
    letra = input('digite uma letra: ')
    letra = letra.upper()
    
    if (letra not in letras_escolhidas):
        analiza_letra()
    else:
        print('você já tentou essa letra, tente novamente')
    
    letras_escolhidas.append(letra)
    
    if (verifica_acerto(estadoAtual)):
        print('parabéns, vc acertou!!!')
        break
    elif (erros == 5):
        print('vc perdeu:(')
        break
    elif (erros == 2007):
        print ('até mais!!!')
        break

    sleep(3)
    system('cls') or None