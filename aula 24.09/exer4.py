'''
Jogo dos dados
Crie um algoritmo que simule uma disputa de dados entre você e o computador
Regras:
Em cada rodada:
os valores sorteados devem ser exibidos;
vence a rodada quem tirar o maior número;
caso os dois tirem o mesmo valor, o resultado deve ser empate.
Ao final de cada rodada perguntar para o “jogador” se deseja jogar novamente
'''
import random

print ("Jogo de dados")

opcoes = [1, 2, 3, 4, 5, 6]

while True:
    jogador = str(input("Escreva jogar para lançar seu dado\n"))
    if (jogador not in "jogar"):
        print ("Não entendi o comando")
    else:
        dado_jogador = random.choice(opcoes)
        dado_pc = random.choice(opcoes)

    if (dado_jogador == dado_pc):
        print ("O jogo empatou!!!")
        print ("Valor do dado do jogador: ", dado_jogador)
        print ("Valor do dado do computador: ", dado_pc)
        repetir = input("Deseja jogar novamente? (s/n)").strip().lower()
        if repetir != "s":
            break
        else:
            continue
    elif (dado_jogador > dado_pc):
        print ("O jogador ganhou!!!")
        print ("Valor do dado do jogador: ", dado_jogador)
        print ("Valor do dado do computador: ", dado_pc)
        repetir = input("Deseja jogar novamente? (s/n)").strip().lower()
        if repetir != "s":
            break
        else:
            continue
    elif (dado_jogador < dado_pc):
        print ("O computador ganhou!!!")
        print ("Valor do dado do jogador: ", dado_jogador)
        print ("Valor do dado do computador: ", dado_pc)
        repetir = input("Deseja jogar novamente? (s/n)").strip().lower()
        if repetir != "s":
            break
        else:
            continue
    else:
        print ("Error")