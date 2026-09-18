#Desenvolva um algoritmo que simule o funcionamento básico de um caixa eletrônico.
#Considere que o usuário inicia sua conta com um saldo de:
#R$ 2.000,00
#Opção 1 — Consultar saldo
#Ao escolher essa opção, o programa deverá apresentar o valor disponível
#atualmente na conta.
#Opção 2 — Realizar depósito
#O programa deverá solicitar o valor que será depositado.
#O depósito somente poderá ser realizado caso o valor informado seja maior
#que zero.
#Opção 3 — Realizar saque
#O programa deverá solicitar o valor que será retirado da conta.
#O saque deverá ser autorizado somente quando:
#o valor for maior que zero;
#o cliente possuir saldo suficiente.
#Opção 4 — Encerrar
#Ao selecionar essa opção, apresente uma mensagem de
#encerramento e finalize o programa.

saldo_conta = 2000

opcao = 0

while (opcao != 4):
    print ("1 - Consultar saldo")
    print ("2 - Realizar deposito")
    print ("3 - Realizar saque")
    print ("4 - Encerrar")

    opcao = int(input("Inserir a opção equivalente: "))

    if (opcao == 1):

        print ("Seu saldo em conta é de R$", saldo_conta)
        continue

    elif (opcao == 2):

        valor_deposito = float(input("Inserir o valor a ser depositado: "))
        saldo_conta = saldo_conta + valor_deposito
        print ("Valor depositado")
        continue

    elif (opcao == 3):

        valor_saque = float(input("Inserir o valor a ser sacado: "))
        saldo_conta = saldo_conta - valor_saque
        print ("Valor sacado")
        continue

    elif (opcao == 4):
        break

    else:
        print ("opção indisponivel")