'''
Faça um programa em Python que obtenha como entrada a quantidade de km
percorridos por um carro e a quantidade de dias pelos quais o carro foi alugado.
Calcule e mostre o valor total gasto com diárias, o valor total gasto com km 
rodado e o valor total a pagar (total de diárias + total gasto pela 
quilometragem rodada), sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 
por km percorrido.
'''

km_percorrido = float(input("Digite a quilometragem percorrida pelo veículo: "))
dias_alugado = int(input("Quantos dias o veiculo ficou locado? "))

total_percorrido = km_percorrido * 0.15
total_aluguel = dias_alugado * 60
total = total_aluguel + total_percorrido

print ("--------------------------------------")
print ("Quantos dias o carro ficou alugado? ", dias_alugado)
print ("Quantos Km foram rodados com o veículo? ", km_percorrido)
print ("--------------------------------------")
print ("Valor gasto com a diária do carro: R$", total_aluguel)
print ("Valor gasto com Km rodado: R$", total_percorrido)
print ("Valor total a pagar: R$", total)