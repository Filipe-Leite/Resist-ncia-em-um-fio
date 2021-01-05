import matplotlib.pyplot as plt

def valores_resistividade_varia():
    valoresdex=[0.01]
    for i in range(99):
        novovalor=valoresdex[-1]+0.01
        valoresdex.append(novovalor)

    return valoresdex

def valores_comprimento_varia():
    valoresdex=[0.10]
    for i in range(199):
        novovalor=valoresdex[-1]+0.10
        valoresdex.append(novovalor)

    return valoresdex


def valores_area_varia():
    valoresdex = [0.01]
    for i in range(149):
        novovalor = valoresdex[-1] + 0.09
        valoresdex.append(novovalor)

    return valoresdex

variacao=input('O que vai variar? ro / l / a \n\n')

if variacao == 'ro':

    nomedex    = "Resistividade"
    nomedey    = "Resistência"
    valoresdex = valores_resistividade_varia()
    valoresdex_to_del = valoresdex[:]
    valoresder = []
    l = float(input('Qual é o valor de L? \n \n'))
    a = float(input('Qual é o valor de a? \n\n'))

    while len(valoresdex_to_del) != 0:

        valores = [valoresdex_to_del[0], l, a]

        valores = valores
        r = valores[0] * valores[1]
        r = r/valores[2]
        valoresder.append(r)
        del valoresdex_to_del[0]

if variacao == 'l':

    nomedex = "Comprimento"
    nomedey = "Resistência"
    valoresdex = valores_comprimento_varia()
    valoresdex_to_del = valoresdex[:]
    valoresder = []
    ro = float(input('Qual é o valor de ro? \n \n'))
    a = float(input('Qual é o valor de a? \n\n'))

    while len(valoresdex_to_del) != 0:

        valores = [valoresdex_to_del[0], ro, a]

        valores = valores
        r = valores[0] * valores[1]
        r = r/valores[2]
        valoresder.append(r)
        del valoresdex_to_del[0]

if variacao == 'a':

    nomedex = "Área"
    nomedey = "Resistência"
    valoresdex = valores_area_varia()
    valoresdex_to_del = valoresdex[:]
    valoresder = []
    ro = float(input('Qual é o valor de ro? \n \n'))
    l = float(input('Qual é o valor de l? \n\n'))

    while len(valoresdex_to_del) != 0:

        valores = [valoresdex_to_del[0], ro, l]

        valores = valores
        r = valores[0] * valores[1]
        r = r/valores[2]
        valoresder.append(r)
        del valoresdex_to_del[0]


plt.plot(valoresdex, valoresder) #Criando o gráfico
plt.title('Resistência em um fio') #adicionando o título
plt.xlabel(nomedex)
plt.ylabel(nomedey)
plt.show()

print(valoresdex)
print(valoresder)