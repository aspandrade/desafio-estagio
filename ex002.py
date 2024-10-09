def fibonacci(n):
    # Gerando a sequência de Fibonacci até um limite n
    a, b = 0, 1
    sequencia = [a, b]
    
    while b <= n:
        a, b = b, a + b
        sequencia.append(b)
    
    return sequencia

def pertence_fibonacci(num):
    # Verificando se o número pertence à sequência de Fibonacci
    sequencia = fibonacci(num)
    
    if num in sequencia:
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} não pertence à sequência de Fibonacci."

# Exemplo de uso:
numero = int(input("Informe um número: "))
resultado = pertence_fibonacci(numero)
print(resultado)