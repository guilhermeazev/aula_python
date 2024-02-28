import pandas as pd
#1
def conta_vogais(string): 
    string = string.lower()
    result = 0 
    vogais = 'aeiou' 
    for i in vogais: 
        result += string.count(i) 
    return result 
 
print(conta_vogais('olaaa')) 
#2
def substituir_letra(string, letra_alvo, letra_substituta):
    return string.replace(letra_alvo, letra_substituta)

# Exemplo de uso
string_original = "banana"
letra_alvo = "a"
letra_substituta = "o"
nova_string = substituir_letra(string_original, letra_alvo, letra_substituta)
print(nova_string) 

#3
def contar_palavras(string):
    string = string.strip()
    if not string:
        return 0
    palavras = string.split()
    return len(palavras)
texto = "exemplo"
num_palavras = contar_palavras(texto)
print("Número de palavras:", num_palavras)

#4
def contar_ocorrencias(frase, palavra):
    palavras = frase.split()
    contador = 0
    for palavra_frase in palavras:
        if palavra_frase.lower() == palavra.lower():
            contador += 1
    return contador
frase = "testando exemplo, exemplo 2 vezes"
palavra = "exemplo"
num_ocorrencias = contar_ocorrencias(frase, palavra)
print(f"A palavra '{palavra}' ocorre {num_ocorrencias} vezes na frase.")

#5
def k_maiores(lista, k):
    lista_ordenada = sorted(lista, reverse=True)
    k_maiores_elementos = lista_ordenada[:k]
    resultado = [x for x in lista if x in k_maiores_elementos]
    return resultado
lista = [4, 8, 2, 10, 5, 3, 7]
k = 3
maiores_elementos = k_maiores(lista, k)
print(f"Os {k} maiores elementos na lista são: {maiores_elementos}")

#6
def soma_matrizes(matriz1, matriz2):
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        return None 

    resultado = [[0 for _ in range(len(matriz1[0]))] for _ in range(len(matriz1))]
    for i in range(len(matriz1)):
        for j in range(len(matriz1[0])):
            resultado[i][j] = matriz1[i][j] + matriz2[i][j]
    
    return resultado

matriz1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matriz2 = [[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]]

resultado = soma_matrizes(matriz1, matriz2)

if resultado is not None:
    print("Matriz Resultante:")
    for linha in resultado:
        print(linha)
else:
    print("ERRO")

#7
def encontrar_intersecao(lista1, lista2):
    intersecao = []
    for elemento in lista1:
        if elemento in lista2 and elemento not in intersecao:
            intersecao.append(elemento)
    return intersecao

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

resultado = encontrar_intersecao(lista1, lista2)
print("Interseção das listas:", resultado)

#8
import random
def embaralhar_lista(lista):
    lista_embaralhada = lista[:]
    random.shuffle(lista_embaralhada)
    return lista_embaralhada

minha_lista = [1, 2, 3, 4, 5]
minha_lista_embaralhada = embaralhar_lista(minha_lista)
print("Lista original:", minha_lista)
print("Lista embaralhada:", minha_lista_embaralhada)

#9
def encontrar_par_soma(lista, alvo):
    conjunto = set()
    for num in lista:
        complemento = alvo - num
        if complemento in conjunto:
            return (num, complemento)
        conjunto.add(num)
    return None

lista = [1, 4, 3, 7, 5, 9, 2]
alvo = 10
par = encontrar_par_soma(lista, alvo)
if par:
    print(f"Par encontrado: {par[0]} + {par[1]} = {alvo}")
else:
    print("Nenhum par encontrado com a soma igual ao alvo.")

#10
def calcular_frequencia(texto):
    texto = texto.lower()
    for char in '.,!?;:':
        texto = texto.replace(char, '')
    palavras = texto.split()
    frequencias = {}
    for palavra in palavras:
        if palavra in frequencias:
            frequencias[palavra] += 1
        else:
            frequencias[palavra] = 1
    return frequencias
texto = "Este é um exemplo de texto. Neste exemplo, estamos contando a frequência de cada palavra neste texto."
frequencias = calcular_frequencia(texto)
print("Frequência de cada palavra no texto:")
for palavra, frequencia in frequencias.items():
    print(f"{palavra}: {frequencia}")
 

#11
with open('arquivo.txt', 'r') as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        print(linha)
#12
df = pd.read_csv('C:\\Users\\1054444\\Documents\\aulas python\\teste1.csv')
print(df)

#13
df2 = pd.read_json(f'C:\Users\1054444\Documents\aulas python\teste2.json')
print(df2)

#14, 15, 16, 17, 18, 19 e 20
def mes_com_mais_vendas(df):
    mes_max_vendas = df.loc[df['Valor'] == df['Valor'].max(), 'Mês'].iloc[0]
    return mes_max_vendas

def mes_com_menos_vendas(df):
    mes_min_vendas = df.loc[df['Valor'] == df['Valor'].min(), 'Mês'].iloc[0]
    return mes_min_vendas

def soma_vendas_por_vendedor(df):
    soma_vendas = df.groupby('Vendedor')['Valor'].sum().reset_index()
    return soma_vendas

def vendedor_mais_e_menos_vendeu(df):
    vendas_por_vendedor = soma_vendas_por_vendedor(df)
    vendedor_mais_vendeu = vendas_por_vendedor.loc[vendas_por_vendedor['Valor'].idxmax()]
    vendedor_menos_vendeu = vendas_por_vendedor.loc[vendas_por_vendedor['Valor'].idxmin()]
    return vendedor_mais_vendeu, vendedor_menos_vendeu

# Lendo o arquivo CSV
df = pd.read_csv('arquivo.csv')

# Mês com mais vendas
mes_max = mes_com_mais_vendas(df)
print("Mês com mais vendas:", mes_max)

# Mês com menos vendas
mes_min = mes_com_menos_vendas(df)
print("Mês com menos vendas:", mes_min)

# Soma de vendas por vendedor
soma_vendas_vendedor = soma_vendas_por_vendedor(df)
print("Soma de vendas por vendedor:")
print(soma_vendas_vendedor)

# Vendedor que mais e menos vendeu
vendedor_mais, vendedor_menos = vendedor_mais_e_menos_vendeu(df)
print("Vendedor que mais vendeu:", vendedor_mais['Vendedor'], "- Valor total de vendas:", vendedor_mais['Valor'])
print("Vendedor que menos vendeu:", vendedor_menos['Vendedor'], "- Valor total de vendas:", vendedor_menos['Valor'])
