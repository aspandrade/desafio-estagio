#Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
#Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
#Imprimir(SOMA);
#Ao final do processamento, qual será o valor da variável SOMA?

# Informações passadas pelo enunciado
indice = 13
soma = 0
k = 0

# Laço de repetição while para executar o cálculo necessário
while k < indice:
    k += 1
    soma += k
    
# Ao executarmos o print(soma) teremos como retorno o valor 91.

print(soma)
