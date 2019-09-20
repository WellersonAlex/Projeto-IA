import copy

def mostarTabuleiro(tabuleiro):
    print("Tabuleiro inicial, nó percorido:", tabuleiro[3][0])
    print(tabuleiro[0])
    print(tabuleiro[1])
    print(tabuleiro[2])

def tabuleirosIguais(tabuleiro1, tabuleiro2):
    iguais = True
    for i in range(3):
        for j in range(3):
            if (tabuleiro1[i][j] != tabuleiro2[i][j]):
                iguais = False
    return iguais

def expandindoTabuleiro(tabuleiro):
    possiveisJogadas = []

    if(tabuleiro[1][1] == 0):
        copiaTabuleiro = copy.deepcopy(tabuleiro)
        copiaTabuleiro[1][1] = copiaTabuleiro[0][1]
        copiaTabuleiro[0][1] = 0
        copiaTabuleiro[3][0] = copiaTabuleiro[3][0]+1 
        copiaTabuleiro[3][1] = tabuleiro
        possiveisJogadas.append(copiaTabuleiro)

        copiaTabuleiro = copy.deepcopy(tabuleiro)
        copiaTabuleiro[1][1] = copiaTabuleiro[2][1]
        copiaTabuleiro[2][1] = 0
        copiaTabuleiro[3][0] = copiaTabuleiro[3][0]+1 
        copiaTabuleiro[3][1] = tabuleiro
        possiveisJogadas.append(copiaTabuleiro)

        copiaTabuleiro = copy.deepcopy(tabuleiro)
        copiaTabuleiro[1][1] = copiaTabuleiro[1][2]
        copiaTabuleiro[1][2] = 0
        copiaTabuleiro[3][0] = copiaTabuleiro[3][0]+1 
        copiaTabuleiro[3][1] = tabuleiro    
        possiveisJogadas.append(copiaTabuleiro)

        copiaTabuleiro = copy.deepcopy(tabuleiro)
        copiaTabuleiro[1][1] = copiaTabuleiro[1][0]
        copiaTabuleiro[1][0] = 0
        copiaTabuleiro[3][0] = copiaTabuleiro[3][0]+1 
        copiaTabuleiro[3][1] = tabuleiro
        possiveisJogadas.append(copiaTabuleiro)
        
    elif(tabuleiro[0][0] == 0):
        copiaTabuleiro = copy.deepcopy(tabuleiro)
        copiaTabuleiro[0][0] = copiaTabuleiro[1][0]
        copiaTabuleiro[1][0] = 0
        copiaTabuleiro[3][0] = copiaTabuleiro[3][0]+1 
        copiaTabuleiro[3][1] = tabuleiro
        possiveisJogadas.append(copiaTabuleiro)

        copiaTabuleiro = copy.deepcopy(tabuleiro)
        copiaTabuleiro[0][0] = copiaTabuleiro[0][1]
        copiaTabuleiro[0][1] = 0
        copiaTabuleiro[3][0] = copiaTabuleiro[3][0]+1 
        copiaTabuleiro[3][1] = tabuleiro
        possiveisJogadas.append(copiaTabuleiro)

    elif(tabuleiro[0][2] == 0):
        copiaTabuleiro = copy.deepcopy(tabuleiro)
        copiaTabuleiro[0][2] = copiaTabuleiro[1][2]
        copiaTabuleiro[1][2] = 0
        copiaTabuleiro[3][0] = copiaTabuleiro[3][0]+1 
        copiaTabuleiro[3][1] = tabuleiro
        possiveisJogadas.append(copiaTabuleiro)

        copiaTabuleiro = copy.deepcopy(tabuleiro)
        copiaTabuleiro[0][2] = copiaTabuleiro[0][1]
        copiaTabuleiro[0][1] = 0
        copiaTabuleiro[3][0] = copiaTabuleiro[3][0]+1 
        copiaTabuleiro[3][1] = tabuleiro
        possiveisJogadas.append(copiaTabuleiro)

    elif(tabuleiro[2][0] == 0):
        copiaTabuleiro = copy.deepcopy(tabuleiro)
        copiaTabuleiro[2][0] = copiaTabuleiro[1][0]
        copiaTabuleiro[1][0] = 0
        copiaTabuleiro[3][0] = copiaTabuleiro[3][0]+1 
        copiaTabuleiro[3][1] = tabuleiro
        possiveisJogadas.append(copiaTabuleiro)

        copiaTabuleiro = copy.deepcopy(tabuleiro)
        copiaTabuleiro[2][0] = copiaTabuleiro[2][1]
        copiaTabuleiro[2][1] = 0
        copiaTabuleiro[3][0] = copiaTabuleiro[3][0]+1 
        copiaTabuleiro[3][1] = tabuleiro
        possiveisJogadas.append(copiaTabuleiro)

    elif(tabuleiro[2][2] == 0):
        copiaTabuleiro = copy.deepcopy(tabuleiro)
        copiaTabuleiro[2][2] = copiaTabuleiro[1][2]
        copiaTabuleiro[1][2] = 0
        copiaTabuleiro[3][0] = copiaTabuleiro[3][0]+1 
        copiaTabuleiro[3][1] = tabuleiro
        possiveisJogadas.append(copiaTabuleiro)
            
        copiaTabuleiro = copy.deepcopy(tabuleiro)
        copiaTabuleiro[2][2] = copiaTabuleiro[2][1]
        copiaTabuleiro[2][1] = 0
        copiaTabuleiro[3][0] = copiaTabuleiro[3][0]+1 
        copiaTabuleiro[3][1] = tabuleiro
        possiveisJogadas.append(copiaTabuleiro)

    elif(tabuleiro[0][1] == 0):
        copiaTabuleiro = copy.deepcopy(tabuleiro)
        copiaTabuleiro[0][1] = copiaTabuleiro[2][1]
        copiaTabuleiro[2][1] = 0
        copiaTabuleiro[3][0] = copiaTabuleiro[3][0]+1 
        copiaTabuleiro[3][1] = tabuleiro
        possiveisJogadas.append(copiaTabuleiro)

        copiaTabuleiro = copy.deepcopy(tabuleiro)
        copiaTabuleiro[0][1] = copiaTabuleiro[0][0]
        copiaTabuleiro[0][0]= 0
        copiaTabuleiro[3][0] = copiaTabuleiro[3][0]+1 
        copiaTabuleiro[3][1] = tabuleiro
        possiveisJogadas.append(copiaTabuleiro)

        copiaTabuleiro = copy.deepcopy(tabuleiro)
        copiaTabuleiro[0][1] = copiaTabuleiro[0][2]
        copiaTabuleiro[0][2] = 0
        copiaTabuleiro[3][0] = copiaTabuleiro[3][0]+1 
        copiaTabuleiro[3][1] = tabuleiro
        possiveisJogadas.append(copiaTabuleiro)

    elif(tabuleiro[2][1] == 0):
        copiaTabuleiro = copy.deepcopy(tabuleiro)
        copiaTabuleiro[2][1] = copiaTabuleiro[1][1]
        copiaTabuleiro[1][1] = 0
        copiaTabuleiro[3][0] = copiaTabuleiro[3][0]+1 
        copiaTabuleiro[3][1] = tabuleiro
        possiveisJogadas.append(copiaTabuleiro)

        copiaTabuleiro = copy.deepcopy(tabuleiro)
        copiaTabuleiro[2][1] = copiaTabuleiro[2][2]
        copiaTabuleiro[2][2] = 0
        copiaTabuleiro[3][0] = copiaTabuleiro[3][0]+1 
        copiaTabuleiro[3][1] = tabuleiro
        possiveisJogadas.append(copiaTabuleiro)

        copiaTabuleiro = copy.deepcopy(tabuleiro)
        copiaTabuleiro[2][1] = copiaTabuleiro[2][0]
        copiaTabuleiro[2][0] = 0
        copiaTabuleiro[3][0] = copiaTabuleiro[3][0]+1 
        copiaTabuleiro[3][1] = tabuleiro
        possiveisJogadas.append(copiaTabuleiro)

    elif(tabuleiro[1][0] == 0):
        copiaTabuleiro = copy.deepcopy(tabuleiro)
        copiaTabuleiro[1][0] = copiaTabuleiro[2][0]
        copiaTabuleiro[2][0] = 0
        copiaTabuleiro[3][0] = copiaTabuleiro[3][0]+1 
        copiaTabuleiro[3][1] = tabuleiro
        possiveisJogadas.append(copiaTabuleiro)

        copiaTabuleiro = copy.deepcopy(tabuleiro)
        copiaTabuleiro[1][0] = copiaTabuleiro[0][0]
        copiaTabuleiro[0][0] = 0
        copiaTabuleiro[3][0] = copiaTabuleiro[3][0]+1 
        copiaTabuleiro[3][1] = tabuleiro
        possiveisJogadas.append(copiaTabuleiro)

        copiaTabuleiro = copy.deepcopy(tabuleiro)
        copiaTabuleiro[1][0] = copiaTabuleiro[1][1]
        copiaTabuleiro[1][1] = 0
        copiaTabuleiro[3][0] = copiaTabuleiro[3][0]+1 
        copiaTabuleiro[3][1] = tabuleiro
        possiveisJogadas.append(copiaTabuleiro)

    elif(tabuleiro[1][2] == 0):
        copiaTabuleiro = copy.deepcopy(tabuleiro)
        copiaTabuleiro[1][2] = copiaTabuleiro[2][2]
        copiaTabuleiro[2][2] = 0
        copiaTabuleiro[3][0] = copiaTabuleiro[3][0]+1 
        copiaTabuleiro[3][1] = tabuleiro
        possiveisJogadas.append(copiaTabuleiro)

        copiaTabuleiro = copy.deepcopy(tabuleiro)
        copiaTabuleiro[1][2] = copiaTabuleiro[0][2]
        copiaTabuleiro[0][2] = 0
        copiaTabuleiro[3][0] = copiaTabuleiro[3][0]+1 
        copiaTabuleiro[3][1] = tabuleiro
        possiveisJogadas.append(copiaTabuleiro)

        copiaTabuleiro = copy.deepcopy(tabuleiro)
        copiaTabuleiro[1][2] = copiaTabuleiro[1][1]
        copiaTabuleiro[1][1] = 0
        copiaTabuleiro[3][0] = copiaTabuleiro[3][0]+1 
        copiaTabuleiro[3][1] = tabuleiro
        possiveisJogadas.append(copiaTabuleiro)
    
    return possiveisJogadas

