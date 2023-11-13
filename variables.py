# Variavais

# Exemplo 1: Atribuindo um valor a uma variável
nome = "João"
idade = 25
altura = 1.75
sobre_nome = "Vilela"

# Exemplo 2: Python permite múltiplas atribuições em uma única linha
a, b, c = 1, 2, 3

# Exemplo 3: Variáveis podem ser utilizadas em expressões
soma = a + b + c

# Exemplo de constante (convenção)
TAXA_DE_JUROS = 0.05
DIAS_DA_SEMANA = 7

# Tentativa de modificar a constante (gerará um aviso, mas não impedirá a modificação)
TAXA_DE_JUROS = 0.1  # Embora isso seja possível, é uma prática ruim

# Outra abordagem (usando uma tupla para imitar a imutabilidade)
constantes = (0.05, 7)
TAXA_DE_JUROS = constantes[0]  # Isso é mais seguro, mas ainda não é completamente imutável

# Concatenação
print(f"Bem vindo {nome} {sobre_nome}! Sua idade é {idade}?")
print("Bem vindo " + str(nome) + str(sobre_nome) + "! Sua idade é " + str(idade) + "?")
