# PROBLEMA 1:

nota_final = float(input("Digite a nota final: "))
faltas = int(input("Digite o número de faltas: "))

aprovado = (nota_final >= 70) and (faltas <= 15)
reprovado = (nota_final < 50) or (faltas > 15)
exame_final = not aprovado and not reprovado

print("Aprovado:", aprovado)
print("Reprovado:", reprovado)
print("Exame Final:", exame_final)

# PROBLEMA 2:

dureza = float(input("Dureza: "))
teor = float(input("Teor de carvão: "))
resistencia = float(input("Resistência da tração: "))

i = (dureza > 50)
ii = (teor < 0.7)
iii = (resistencia > 5600)

resultado_10 = (i and ii and iii)
resultado_9 = (i and ii and not iii)
resultado_8 = (not i and ii and iii)
resultado_7 = (i and not ii and iii)
resultado_6 = (i and not ii and not iii) or (not i and ii and not iii) or (not i and not ii and iii)
resultado_5 = (not i and not ii and not iii)

print("Pontuação 10: ", resultado_10)
print("Pontuação 9: ", resultado_9)
print("Pontuação 8: ", resultado_8)
print("Pontuação 7: ", resultado_7)
print("Pontuação 6: ", resultado_6)
print("Pontuação 5: ", resultado_5)
