from math import *
import os

# Consts
C_LUZ = 3E8
U0 = 4E-7*pi

# Functions


def cleanup():  # Cleans everything on terminal
    os.system('cls') or None


def ra():  # Show students Register

    ra = """        Integrantes do grupo:
        Caio de Souza Conceição - RA: 22.122.033-8
        Samir Oliveira da Costa - RA: 22.122.030-4
        Lucas Rebouças Silva    - Ra: 22.122.048-6

O programa tem o intuito de realizar cálculos físicos relacionados a ondas eletromagnéticas, podendo ter como entrada as seguintes variáveis:
1 - (Em) Campo Elétrico (V/m): medida da força elétrica exercida por uma carga elétrica em um ponto do espaço.
2 - (Bm) Campo Magnético (T): medida da força magnética exercida por um campo magnético em um ponto do espaço.
3 - (I) Intensidade (W/m^2): medida da quantidade de energia que atravessa uma área em um segundo.
4 - (f) Frequência (Hz): número de ciclos completos de uma onda que ocorrem em um segundo.
5 - (λ) Comprimento de onda (m): distância entre dois pontos consecutivos de uma onda que estejam em fase.
6 - (k) Número de Ondas (rad/m): medida da quantidade de oscilações por unidade de comprimento.
7 - (w) Frequência Angular (rad/s): medida da velocidade angular com que uma onda oscila, em radianos por segundo.

    Ao utilizar o programa, note que as unidades de medida de entrada já estão previamente definidas, então confira a unidade antes de inseri-la
no programa, como converter μT para T antes de executar comandos com o campo magnético.
    """
    print(ra)
    v = input(
        "Se estiver pronto(a) para usar o aplicativo, clique no terminal e aperte ENTER.")


def to_decimal(value):  # Accepts a scietific number like 12E20 and returns it as a decimal
    return float(value)


# Receives a decimal number and transform it to scientific notation
def to_scientific_notation(value):
    return format(value, '.2E')


def menu():  # Main menu loop function
    cleanup()
    while True:
        menu = """               == Menu de escolha == 
            1 - (Em) Campo Elétrico (V/m)
            2 - (Bm) Campo Magnético (T)
            3 - (I) Intensidade (W/m^2)
            4 - (f) Frequência (Hz)
            5 - (λ) Comprimento de onda (m)
            6 - (k) Número de Ondas (rad/m)
            7 - (w) Frequência Angular (rad/s)
            """

        print(menu)
        try:
            x = int(input("Digite o dado que possui: "))
        except:
            print("Error: Invalid number.")
            exit(0)

        value = input(
            "Digite o valor da variável (Aceita notação científica (Ex: 320E-20)): ")
        decimal_value = to_decimal(value)

        for element in [Em, Bm, I, f, k, w, λ]:
            element(x, decimal_value)

        print("Deseja continuar? (S/N)", end=" ")
        v = input()
        if v == 'S' or v == 's':
            cleanup()
        elif v == "N" or v == "N":
            print("\nObrigado(a) por utilizar o aplicativo!")
            exit(0)
        else:
            print("Opção inválida. Tente novamente.")

# Each function calculates the variable written on the function sign, depending on the parameters given.


def Em(x, value):
    # 1 - (Em) Campo Elétrico (V/m)
    if x == 2:
        Em = value*C_LUZ
        print("Em (Campo Elétrico) = %s V/m\n" % to_scientific_notation(Em))
    elif x == 3:
        Em = sqrt(2*U0*C_LUZ*value)
        print("Em (Campo Elétrico) = %s V/m\n" % to_scientific_notation(Em))


def Bm(x, value):
    # 2 - (Bm) Campo Magnético (T)
    if x == 1:
        Bm = value/C_LUZ
        print("Bm (Campo Magnético) = %s T\n" % to_scientific_notation(Bm))
    elif x == 3:
        Bm = sqrt((value*2*U0)/C_LUZ)
        print("Bm (Campo Magnético) = %s T\n" % to_scientific_notation(Bm))


def I(x, value):
    # 3 - (I) Intensidade (W/m^2)
    if x == 1:
        I = (value)**2/(2*U0*C_LUZ)
        print("I (Intensidade) = %s W/m^2\n" % to_scientific_notation(I))
    elif x == 2:
        I = (C_LUZ*value**2)/(2*U0)
        print("I (Intensidade) = %s W/m^2\n" % to_scientific_notation(I))


def f(x, value):
    # 4 - (f) Frequência (Hz)
    if x == 5:
        f = C_LUZ/value
        print("f (Frequência) = %s Hz\n" % to_scientific_notation(f))
    elif x == 6:
        f = C_LUZ*value/(2*pi)
        print("f (Frequência) = %s Hz\n" % to_scientific_notation(f))
    elif x == 7:
        f = value/(2*pi)
        print("f (Frequência) = %s Hz\n" % to_scientific_notation(f))


def k(x, value):
    # 6 - (k) Número de Ondas (rad/m)
    if x == 4:
        k_aux = C_LUZ * (1/value)
        k = (2*pi)/k_aux
        print("k (Número de ondas) = %s rad/m\n" % to_scientific_notation(k))
    elif x == 5:
        k = (2*pi)/value
        print("k (Número de ondas) = %s rad/m\n" % to_scientific_notation(k))
    elif x == 7:
        k = value/C_LUZ
        print("k (Número de ondas) = %s rad/m\n" % to_scientific_notation(k))


def λ(x, value):
    # 5 - (λ) Comprimento de onda (m)
    if x == 4:
        λ = C_LUZ/value
        print("λ (Comprimento de onda) = %s m\n" % to_scientific_notation(λ))
    elif x == 6:
        λ = (2*pi)/value
        print("λ (Comprimento de onda) = %s m\n" % to_scientific_notation(λ))
    elif x == 7:
        T = (2*pi)/value
        λ = C_LUZ*T
        print("λ (Comprimento de onda) = %s m\n" % to_scientific_notation(λ))


def w(x, value):
    # 7 - (w) Frequência Angular (rad/s)
    if x == 4:
        w = 2*pi*value
        print("w (Frequência Angular) = %s rad/s\n" %
              to_scientific_notation(w))
    elif x == 5:
        T = value/C_LUZ
        w = (2*pi)/T
        print("w (Frequência Angular) = %s rad/s\n" %
              to_scientific_notation(w))
    elif x == 6:
        w = C_LUZ * value
        print("w (Frequência Angular) = %s rad/s\n" %
              to_scientific_notation(w))


ra()
menu()
