"""
Exemplo de ETL simples - Extract, Transform, Load
"""
import pandas as pd
from datetime import datetime


class SimpleETL:
    """Classe para demonstrar um processo ETL básico."""
    
    def __init__(self):
        self.dados_brutos = None
        self.dados_transformados = None
    
    def extract(self, fonte='arquivo'):
        """
        Extração de dados.
        Em um cenário real, isso poderia vir de uma API, banco de dados, etc.
        """
        print("[EXTRACT] Extraindo dados...")
        
        # Simulando dados extraídos
        self.dados_brutos = {
            'id_transacao': [1, 2, 3, 4, 5],
            'data': ['2024-01-15', '2024-01-16', '2024-01-16', '2024-01-17', '2024-01-17'],
            'produto': ['Notebook', 'Mouse', 'Teclado', 'Monitor', 'Notebook'],
            'quantidade': [2, 5, 3, 1, 1],
            'valor_unitario': [3000.00, 50.00, 150.00, 800.00, 3200.00],
            'cliente': ['João Silva', 'Maria Santos', 'João Silva', 'Pedro Costa', 'Ana Lima']
        }
        
        print(f"[EXTRACT] {len(self.dados_brutos['id_transacao'])} registros extraídos.")
        return self
    
    def transform(self):
        """
        Transformação de dados.
        Aplica regras de negócio e limpeza.
        """
        print("\n[TRANSFORM] Transformando dados...")
        
        # Converter para DataFrame
        df = pd.DataFrame(self.dados_brutos)
        
        # Transformações
        # 1. Converter data para datetime
        df['data'] = pd.to_datetime(df['data'])
        
        # 2. Calcular valor total
        df['valor_total'] = df['quantidade'] * df['valor_unitario']
        
        # 3. Adicionar categoria de produto
        df['categoria'] = df['produto'].apply(self._categorizar_produto)
        
        # 4. Normalizar nome do cliente
        df['cliente'] = df['cliente'].str.upper()
        
        # 5. Adicionar timestamp de processamento
        df['processado_em'] = datetime.now()
        
        self.dados_transformados = df
        print(f"[TRANSFORM] Transformação concluída. {len(df)} registros processados.")
        
        return self
    
    def _categorizar_produto(self, produto):
        """Categoriza produtos."""
        categorias = {
            'Notebook': 'Informática',
            'Mouse': 'Periféricos',
            'Teclado': 'Periféricos',
            'Monitor': 'Informática'
        }
        return categorias.get(produto, 'Outros')
    
    def load(self, destino='console'):
        """
        Carregamento de dados.
        Em um cenário real, isso seria um banco de dados, data warehouse, etc.
        """
        print("\n[LOAD] Carregando dados...")
        
        if self.dados_transformados is None:
            print("[LOAD] Erro: Nenhum dado transformado disponível.")
            return self
        
        # Simulando carregamento
        if destino == 'console':
            print("\nDados transformados:")
            print(self.dados_transformados)
            
            print("\nResumo:")
            print(f"Total de transações: {len(self.dados_transformados)}")
            print(f"Valor total: R$ {self.dados_transformados['valor_total'].sum():.2f}")
            print(f"\nPor categoria:")
            print(self.dados_transformados.groupby('categoria')['valor_total'].sum())
        
        print("\n[LOAD] Dados carregados com sucesso!")
        return self
    
    def executar(self):
        """Executa o pipeline ETL completo."""
        print("="*60)
        print("INICIANDO PROCESSO ETL")
        print("="*60)
        
        self.extract().transform().load()
        
        print("\n" + "="*60)
        print("PROCESSO ETL CONCLUÍDO")
        print("="*60)


def main():
    """Função principal."""
    etl = SimpleETL()
    etl.executar()


if __name__ == "__main__":
    main()
