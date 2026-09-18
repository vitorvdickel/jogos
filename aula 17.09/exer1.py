#Desenvolva um algoritmo que simule uma calculadora simples.
#O programa deverá apresentar um menu com diferentes operações matemáticas e
#permanecer em
#execução até que o usuário escolha a opção de sair.

opcao = 0

print ("CALCULADORA")
print ("1 - Somar")
print ("2 - Subtrair")
print ("3 - Multiblicar")
print ("4 - Dividir")
print ("5 - Sair")

while opcao != 5:

    opcao = int(input("Escolha uma opção: "))
    
    numero1 = float(input("Digite o primeito numero: "))
    numero2 = float(input("Digite o segundo numero: "))

    if (opcao == 1):
        resultado = numero1 + numero2
        print ("Resultado: ", resultado)
    elif (opcao == 2):
        resultado = numero1 - numero2
        print ("Resultado: ", resultado)
    elif (opcao == 3):
        resultado = numero1 * numero2
        print ("Resultado: ", resultado)
    elif (opcao == 4):
        resultado = numero1 / numero2
        print ("Resultado: ", resultado)
    elif (opcao == 5):
        print ("Fechando calculadora...")
    else:
        print ("Opção indisponivel, tente novamente")