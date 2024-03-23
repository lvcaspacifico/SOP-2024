# Sempre que uma nova tarefa entra,ela é comparada as demais
## a menor inicia

# Sempre que a tarefa rodando acaba, as demais são comparadas
## a menor inicia


class Tarefa():
    def __init__(self, tamanhoCiclo, tamanhoCicloAtualizado, cicloDeEntrada, cicloDeFinal, ciclosEsperando):
        self.tamanhoCiclo = tamanhoCiclo
        self.tamanhoCicloAtualizado = tamanhoCicloAtualizado
        self.cicloDeEntrada = cicloDeEntrada
        self.cicloDeFinal = cicloDeFinal
        self.ciclosEsperando = ciclosEsperando

    def descontarUmCiclo(self):
        self.tamanhoCiclo -= 1



rodar = True
gerir = 0
contador_ciclo_cpu = 0
tarefasNaFila = []
menorTarefa = []
indiceTarefaADescontar = 0
tarefaAtual = []
while(rodar):
        # Aqui começa as validações

        ## indicando qual ciclo atual
        print(f"Ciclo atual: {contador_ciclo_cpu}")


        ## Adicionando ou não tarefa
        print("Desejar adicionar tarefa?")
        print("1 = Adicionar")
        print("0 = Continuar")

        gerir = int(input())

        if gerir == 1:
            input_tamanhoCiclo = int(input("Digite o tamanho do ciclo:\n"))
            tarefaNova = Tarefa(input_tamanhoCiclo,input_tamanhoCiclo,contador_ciclo_cpu,0,0) # valores 0 vão ser atualizados ao final da tarefa
            tarefasNaFila.append(tarefaNova)
            #print(tarefasNaFila)


            if contador_ciclo_cpu == 0:
                menorTarefa.append(tarefaNova)
                # print("Menor tarefa atualizada primeira vez")
            else:
                 # Validando tarefa com menor quantidade de ciclos atual
                print("=================Validando a nova menorTarefa=================")
                for tarefa in range(len(tarefasNaFila)):
                    if tarefasNaFila[tarefa].tamanhoCicloAtualizado < menorTarefa[0].tamanhoCicloAtualizado:
                        
                        indiceTarefaADescontar = tarefa
                        menorTarefa.pop() # remove atual menor
                        menorTarefa.append(tarefasNaFila[tarefa]) # adiciona nova menor
                        print(f"Menor tarefa atualizada! Agora ela é a {menorTarefa[0].tamanhoCiclo}")
                    else:
                        print("Tarefa menor persiste a mesma.")
            
            
                        
            ## Mostrar todas
            print("=================Relatório Tarefas=================")
            for tarefa in range(len(tarefasNaFila)):
                print(f"Tamanho da Tarefa {tarefa+1} é: {tarefasNaFila[tarefa].tamanhoCiclo} | Espera: {tarefasNaFila[tarefa].ciclosEsperando}")

    

            # Adicionando um ciclo ao tempo de espera de cada tarefa + aumentando espera
            print("=================Relatório de Espera das Tarefas=================")
            for tarefa in range(len(tarefasNaFila)):
                if tarefa != indiceTarefaADescontar:
                    print(f"Tarefa {tarefa+1} estava esperando à: {tarefasNaFila[tarefa].ciclosEsperando}")
                    tarefasNaFila[tarefa].ciclosEsperando += 1
                    print(f"Tarefa {tarefa+1} agora espera à: {tarefasNaFila[tarefa].ciclosEsperando} | Seu tamanho era: {tarefasNaFila[tarefa].tamanhoCiclo} e agora é: {tarefasNaFila[tarefa].tamanhoCicloAtualizado}")
                else:
                    print("Apenas uma tarefa em execução.")
            
            # Descontando da menor tarefa
            print("=================Relatório Menor Tarefa Atual=================")
            print(f"Tamanho inicial menorTarefa: {menorTarefa[0].tamanhoCiclo}")
            menorTarefa[0].tamanhoCicloAtualizado -= 1 ## Descontando um ciclo (atual) da menor tarefa
            print(f"Tamanho atual restando na menorTarefa: {menorTarefa[0].tamanhoCicloAtualizado}")

            contador_ciclo_cpu += 1
            

        if gerir == 0:
             ## Mostrar todas
            print("=================Relatório Tarefas=================")
            for tarefa in range(len(tarefasNaFila)):
                print(f"Tamanho da Tarefa {tarefa+1} é: {tarefasNaFila[tarefa].tamanhoCiclo} | Espera: {tarefasNaFila[tarefa].ciclosEsperando}")
            # Adicionando um ciclo ao tempo de espera de cada tarefa + aumentando espera
            print("=================Relatório de Espera das Tarefas=================")
            for tarefa in range(len(tarefasNaFila)):
                if tarefa != indiceTarefaADescontar:
                    print(f"Tarefa {tarefa+1} estava esperando à: {tarefasNaFila[tarefa].ciclosEsperando}")
                    tarefasNaFila[tarefa].ciclosEsperando += 1
                    print(f"Tarefa {tarefa+1} agora espera à: {tarefasNaFila[tarefa].ciclosEsperando} | Seu tamanho era: {tarefasNaFila[tarefa].tamanhoCiclo} e agora é: {tarefasNaFila[tarefa].tamanhoCicloAtualizado}")
                else:
                    print("Apenas uma tarefa em execução.")
            
            # Descontando da menor tarefa
            print("=================Relatório Menor Tarefa Atual=================")
            print(f"Tamanho inicial menorTarefa: {menorTarefa[0].tamanhoCiclo}")
            menorTarefa[0].tamanhoCicloAtualizado -= 1 ## Descontando um ciclo (atual) da menor tarefa
            print(f"Tamanho atual restando na menorTarefa: {menorTarefa[0].tamanhoCicloAtualizado}")


            ### PRECISA ADICIONAR O QUE ACONTECE QUANDO A menorTarefa FICA ZERADA EM tamanhoCicloAtualizado
                ## o novo menorTarefa deve entrar na sequência

            contador_ciclo_cpu += 1
            
        if gerir == 4:
            break
