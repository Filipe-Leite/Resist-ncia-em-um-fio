# Este código plota os gráficos da resistência em um fio, dada pela equação r = rô*l/a (sendo "rô" a descrição dapropriedade resistiva
#       do material; "l" o comprimento do fio; e "a" a aréa do fio [um cilíndro]). Pedindo para o usuário entrar com um valor que vai variar
#       enquanto os outros dois valores valores da equação permanecerão constantes. O código cria duas listas, sendo definida na variável x (escolhida
#       pelo usuário) e outra lista será os valores de r (que será o y da função. A resistência calculada pela função "equacao_resistencia").

import matplotlib.pyplot as plt

# Esta função irá gerar uma lista com vários valores crescentes de "rô"

def valores_resistividade_varia():
    valoresdex=[0.01]
    for i in range(99):
        novovalor=valoresdex[-1]+0.01
        valoresdex.append(novovalor)

    return valoresdex

# Esta função irá gerar uma lista com vários valores crescentes de "l"

def valores_comprimento_varia():
    valoresdex=[0.10]
    for i in range(199):
        novovalor=valoresdex[-1]+0.10
        valoresdex.append(novovalor)

    return valoresdex

# Esta função irá gerar uma lista com vários valores crescentes de "a"

def valores_area_varia():
    valoresdex = [0.01]
    for i in range(166):
        novovalor = valoresdex[-1] + 0.09
        valoresdex.append(novovalor)

    return valoresdex

# Esta função irá calcular o valor da resistência a partir da equação da resistência

def equacao_resistencia(valores, variacao):
    if variacao == 'ro':

        r = valores[0]*float(valores[1])/float(valores[2])

    if variacao == 'l':

        r = float(valores[0])*valores[1]/float(valores[2])

    if variacao == 'a':

        r = float(valores[0]) * float(valores[1]) / valores[2]

    return r

# Aqui o usuário entrará com o que irá variar

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

# Esta parte do código irá plotar o gráfico        
        
plt.plot(valoresdex, valoresder) #criando o gráfico
plt.title('Resistência em um fio\n(Resistence in a wire)') #adicionando o título
plt.xlabel(nomedex)
plt.ylabel(nomedey)
plt.show()

print(valoresdex)
print(valoresder)
