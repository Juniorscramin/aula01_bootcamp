# 1) Solicita ao usuário que digite seu nome
nome = input("Digite seu nome: ")

# 2) Solicita ao usuario que digite o valor do seu salário
# Converte a entrada para número de ponto flutuante
salario = float(input("Digite o valor do seu salário: "))

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para número de ponto flutuante
bonus = float(input("Digite o valor do bônus recebido: "))
CONSTANTE_BONUS = 1000

# 4) Calcule o valor do bônus final
valor_do_bonus = CONSTANTE_BONUS + salario * bonus

# 5) Imprima a mensagem personalizada incluindo o nome do usuário e o valor do bônus
print(f"O usuário {nome} possui o bonus de {valor_do_bonus}")