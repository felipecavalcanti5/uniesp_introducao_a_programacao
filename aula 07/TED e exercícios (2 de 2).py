# Ler o ano atual e o ano de nascimento de uma pessoa. 
# Escrever uma mensagem que diga se ela poderá ou não votar este ano 
# (não é necessário considerar o mês em que a pessoa nasceu)

ano_atual = int(input('Em que ano nós estamos? '))
nascimento = int(input('Em que ano você nasceu? '))
if ano_atual - nascimento < 16:
    print("Você não poderá votar este ano")
else:
    print("Este ano, você poderá votar")
