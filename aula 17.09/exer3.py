#Desenvolva um algoritmo que simule um sistema simples da situação acadêmica de um aluno.
#Opção 1 — Informar nota
#Ao selecionar essa opção, o programa deverá solicitar uma nota ao usuário.
#A nota deverá obrigatoriamente estar entre:
#0 e 10
#Opção 2 — Consultar situação do aluno
#Ao selecionar essa opção, o sistema deverá apresentar a nota registrada e informar a 
#situação do aluno.
#Considere as seguintes regras:
#Nota maior ou igual a 7 = Aprovado
#Nota maior ou igual a 3 e menor que 7 = Recuperação
#Nota menor que 5 = Reprovado

opcao = 0
nota = -1

while (opcao != 3):
    print ("SISTEMA DE NOTAS")
    print ("1 - Inserir nota")
    print ("2 - Consultar situação do aluno")
    print ("3 - Sair")

    opcao = int(input("Escolha uma opcao: "))

    if (opcao == 1):

        nota = float(input("Insira sua nota: "))
        continue

    elif (opcao == 2):

        if (nota == -1):
            print ("Inserir sua nota primeiro...")
            continue

        elif (nota >= 7):
            print ("Aluno aprovado por media ")

        elif (7 > nota >= 3):
            print ("Aluno em recuperação ")

        else:
            print ("Aluno reprovado ")

    else:
        print ("Encerrando programa...")