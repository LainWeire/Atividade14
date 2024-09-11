# Crie um programa que receba três notas de um aluno e calcule a média. Informe se o aluno foi aprovado, reprovado ou se está de recuperação. Use as seguintes regras:
# Média ≥ 7: Aprovado
# 5 ≤ Média < 7: Recuperação
# Média < 5: Reprovado

n1 = float(input("Digite a 1° nota: "))
n2 = float(input("Digite a 2° nota: "))
n3 = float(input("Digite a 3° nota: "))

m = ((n1 + n2 + n3) / 3)

if (m >= 7):
    print ("Aprovado")

elif (5 <= m) and (m < 7):
    print ("Recuperação")

elif (m < 5):
    print ("Reprovado")