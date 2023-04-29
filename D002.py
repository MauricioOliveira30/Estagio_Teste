# Função que calcula a sequência de Fibonacci até um determinado limite
def fibonacci(limit):
    seq = [0, 1]
    while seq[-1] < limit:
        seq.append(seq[-1] + seq[-2])
    return seq

# Pede um número ao usuário
n= int(input("Digite um número inteiro: "))

# Calcula a sequência de Fibonacci até o número digitado
seq_fibonacci = fibonacci(n)

# Verifica se o número pertence à sequência
if n in seq_fibonacci:
    print(f"{n} pertence à sequência de Fibonacci.")
else:
    print(f"{n} não pertence à sequência de Fibonacci.")
