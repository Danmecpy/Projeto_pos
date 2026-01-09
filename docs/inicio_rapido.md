# Guia de Início Rápido

## Configuração do Ambiente

### 1. Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Git

### 2. Clone o Repositório

```bash
git clone https://github.com/Danmecpy/Projeto_pos.git
cd Projeto_pos
```

### 3. Crie um Ambiente Virtual

#### Linux/Mac:
```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### 4. Instale as Dependências

```bash
pip install -r requirements.txt
```

## Executando os Exemplos

### Exemplo com Pandas

```bash
python exemplos/exemplo_pandas.py
```

Este exemplo demonstra:
- Criação de datasets
- Estatísticas básicas
- Filtros de dados
- Agregações

### Exemplo de ETL

```bash
python exemplos/exemplo_etl.py
```

Este exemplo demonstra:
- Extração de dados
- Transformação de dados
- Carregamento de dados
- Pipeline ETL completo

## Executando os Testes

```bash
# Executar todos os testes
pytest testes/

# Executar com relatório detalhado
pytest testes/ -v

# Executar com cobertura de código
pytest testes/ --cov=exemplos --cov-report=html
```

## Estrutura de Trabalho Recomendada

1. **Para cada aula**: Crie uma pasta em `aulas/aula_XX/`
2. **Para projetos**: Use a pasta `projetos/`
3. **Para experimentar**: Use a pasta `exemplos/`
4. **Para testes**: Adicione em `testes/`

## Dicas

- Sempre ative o ambiente virtual antes de trabalhar
- Mantenha as dependências atualizadas
- Escreva testes para seu código
- Documente suas soluções
- Use controle de versão (Git)

## Recursos Adicionais

- Consulte o `docs/glossario.md` para termos técnicos
- Veja `docs/README.md` para referências e materiais de estudo
- Cada pasta tem seu próprio README com informações específicas

## Problemas Comuns

### Erro ao instalar dependências

Se houver erro ao instalar alguma dependência, tente:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Erro ao importar módulos

Certifique-se de que o ambiente virtual está ativado:
```bash
# Verifique se (venv) aparece no início do prompt
which python  # Linux/Mac
where python  # Windows
```

## Próximos Passos

1. Execute os exemplos fornecidos
2. Explore o código dos exemplos
3. Modifique os exemplos para experimentar
4. Crie suas próprias soluções
5. Compartilhe seu aprendizado!
