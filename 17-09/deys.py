
dureza = float(input("Digite a dureza: "))
teor = float(input("Digite o teor de teor: "))
resistencia_tracao = float(input("Digite a resistência à tração: "))

# Expressões Booleanas: As expressões dentro dos parênteses, como dureza > 50, 
#resultam em um valor booleano: True (verdadeiro) ou False (falso).
#true vale 1 e false vale 0

pontuacao = 10 * (dureza > 50) * (teor < 0.7) * (resistencia_tracao > 5600) + \
            9 * (dureza > 50) * (teor < 0.7) * (resistencia_tracao <= 5600) + \
            8 * (dureza <= 50) * (teor < 0.7) * (resistencia_tracao > 5600) + \
            7 * (dureza > 50) * (teor >= 0.7) * (resistencia_tracao > 5600) + \
            6 * ((dureza > 50) * (teor >= 0.7) * (resistencia_tracao <= 5600) + \
                (dureza <= 50) * (teor < 0.7) * (resistencia_tracao <= 5600) + \
                (dureza <= 50) * (teor >= 0.7) * (resistencia_tracao > 5600)) + \
            5 * (dureza <= 50) * (teor >= 0.7) * (resistencia_tracao <= 5600)


print("A pontuação do aço é:", +\
      pontuacao)