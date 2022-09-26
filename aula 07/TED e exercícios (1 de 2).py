#As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas
#pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.

preço1 = 1.30
preço2 = 1.00


quantidade = int(input('Quntas maçãs você quer? '))
n1 = preço1*quantidade
n2 = preço2*quantidade
if quantidade < 12:
    print(f'Fica por R$ {n1}')
else:
    print(f'O valor será de R$ {n2}')
