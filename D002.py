# Função que calcula a sequência de Fibonacci até um determinado limite
def fibonacci():
   
# Pede um número ao usuário
n= int(input("Digite um número inteiro: "))

# Calcula a sequência de Fibonacci até o número digitado

t1=0
t2=1
for i in range(0,num):
    fibo=t1+t2
    t1=t2
    t2=fibo
    print(f"A sequência fibonacci é {fibo}")

