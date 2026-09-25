'''
Crie um algoritmo que o colaborador digite a velocidade escolhida (300, 600 ou 1000 Mbps)
Se o cliente quer:
streaming (S/N) e se e cliente é antigo ( > 6 meses )

Regras:
- Valor base: 300mb: 79.90 – 600mb: 109.90, 1gb -> 129.90
- Netflix adiciona 19.90
- Cliente antigo recebe 10% de desconto no subtotal
- Exiba plano, adicional, desconto e o Total
'''

while True:
    #Velocidade da internet no plano
    velocidade = int(input("Digite a velocidade da internet (300, 600 ou 1000 Mbps)"))
    if (velocidade == 300):
        valor_internet = 79.90
    elif (velocidade == 600):
        valor_internet = 109.90
    elif (velocidade == 1000):
        valor_internet = 129.9
    else:
        print ("Não trabalhamos com essa velocidade de internet, tente novamente")

    #Cliente deseja canal de streaming?
    streaming = input("O cliente deseja canal de streaming? (s/n) ")
    if (streaming == "s"):
        valor_total = valor_internet + 19.90
    else:
        valor_total = valor_internet + 0

    #Tempo de contrato do cliente
    tempo_contrato = int(input("Quanto tempo o cliente já tem de contrato conosco? "))
    if (tempo_contrato >= 6):
        valor_total * 0.9
        print ("Valor total do plano é: ", valor_total)
        print ("Valor da internet: ", valor_internet)
        print ("Valor do streaming é R$ 19.90")
        print ("O desconto por fidelidade é de 10%")
    else:
        print ("Valor total do plano é: ", valor_total)
        print ("Valor da internet: ", valor_internet)
        print ("Você optou por não assinar o streaming")
        print ("Você não ganhou o desconto de fidelidade (a partir dos 6 meses)")
