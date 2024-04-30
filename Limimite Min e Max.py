print("Gabriel Gomes da Silva")
print("Questão 02")

LMin = int(input("Digite o LMin: "))
LMax = int(input("Digite o LMax: "))
if LMin <= 0:
    print("LMin deve ser maior que zero")
    LMin = int(input("Digite o LMin: "))
elif LMin > LMax:
    print("LMax deve ser maior que o LMin")
    LMax = int(input("Digite o LMax: "))
X = int(input("Digite o X: "))
if X == 0:
    print("X deve ser diferente de 0")
    X = int(input("Digite o X: "))
N = 1
L = []
V = 0
while N != 0:
    N = int(input("Digite um valor: "))
    if N in L:
        print("Valor repetido")
    elif N > LMin and N < LMax and N % X == 0 and N not in L:
        L.append(N)
        V = V + N
M = V / len(L)
for x in L:
    print(x)
print("Há {} elemento(s) na lista".format(len(L)))
print("A soma de todos os valores é: {}".format(V))
print("A média dos elementos da lista é: {}".format(M))

