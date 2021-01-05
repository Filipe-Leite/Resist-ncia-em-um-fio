# A equação é R = ro(L/A)
# Onde R é a resistência
# ro é a resistividade do material
# L é o comprimento do fio
# A é a área do fio

ro = float(input("Qual o valor de rô?"))
l  = float(input("Qual o valor do comprimento do fio?"))
a  = float(input("Qual o valor da área?"))

valores = [ro, l, a]

def equacao_resistencia(valores):
    r = valores[0]*(valores[1]/valores[2])

    return r


equacao_resistencia=equacao_resistencia(valores)

