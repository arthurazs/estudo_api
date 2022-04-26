# estudo_api

Requisitos

- Python 3.10
- poetry 1.1.13

## Instalacao

No terminal 

```bash
git clone https://github.com/arthurazs/estudo_api.git
cd estudo_api
pip install poetry
poetry install
```

## Execucao

No terminal

```bash
poetry run uvicorn --reload estudo_api.main:app
```

No browser, `/docs` ou `/redoc`

```
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc
```

## Modelo Base

- Pioritário
  - Descrição (1 Obrigatorio)
    - Breve descrição do endpoint contendo para que serve
  - Método [get/post/delete/update] (2 Obrigatorio)
  - Dados de Entrada (3 Obrigatorio)
    - Descrição
    - Tipo do Dado
    - Exemplo de Entrada
    - Se é Obrigatorio
  - Retorno (4 Obrigatorio)
    - Descrição
    - Tipo do Dado
    - Exemplo de Retorno
    - Código do Retorno (7 Opcional)
- Nao Prioritário
  - Descrição
    - Breve descricao de Qual é Saida (1 Obrigatorio)
    - Breve descricao de Quais Dados são de entrada (2 Opicional)
  - Retorno
    - Código do Retorno (3 Opcional)
- Ordernar endpoints (2 Obrigatorio, Não Prioritário)
  - Mais utilizados p/ menos utilizados 
- Quickstart (3 Nao prioritario)
  - Requisitos
  - Instalação
  - Configuração
  - Execução
- Outros exemplos de uso (4 Opcional, Não Prioritário)
