import random


def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


def carrega_palavra_secreta():
    arquivo = open("palavra.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip().upper()
        palavras.append(linha)


    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero]

    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    return ["_" for _ in palavra]


def pede_chute():
    chute = input("Qual é a letra?")
    chute = chute.strip().upper()
    return chute


def marca_chute_correto(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if chute.upper() == letra.upper():
            letras_acertadas[index] = letra
        index += 1


def imprime_mensagem_vencedor(erros, tentativas):
    print("Voce acertou com {1} tentativas e teve {0} erro(s)".format(erros, tentativas))


def imprime_mensagem_perdedor(erros, tentativas, palavra_secreta):
    print(f"Voce foi enforcado, teve {tentativas} tentativas com {erros} erros e a palavra era {palavra_secreta}")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def jogar():
    imprime_mensagem_abertura()

    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0
    tentativas = 0

    print(letras_acertadas)

    while not enforcou and not acertou:

        chute = pede_chute()
        tentativas += 1
        if chute in palavra_secreta:

            marca_chute_correto(chute, palavra_secreta, letras_acertadas)

        else:
            erros += 1
            desenha_forca(erros)
        enforcou = erros == 6

        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    if acertou:
        imprime_mensagem_vencedor(erros, tentativas)

    elif enforcou:
        imprime_mensagem_perdedor(erros, tentativas, palavra_secreta)


if __name__ == "__main__":
    jogar()
