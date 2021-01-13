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
    for i in range(166):
        novovalor = valoresdex[-1] + 0.09
        valoresdex.append(novovalor)

    return valoresdex

def equacao_resistencia(valores, variacao):
    if variacao == 'ro':

        r = valores[0]*float(valores[1])/float(valores[2])

    if variacao == 'l':

        r = float(valores[0])*valores[1]/float(valores[2])

    if variacao == 'a':

        r = float(valores[0]) * float(valores[1]) / valores[2]

    return r

variacao=input('O que vai variar? ro / l / a \n\n')

if variacao == 'ro':

    nomedex    = "Resistividade (Ωcm)"
    nomedey    = "Resistência (ohms)"
    valoresdex = valores_resistividade_varia()
    valoresder = []
    l = input('Qual é o valor de L? \n \n')
    a = input('Qual é o valor de a? \n\n')

    for i in valoresdex:

        valores = [i, l, a]
        r = equacao_resistencia(valores, variacao)
        valoresder.append(r)

if variacao == 'l':

    nomedex = "Comprimento (cm)"
    nomedey = "Resistência (ohms)"
    valoresdex = valores_comprimento_varia()
    valoresder = []
    ro = input('Qual é o valor de ro? \n \n')
    a  = input('Qual é o valor de a? \n\n')

    for i in valoresdex:

        valores = [ro, i, a]
        r = equacao_resistencia(valores, variacao)
        valoresder.append(r)

if variacao == 'a':

    nomedex = "Área (cm²)"
    nomedey = "Resistência (ohms)"
    valoresdex = valores_area_varia()
    valoresder = []
    ro = input('Qual é o valor de ro? \n \n')
    l  = input('Qual é o valor de l? \n\n')

    for i in valoresdex:

        valores = [ro, l, i]
        r = equacao_resistencia(valores, variacao)
        valoresder.append(r)

plt.plot(valoresdex, valoresder) #criando o gráfico
plt.title('Resistência em um fio\n(Resistence in a wire)') #adicionando o título
plt.xlabel(nomedex)
plt.ylabel(nomedey)
plt.show()

print(valoresdex)
print(valoresder)