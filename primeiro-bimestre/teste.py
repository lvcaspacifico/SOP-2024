# Testando se vai atualizar no Github

class Processo():
    def __init__(self, tamanho, posicaoAtual):
        self.tamanho = tamanho
        self.posicaoAtual = posicaoAtual


class AlgoritmoSTRF():
    def __init__(self):
        contadorCPU = []
        rodar = True
        contador = 0
        while (rodar):
            
            print("///////// Bem-vindo ao Algoritmo STRF /////////")
            print("///////// 'shortest time remaining first /////////")
            print("==================================================")

            print("Adicione um Processo na fila:")

            processoAtual = Processo(int(input("Digite o tamanho do processo(0 a 10):")),contador)
            contadorCPU.append(processoAtual)


            print(contadorCPU)
            op = int(input("Digite 4 para sair"))
            if op == 4:
                rodar = False
            contador += 1


AlgoritmoSTRF()