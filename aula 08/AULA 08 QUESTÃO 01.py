# [FORBELLONE, 2022] Construa um algoritmo para calcular as raízes de uma equação do 2 grau (Ax² + Bx + C),
# sendo que os valores A, B, C são fornecidos pelo usuário. (considere que a equação possui duas raizes reais).

a = float(input("Qual o valor de A ?    "))
b = float(input("Qual o valor de B ?    "))
c = float(input("Qual o valor de C ?    "))

d = b**2 - 4 * (a * c )

x1 = (-b + (d**0.5) ) / (2*a)
print (x1)

x2 = (-b - (d**0.5) ) / (2*a)
print (x2)