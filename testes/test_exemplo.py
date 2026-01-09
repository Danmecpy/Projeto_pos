"""
Exemplo de testes unitários para funções de engenharia de dados
"""
import pytest
import pandas as pd
import sys
from pathlib import Path

# Adicionar o diretório de exemplos ao path
sys.path.insert(0, str(Path(__file__).parent.parent / 'exemplos'))

from exemplo_pandas import criar_dataset_exemplo


class TestDatasetExemplo:
    """Testes para o dataset de exemplo."""
    
    def test_criar_dataset_retorna_dataframe(self):
        """Testa se a função retorna um DataFrame."""
        df = criar_dataset_exemplo()
        assert isinstance(df, pd.DataFrame)
    
    def test_dataset_tem_colunas_esperadas(self):
        """Testa se o dataset tem todas as colunas esperadas."""
        df = criar_dataset_exemplo()
        colunas_esperadas = ['id', 'nome', 'idade', 'cidade', 'salario']
        assert list(df.columns) == colunas_esperadas
    
    def test_dataset_tem_10_registros(self):
        """Testa se o dataset tem 10 registros."""
        df = criar_dataset_exemplo()
        assert len(df) == 10
    
    def test_coluna_id_e_unica(self):
        """Testa se a coluna id não tem valores duplicados."""
        df = criar_dataset_exemplo()
        assert df['id'].is_unique
    
    def test_idade_sempre_positiva(self):
        """Testa se todas as idades são positivas."""
        df = criar_dataset_exemplo()
        assert (df['idade'] > 0).all()
    
    def test_salario_sempre_positivo(self):
        """Testa se todos os salários são positivos."""
        df = criar_dataset_exemplo()
        assert (df['salario'] > 0).all()
    
    def test_sem_valores_nulos(self):
        """Testa se não há valores nulos no dataset."""
        df = criar_dataset_exemplo()
        assert not df.isnull().any().any()


class TestTransformacoesDados:
    """Testes para transformações de dados."""
    
    def test_filtro_por_idade(self):
        """Testa filtro por idade."""
        df = criar_dataset_exemplo()
        resultado = df[df['idade'] > 30]
        assert (resultado['idade'] > 30).all()
    
    def test_filtro_por_cidade(self):
        """Testa filtro por cidade."""
        df = criar_dataset_exemplo()
        resultado = df[df['cidade'] == 'São Paulo']
        assert (resultado['cidade'] == 'São Paulo').all()
    
    def test_agregacao_media_salario(self):
        """Testa cálculo de média de salário."""
        df = criar_dataset_exemplo()
        media = df['salario'].mean()
        assert isinstance(media, (int, float))
        assert media > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
