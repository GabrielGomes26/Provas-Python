print("Gabriel Gomes da Silva")
print("Questão 03")

NV = int(input("Digite o número de vendas realizadas: "))
if NV < 0:
    print("O número de vendas deve ser maior que zero")
    NV = int(input("Digite o número de vendas realizadas: "))
cont = 0
VA = []
AT = []
VAT = 0
VVA = 0
while cont < NV:
    Cod, QV = input("Digite o Código e a quantidade de vendas, separadas por espaço: ").split(" ")
    Cod = int(Cod)
    QV = int(QV)
    if Cod != 16 and Cod != 23 and Cod != 27 and Cod != 34:
        print("Código Inválido")
    if Cod == 16 and QV < 50:
        V = 14.35 * QV
        VA.append(V)
        VVA = VVA + V
        cont += 1
    elif Cod == 16 and QV >= 50:
        V = 12.93 * QV
        AT.append(V)
        VAT = VAT + V
        cont += 1
    elif Cod == 23 and QV < 100:
        V = 35.12 * QV
        VA.append(V)
        VVA = VVA + V
        cont += 1
    elif Cod == 23 and QV >= 100:
        V = 29.85 * QV
        AT.append(V)
        VAT = VAT + V
        cont += 1
    elif Cod == 27 and QV < 70:
        V = 19.35 * QV
        VA.append(V)
        VVA = VVA + V
        cont += 1
    elif Cod == 27 and QV >= 70:
        V = 16.76 * QV
        AT.append(V)
        VAT = VAT + V
        cont += 1
    elif Cod == 34 and QV < 40:
        V = 63.40 * QV
        VA.append(V)
        VVA = VVA + V
        cont += 1
    elif Cod == 34 and QV >= 40:
        V = 58,25 * QV
        AT.append(V)
        VAT = VAT + V
        cont += 1

print("Total de Vendas do Grupo Varejo: R$ {:.2f}".format(VVA))
print("Total de Vendas do Grupo Atacado: R$ {:.2f}".format(VAT))
VTOTAL = VAT + VVA
print("Vendas Totais: R$ {:.2f}".format(VTOTAL))
        
