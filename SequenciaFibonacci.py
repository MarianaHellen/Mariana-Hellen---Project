def fibonacci_sequencia(n):
    fibonacci = [0, 1]
    while fibonacci[-1] < n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci

def verifica_pertence(numero, sequencia):
    if numero in sequencia:
        return f"O número {numero} pertence à sequência de Fibonacci."
    else:
        return f"O número {numero} não pertence à sequência de Fibonacci."

if __name__ == "__main__":
    numero_informado = int(input("Informe um número para verificação: "))
    sequencia_fibonacci = fibonacci_sequencia(numero_informado)
    mensagem = verifica_pertence(numero_informado, sequencia_fibonacci)
    print(mensagem)
