import forca
import advinhacao_for
def escolhe_jogo():
    print("*********************************")
    print("Olá bem vindo, Escolha seu jogo!")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")
    jogo = int(input("Qual seu jogo ? "))

    if (jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif (jogo == 2):
        print("Jogando adivinhação")
        advinhacao_for.jogar()

if (__name__ == "__main__"):
    escolhe_jogo()