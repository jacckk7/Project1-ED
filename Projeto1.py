#####################################################################################################
###################################### Projeto 1 de ED ##############################################
################################## Breno Costa Avelino Lima #########################################
#####################################################################################################


#####################################################################################################
##################################### classes definition ############################################
#####################################################################################################

class Pilha:
    def __init__(self):
        self.items = []

    def vazia(self):
        return self.items == []

    def colocar(self, item):
        self.items.append(item)

    def tirar(self):
        return self.items.pop()

    def ver_topo(self):
        return self.items[len(self.items)-1]

    def tamanho(self):
        return len(self.items)


class Fila:
    def __init__(self):
        self.items = []

    def vazia(self):
        return self.items == []

    def enfileirar(self, item):
        self.items.insert(0, item)

    def desenfileirar(self):
        return self.items.pop()

    def tamanho(self):
        return len(self.items)


#####################################################################################################
#################################### functions definition ###########################################
#####################################################################################################

def crypto(instancia):
    p_crypto = Pilha()
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    frase = ''

    for i in range(len(instancia[0]) + 1):
        p_crypto.colocar(numeros[i])

        if i == len(instancia[0]) or instancia[0][i] == '+':
            while not p_crypto.vazia():
                frase = frase + p_crypto.tirar()

    return frase


def deYodafy(instancia):
    p_deY = Pilha()
    frase = ''
    instancia[-1], ponto = instancia[-1][0:len(
        instancia[-1]) - 1], instancia[-1][len(instancia[-1]) - 1:]

    for i in range(len(instancia)):
        p_deY.colocar(instancia[i])

    while not p_deY.vazia():
        frase = frase + p_deY.tirar() + ' '

    frase = frase[0:len(frase) - 1] + ponto

    return frase


def merge(instancia):
    lista_hold = []
    lista = []
    resposta = []
    frase = ''

    for elemento in instancia:
        if elemento[-1] == ',':
            lista_hold.append(int(elemento[1:len(elemento) - 1]))
        else:
            lista_hold.append(int(elemento[0:len(elemento) - 1]))

    for j in range(0, len(lista_hold), 2):
        lista.append([lista_hold[j], lista_hold[j + 1]])

    lista = sorted(lista, reverse=True)

    intervalo = lista.pop()
    while len(lista) > 0:
        if intervalo[1] >= lista[-1][0]:
            if intervalo[1] < lista[-1][1]:
                intervalo[1] = lista[-1][1]
                lista.pop()
            else:
                lista.pop()
        else:
            resposta.append(intervalo)
            intervalo = lista.pop()

    resposta.append(intervalo)

    for k in range(len(resposta)):
        frase = frase + str(resposta[k]) + ' '

    return frase[0:len(frase) - 1]


#####################################################################################################
######################################## main function ##############################################
#####################################################################################################

num_processos = []
comandos = Fila()

while True:
    processo = list(input().split())
    if processo[0] == 'halt':
        num_processos = comandos.tamanho()
        num_comandos = 0
        for j in range(num_processos):
            num_comandos += comandos.desenfileirar().tamanho()

        print(f'{num_processos} processo(s) e {num_comandos} comando(s) órfão(s).')
        break

    elif processo[0] == 'add':
        processos = Fila()

        for i in range(int(processo[1])):
            comando_instancia = list(input().split())
            comando, instancia = comando_instancia[0], comando_instancia[1:len(
                comando_instancia)]

            if comando == 'crypto':
                processos.enfileirar(crypto(instancia))
            elif comando == 'deYodafy':
                processos.enfileirar(deYodafy(instancia))
            elif comando == 'merge':
                processos.enfileirar(merge(instancia))

        comandos.enfileirar(processos)

    elif processo[0] == 'process':
        if comandos.vazia():
            continue
        else:
            hold = comandos.desenfileirar()

            if hold.tamanho() < 2:
                print(hold.desenfileirar())
            else:
                print(hold.desenfileirar())
                comandos.enfileirar(hold)
