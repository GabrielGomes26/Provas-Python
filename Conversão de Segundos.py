print("Gabriel Gomes da Silva")
print("Questão 1")

N = int(input("Digite a quantidade de segundos: "))
h = N // 3600
R = N % 3600
m = R // 60
R = R % 60

print("{} horas, {} minutos, {} segundos".format(h, m, R))
        
