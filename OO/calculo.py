import math


def calcula_corda():
    numero_furo = int(input("Número de furo: "))
    diametro = float(input("Diâmetro do Furo: "))
    centro = float(input("Centro a Centro da furacão: "))

    angulo = 360 / numero_furo / 2
    resultado_final = math.sin(math.pi / 180.0 * angulo) * centro - diametro

    resultado_formatado = "{:.2f}".format(resultado_final)

    print(f"A distância entre furo é {resultado_formatado}.")


if __name__ == "__main__":
    calcula_corda()
