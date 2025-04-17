import numpy as np
class Vetor_Ordenado():
    def __init__(self, capacidade):
        self.capacidade = capacidade #capacidade total do nosso vetor
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int) #preencher o vetor com espaços vazios do tipo inteiro

    def imprimir(self): #função para imprimir o vetor
        if self.ultima_posicao == -1:
                print("Vetor vazio")
        else:
            for i in range(self.ultima_posicao+1):
                print(f"{i} - {self.valores[i]}")

    def inserir(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida')
            return

        posicao = 0
        for i in range(self.ultima_posicao+1):
            posicao = i
            if self.valores[i]>valor:
                break
            if i == self.ultima_posicao:
                posicao = i+1

        x = self.ultima_posicao
        while x>=posicao:
            self.valores[x+1] = self.valores[x]
            x-=1

        self.valores[posicao] = valor
        self.ultima_posicao+=1

vetor = Vetor_Ordenado(10)

vetor.inserir(1)
vetor.inserir(5)
vetor.inserir(3)
vetor.imprimir()