# Documentação da Estrutura da Pasta `./api`

## Visão Geral

A pasta `./api` contém as definições das rotas e controladores que gerenciam a interface de programação de aplicativos (API) da aplicação. Esses arquivos são responsáveis por gerenciar a autenticação, a autorização e a comunicação com os clientes através de requisições HTTP. A estrutura modular permite uma organização clara e facilita a manutenção e a escalabilidade da API.

## Sumário

- [Pasta: `./api`](#pasta-api)
  - [Arquivos e Funcionalidades](#arquivos-e-funcionalidades)
    - [__init__.py](#__init__.py)
    - [oauth2.py](#oauth2.py)

## Arquivos e Funcionalidades

### Pasta: `./api`

- **Propósito**: Definir rotas e controladores que gerenciam a API da aplicação, incluindo autenticação e autorização.

#### `__init__.py`

- **Função**: Inicializa o módulo da API, permitindo a importação de suas classes e funções em outros módulos.
  
  ```python
  from fastapi import FastAPI
  from .oauth2 import create_access_token, verify_access_token  # noqa: F401
  ```

- **Dependências**: Importa `FastAPI` e funções de `oauth2`.

- **Descrição**: Este arquivo serve como um ponto de entrada para o módulo `api`, permitindo que outras partes da aplicação acessem as rotas e funcionalidades definidas dentro dele.

#### `oauth2.py`

- **Função**: Gerencia a autenticação e a geração de tokens JWT (JSON Web Tokens) para usuários.
  
  ```python
  def create_access_token(user_id: int) -> str:
      ...
  ```

- **Dependências**: Importa `JWTError`, `jwt` do `jose`, e `ValidationError` do `pydantic`.

- **Descrição**: Este arquivo contém a lógica para criar e verificar tokens de acesso, garantindo que apenas usuários autenticados possam acessar recursos protegidos da API.

---

### Inter-relações

A estrutura da pasta `./api` é projetada para ser modular e interconectada. Aqui estão algumas das principais inter-relações:

- **`__init__.py` e `oauth2.py`**: O arquivo `__init__.py` importa funções do `oauth2.py`, permitindo que a lógica de autenticação e geração de tokens esteja disponível em outras partes da aplicação.

- **`oauth2.py` e Controladores**: As funções de autenticação e verificação de tokens em `oauth2.py` são utilizadas por controladores em outras partes da aplicação para proteger rotas e garantir que apenas usuários autenticados possam acessar dados sensíveis.

---

## Conclusão

A pasta `./api` é fundamental para a arquitetura da aplicação, organizando a lógica de autenticação e autorização de maneira coesa. Cada arquivo desempenha um papel específico, e suas inter-relações garantem que a API funcione de maneira eficiente e segura.
