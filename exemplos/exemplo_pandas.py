"""
Exemplo básico de manipulação de dados com Pandas
"""
import pandas as pd
import numpy as np


def criar_dataset_exemplo():
    """Cria um dataset de exemplo para demonstração."""
    dados = {
        'id': range(1, 11),
        'nome': ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo',
                 'Fernanda', 'Gabriel', 'Helena', 'Igor', 'Julia'],
        'idade': [25, 30, 35, 28, 42, 31, 27, 33, 29, 26],
        'cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'São Paulo', 'Curitiba',
                   'Porto Alegre', 'São Paulo', 'Rio de Janeiro', 'Brasília', 'Salvador'],
        'salario': [5000, 6500, 7200, 5800, 9000, 6200, 5500, 7000, 6800, 5300]
    }
    return pd.DataFrame(dados)


def estatisticas_basicas(df):
    """Calcula estatísticas básicas do dataset."""
    print("=" * 50)
    print("ESTATÍSTICAS BÁSICAS")
    print("=" * 50)
    print(f"\nTotal de registros: {len(df)}")
    print(f"\nPrimeiras linhas:")
    print(df.head())
    print(f"\nInformações do dataset:")
    print(df.info())
    print(f"\nEstatísticas descritivas:")
    print(df.describe())


def filtrar_dados(df):
    """Exemplos de filtros em dados."""
    print("\n" + "=" * 50)
    print("EXEMPLOS DE FILTROS")
    print("=" * 50)
    
    # Filtrar por idade
    print("\nPessoas com mais de 30 anos:")
    print(df[df['idade'] > 30])
    
    # Filtrar por cidade
    print("\nPessoas de São Paulo:")
    print(df[df['cidade'] == 'São Paulo'])
    
    # Filtros combinados
    print("\nPessoas de São Paulo com salário acima de 5500:")
    print(df[(df['cidade'] == 'São Paulo') & (df['salario'] > 5500)])


def agrupar_dados(df):
    """Exemplos de agregações."""
    print("\n" + "=" * 50)
    print("AGREGAÇÕES")
    print("=" * 50)
    
    # Média de salário por cidade
    print("\nMédia de salário por cidade:")
    print(df.groupby('cidade')['salario'].mean().sort_values(ascending=False))
    
    # Contagem por cidade
    print("\nContagem de pessoas por cidade:")
    print(df['cidade'].value_counts())


def main():
    """Função principal."""
    print("Exemplo de Manipulação de Dados com Pandas\n")
    
    # Criar dataset
    df = criar_dataset_exemplo()
    
    # Executar exemplos
    estatisticas_basicas(df)
    filtrar_dados(df)
    agrupar_dados(df)
    
    print("\n" + "=" * 50)
    print("Exemplo finalizado com sucesso!")
    print("=" * 50)


if __name__ == "__main__":
    main()
