# Desafio backend_python

> Projeto feito em python
>
> [Documentação | Docs](https://CarloRBF.github.io/desafio_backend_python/)

## O projeto visa :

- Faz a formatação e leitura de arquivos txt via POST, para armezanamento dos dados e salvo no banco de dados
- É possível visualizar todos os dados salvos e formatados com paginação do próprio rest_framework

# Instruções para funcionamento:

1. Crie seu ambiente virtual:

```bash
python -m venv venv
```

2. Ative seu venv:

```bash
# linux:
source venv/bin/activate

# windows:
.\venv\Scripts\activate
```

> Use o pip install para instalar todas as dependências
> Use pip install para instalar dependências.

```bash
pip install -r requirements.txt
```

> Para iniciar o servidor

```bash
python manage.py runserver
```

Certifique-se de ter um banco de dados criado com postgresql e que esteja rodando localmente com arquivo .env contendo as informações corretamente.
