import numpy as np
import pandas as pd
from Array import arr1
from matriz3x3 import mat1
from Dataframe import df
def definir_valor_max():
    valor_max = np.max(arr1)
    print(valor_max)

def definir_media():
    valor_medio = np.mean(arr1)
    print(valor_medio)

def multiplicar_tudo_por_2():
    resultado_multiplicacao = arr1 * 2
    print(resultado_multiplicacao)

def matriz_multiplicacao():
    resultado_mult_matriz = mat1 * 2
    print(resultado_mult_matriz)

def calcular_determinante():
    resultado_determinante = np.linalg.det(mat1)
    print(resultado_determinante)

def adicionar_dados(df):
    nome = input("Insira o nome: ")
    idade = int(input("Insira a idade: "))
    sexo = input("Insira o sexo: (M para Masc, F para Fem")
    medicamento = input("Insira o Medicamento: ")

    inserindo_novos_dados = pd.DataFrame({'Nome': [nome], 'Idade': [idade], 'Sexo': [sexo],'Medicamento': [medicamento]})
    df = df.append(inserindo_novos_dados)
    print(df)



