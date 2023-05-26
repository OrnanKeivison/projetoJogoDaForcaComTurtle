from interface import *

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

inicio()

forca()
cabeca()
braco1()
braco2()
corpo()
pernas()
main.mainloop()

