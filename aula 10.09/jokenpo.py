#1º atividade: Adicionar 3 chances para jogar

#2º atividade: Mudar a estrutura do jogo adicionando mais uma opção

import random

print("Jogo Jokenpo!")

opcoes = ["Pedra", "Papel", "Tesoura", "Bazuca"]

chances = 0

while chances < 3:
    jogador = str(input("Escolha entre Pedra, Papel, Tesoura ou Bazuca: ").capitalize())
    chances += 1

    if jogador not in opcoes:
        print("Escolha errada tente novamente.")
        continue

    pc = random.choice(opcoes)

    print("O computador escolheu:", pc)

    if jogador == pc:
        print("Empate!")
    elif jogador == "Pedra":
        if pc == "Tesoura":
            print("Você venceu!")
        else:
            print("O seu adversario venceu!")
    elif jogador == "Papel":
        if pc == "Pedra":
            print("Você venceu!")
        else:
            print("O seu adversario venceu!")
    elif jogador == "Tesoura":
        if pc == "Papel":
            print("Você venceu!")
        else:
            print("O seu adversario venceu!")
    elif jogador == "Bazuca":
        if pc == "Papel" or "Pedra" or "Tesoura":
            print("Você explodiu o pc")
        else:
            print("O advesario venceu")

    if chances < 3:
        continue
    else:
        restart = input("Gostaria de jogar novamente? (Sim/Nao) ").upper()
    if restart != "SIM":
        break