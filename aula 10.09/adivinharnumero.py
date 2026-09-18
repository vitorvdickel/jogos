import random

print ("Adivinhe o numero que o PC pensou")

numero_pc = random.randint(1, 10)

chances = 0;

while chances < 3:

    chances += 1
    choice = int(input("Escolha um numero entre 1 a 10 "))

    if choice not in (1,2,3,4,5,6,7,8,9,10):
        print ("Resposta fora das alternativas, tente novamente")
        continue

    if (choice == numero_pc):
        print ("Parabéns, você acertou!!!")
        break
    elif (choice > numero_pc):
        print ("O seu número é maior que o número do PC")
    else:
        print ("O seu número é menor que o número do PC")

    if (chances < 3):
        continue
    else:
        restart = input("Gostaria de jogar novamente? (Sim/Nao) ").upper()
    if restart != "SIM":
        break
    else:
        continue