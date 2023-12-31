import random
def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")
    total_de_tentativas = 0

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 5
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Define o nivel: "))

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas+1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite o seu número: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você precisa digitar um número entre 1 e 100")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou e fez {:3.0f} pontos.".format(pontos))
            break
        else:
            if (maior):
                print("Você errou! O seu chute foi maior que o número secreto.")
                pontos_perdidos = abs(numero_secreto - chute) / 3
                pontos = pontos - pontos_perdidos
            elif (menor):
                print("Você errou! O seu chute foi menor que o número secreto.")
                pontos_perdidos = abs(numero_secreto - chute) / 3
                pontos = pontos - pontos_perdidos
        if rodada == total_de_tentativas:
            print("Você esgotou o numero de tentativas, o numero secreto era {}".format(numero_secreto))
        else:
            continue
    else:
        print("Fim do jogo")
if (__name__ == "__main__"):
    jogar()