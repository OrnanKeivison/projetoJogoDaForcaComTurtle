from turtle import textinput
import turtle
import time
turtle = turtle.Turtle()
main = turtle.screen
escritor = turtle.clone()
turtle.speed(5) 
escritor.shape('turtle')
escritor.hideturtle()


nome = textinput("Python Guides", "Enter your Name")


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
    sleep(3)
    escritor.clear()



forca()
cabeca()
braco1()
braco2()
corpo()
pernas()

#inicio()



escritor.write('olá '+nome, align ='left')
time.sleep(5)
escritor.clear()

main.mainloop()


