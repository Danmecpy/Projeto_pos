# Testes

Esta pasta contém testes unitários e de integração.

## Executando os Testes

```bash
# Executar todos os testes
pytest

# Executar testes com cobertura
pytest --cov=.

# Executar um teste específico
pytest testes/test_exemplo.py
```

## Estrutura

- `test_*.py`: Testes unitários
- `integration/`: Testes de integração
- `fixtures/`: Dados de teste

## Boas Práticas

- Escrever testes para toda lógica de negócio
- Manter testes independentes
- Usar fixtures para dados de teste
- Manter cobertura de testes acima de 80%
