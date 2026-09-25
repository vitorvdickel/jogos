'''
Você decidiu organizar melhor suas finanças e começar a guardar dinheiro todos os meses.
Crie um Algoritmo que:
Possa ser adicionado o valor que será depositado mensalmente;
A quantidade de meses em que esse valor será guardado;
Utilize um laço de repetição para calcular e exibir o saldo acumulado mês a mês; 
'''

print ("Cofrinho!!!")

dinheiro_mensal = float(input("Escolha o valor que deseja depositar mensalmente: "))
meses_guardados = int(input("Quantos meses esse valor ficará guardado? "))

print ("Valor de deposito mensal (R$): ", dinheiro_mensal)
print ("Quantidade de meses: ", meses_guardados)

saldo = 0

for mes in range (1, meses_guardados + 1):
    saldo += dinheiro_mensal
    print ("Mes", mes,": saldo acumulado = R$ ",saldo)