def heuristica(tabuleiro):
    valorH = 0
    for i in range(3):
        for j in range(3):
            if(tabuleiro[i][j] == 0):
                valorH = valorH + abs(0-i) + abs(0-j)
            if(tabuleiro[i][j] == 1):
                valorH = valorH + abs(0-i) + abs(1-j)
            if(tabuleiro[i][j] == 2):
                valorH = valorH + abs(0-i) + abs(2-j)
            if(tabuleiro[i][j] == 3):
                valorH = valorH + abs(1-i) + abs(0-j)
            if(tabuleiro[i][j] == 4):
                valorH = valorH + abs(1-i) + abs(1-j)
            if(tabuleiro[i][j] == 5):
                valorH = valorH + abs(1-i) + abs(2-j)
            if(tabuleiro[i][j] == 6):
                valorH = valorH + abs(2-i) + abs(0-j)
            if(tabuleiro[i][j] == 7):
                valorH = valorH + abs(2-i) + abs(1-j)
            if(tabuleiro[i][j] == 8):
                valorH = valorH + abs(2-i) + abs(2-j)
    return valorH

def jogadasRealizadas(tabuleiro):
    print("\nEssas foram as jogadas realizadas:")
    pilha = []
    while(tabuleiro[3][1] != None):
        pilha.append(tabuleiro)
        tabuleiro = tabuleiro[3][1]
    pilha.append(tabuleiro)
    while(len(pilha) > 0):
        temp = pilha.pop()
        mostarTabuleiro(temp)

