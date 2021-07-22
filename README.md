## Sobre

Projeto criado em django com rest framework, para o backend-challenge da alura

## Instalação do projeto

1 - Clone o repositório

```bash
$ git clone https://github.com/matheusth/PSDjango.git
```

2 - Depois crie um ambiente virtual python e o ative:

```bash
$ python -m venv .venv
$ source .venv/bin/activate
```

*.venv* pode ser subistituido por qualquer nome de diretorio de sua preferencia.

3 - Rode o `pip` para instalar os pacotes necessários.

```bash
$ pip install -r requirements.txt
```

4 - Crie um arquivo *.env* e copie o conteudo do arquivo *.env-exemple*, e depois edite o arquivo de acordo com as suas
configurações.

5 - Execute o servidor de desenvolvimento do django:

```bash
$ python manage.py runserver
```