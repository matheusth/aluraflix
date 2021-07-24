## 1 - Sobre

Projeto criado em django com rest framework, para o backend-challenge da alura

## 2 - Instalação do projeto

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

## 3 - Rotas

### 3.1 Videos

#### GET /videos/

**Retorna um json com as informações de todos os videos:**

```json
[
  {
    "id": 1,
    "titulo": "teste3",
    "descricao": "lorem ipsum dolor sit ammet",
    "url": "http://testesimples.com"
  },
  {
    "id": 2,
    "titulo": "teste4",
    "descricao": "lorem ipsum dolor sit ammet",
    "url": "http://testesimples.com"
  }
]
```

### GET /videos/<int: pk>

**Exemplo de url:** `/videos/2`

**Resposta:**

```json
{
  "id": 2,
  "titulo": "teste4",
  "descricao": "lorem ipsum dolor sit ammet",
  "url": "http://testesimples.com"
}
```

### POST /videos/

O codigo de uma requisão bem sucessedida deve ser `201`.

**Corpo da requisição:**

```json
{
  "titulo": "Hello World!",
  "descricao": "lorem ipsum dolor sit ammet",
  "url": "http://localhost.com"
}
```

**Corpo da resposta:**

```json
{
  "id": 19,
  "titulo": "Hello World!",
  "descricao": "lorem ipsum dolor sit ammet",
  "url": "http://localhost.com"
}
```

### PUT /videos/<int: pk>

Atualiza todas as informações do video especificado.

URL de exemplo: `/videos/19`.

O codigo de uma requisão bem sucessedida deve ser `200`.

**Corpo da requisição:**

```json
{
  "titulo": "Hello World!",
  "descricao": "Nova descrição",
  "url": "http://localhost.com"
}
```

**Corpo da resposta:**

```json
{
  "id": 19,
  "titulo": "Hello World!",
  "descricao": "nova descrição",
  "url": "http://localhost.com"
}
```

### PATCH /videos/<int: pk>

Atualiza as informações do video com os campos passados, os campos omitidos não são mudados.

URL de exemplo: `/videos/19`.

O codigo de uma requisão bem sucessedida deve ser `200`.

**Corpo da requisição:**

```json
{
  "titulo": "Novo titulo"
}
```

**Corpo da resposta:**

```json
{
  "id": 19,
  "titulo": "Hello World 2!",
  "descricao": "nova descrição",
  "url": "http://localhost.com"
}
```

### DELETE /videos/<int: pk>

Deleta as informações do video com `id` fornecido no parametro `pk`.

URL de exemplo: `/videos/19` (deleta o video de `id` 19).

O codigo de uma requisão bem sucessedida deve ser `204`.