def realizarBuscaAStar(tabuleiroI, tabuleiroR):
    fila = []
    filaRepetidos = []
    fila.append(tabuleiroI)
    filaRepetidos.append(tabuleiroI)
    nosExpandidos = 0

    while (len(fila)):
        
        if(len(tabuleiroI) == 0 or len(tabuleiroR) == 0):
            return False

        temp = fila.pop(0)
        nosExpandidos +=1

        print("\nNó expandido: ",nosExpandidos)
        mostarTabuleiro(temp)
        
        if(tabuleirosIguais(temp,tabuleiroR)):
            print("\n*****************************************"+
            "\n|----------SOLUÇÃO ENCONTRADA-----------|"+
            "\n*****************************************")
            jogadasRealizadas(temp)
            break;
        
        else:
            filhos = expandindoTabuleiro(temp)
            filhosSemRepetir = []
            
            for n in filhos:
                jaExiste = False
            
                for x in filaRepetidos:
            
                    if(tabuleirosIguais(n,x)):
                        jaExiste = True
                        break
            
                if(jaExiste == False):
                    filhosSemRepetir.append(n)
            
            valorHeuristica = 1000
            
            for r in filhosSemRepetir:
                if(heuristica(r) < valorHeuristica):
                    valorHeuristica = heuristica(r)
            
            for r in filhosSemRepetir:
                if(heuristica(r) == valorHeuristica):
                    fila.append(r)
                    filaRepetidos.append(r)
                



tabuleiroInicial = [[2,5,8],[1,0,7],[3,4,6],[0,None]]
#tabuleiroInicial = [[0,1,2],[3,4,5],[6,7,8],[0,None]]
tabuleiroObjetivo = [[0,1,2],[3,4,5],[6,7,8],[0,None]]

mostarTabuleiro(tabuleiroInicial)
realizarBuscaAStar(tabuleiroInicial,tabuleiroObjetivo)

    