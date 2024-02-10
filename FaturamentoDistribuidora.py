import json

def calcular_faturamento(faturamento_diario):
    
    menor_faturamento = min(faturamento_diario, key=lambda x: x['valor'])['valor']
    
    maior_faturamento = max(faturamento_diario, key=lambda x: x['valor'])['valor']
    
    faturamento_sem_zero = [dia['valor'] for dia in faturamento_diario if dia['valor'] > 0]
    media_mensal = sum(faturamento_sem_zero) / len(faturamento_sem_zero)
    
    dias_acima_da_media = len([dia for dia in faturamento_diario if dia['valor'] > media_mensal])
    
    return menor_faturamento, maior_faturamento, dias_acima_da_media

if __name__ == "__main__":
    with open('/home/mariana/Documentos/Target Sistemas/Questão 3/dados.json') as file:
        faturamento_diario = json.load(file)
    
    menor_faturamento, maior_faturamento, dias_acima_da_media = calcular_faturamento(faturamento_diario)
    
    print(f"Menor valor de faturamento: R$ {menor_faturamento}")
    print(f"Maior valor de faturamento: R$ {maior_faturamento}")
    print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")

