#Desenvolva um algoritmo que simule uma votação entre 3 candidatos.
#Cada vez que o usuário selecionar uma das opções correspondentes aos candidatos, 
# deverá ser
#registrado um voto para aquele candidato.
#O processo deverá continuar até que seja escolhida a opção 4.
#Quando finalizar o programa devera mostrar a quantidade de votos de todos os 
#candidatos

opcao = 0
pikachu = 0
jon_snow = 0
num_quidito = 0
barcelos = 0

while (opcao != 5):

    print ("=========VOTAÇÃO==========")
    print ("1 - Pikachu")
    print ("2 - Jon Snow")
    print ("3 - Num quidito")
    print ("4 - Barcelos")
    print ("5 - Encerrar votação")

    opcao = int(input("Digite o número correspondente ao seu voto: "))

    if (opcao == 1):

        pikachu += 1
        print ("Voto registrado para pikachu")

    elif (opcao == 2):

        jon_snow += 1
        print ("Voto registrado para Jon Snow")

    elif (opcao == 3):

        num_quidito += 1
        print ("Voto registrado para Num quidito")

    elif (opcao == 4):

        barcelos += 1
        print ("Voto registrado para Barcelos (gremista)")

    elif (opcao == 5):

        print ("RESULTADO DAS ELEIÇÕES!!!")

        if (pikachu > jon_snow or num_quidito or barcelos):
            print (("Pikachu ganhou a eleicao com "), pikachu, (" votos!"))

            if (jon_snow > num_quidito):
                print ("1º Pikachu, 2º Jon Snow, 3º Num quidito")
            else:
                 print ("1º Pikachu, 2º Num quidito, 3º Jon Snow")               

        elif (jon_snow > pikachu or num_quidito or barcelos):
            print (("Jon Snow ganhou a eleicao com "), jon_snow (" votos!"))

            if (pikachu > num_quidito):
                print ("1º Jon Snow, 2º Pikachu, 3º Num quidito")
            else:
                 print ("1º Jon Snow, 2º Num quidito, 3º Pikachu")                

        elif (num_quidito > pikachu or jon_snow or barcelos):
            print (("Num quidito ganhou a eleicao com "), num_quidito (" votos!"))

            if (pikachu > jon_snow):
                print ("1º Num quidito, 2º Pikachu, 3º Jon Snow")
            else:
                 print ("1º Num quidito, 2º Jon Snow, 3º Pikachu") 

        elif (barcelos > pikachu or jon_snow or num_quidito):
            print (("Alessandro barcelos ganhou a eleicao com "), barcelos (" votos!"))

        else:
            ("Meu código não funciona")

    else:
        print ("Opcao invalida, tente novamente...")
        continue

    total_votos = pikachu + jon_snow + num_quidito

    print ("O total de votos foi de: ", total_votos)


#adicione o numero total de votos
# Adicione a ordem do resultado 1 - 2 -3 
# adicione + 1 candidato.