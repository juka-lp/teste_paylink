# Documentação da Estrutura da Pasta `./api/routes`

## Visão Geral

A pasta `./api/routes` contém as definições das rotas da API da aplicação, que gerenciam a comunicação entre o cliente e o servidor. Esses arquivos são responsáveis por processar requisições HTTP, gerenciar autenticação, manipular dados de eventos e usuários, e retornar respostas apropriadas. A estrutura modular permite uma organização clara e facilita a manutenção e a escalabilidade da API.

## Sumário

- [Pasta: `./api/routes`](#pasta-apiroutes)
  - [Arquivos e Funcionalidades](#arquivos-e-funcionalidades)
    - [__init__.py](#__init__.py)
    - [auth.py](#auth.py)
    - [events.py](#events.py)
    - [user.py](#user.py)

## Arquivos e Funcionalidades

### Pasta: `./api/routes`

- **Propósito**: Definir rotas que gerenciam a interação do cliente com a API, incluindo autenticação e manipulação de dados.

#### `__init__.py`

- **Função**: Inicializa o módulo de rotas, permitindo a importação de suas classes e funções em outros módulos.
  
  ```python
  from fastapi import APIRouter
  from .auth import router as auth_router  # noqa: F401
  from .events import events_router  # noqa: F401
  from .user import user_router  # noqa: F401
  ```

- **Dependências**: Importa `APIRouter` do FastAPI e routers de `auth`, `events`, e `user`.

- **Descrição**: Este arquivo serve como um ponto de entrada para o módulo `routes`, permitindo que outras partes da aplicação acessem as rotas definidas dentro dele.

#### `auth.py`

- **Função**: Gerencia as rotas relacionadas à autenticação de usuários, incluindo login e geração de tokens de acesso.
  
  ```python
  @router.post("/login", status_code=status.HTTP_200_OK, response_model=s.Token)
  def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
      ...
  ```

- **Dependências**: Importa `Depends`, `APIRouter`, e `OAuth2PasswordRequestForm` do FastAPI, além de `create_access_token` para geração de tokens.

- **Descrição**: Este arquivo contém a lógica para gerenciar o login de usuários e a geração de tokens de autenticação.

#### `events.py`

- **Função**: Gerencia as rotas relacionadas a eventos, incluindo a busca e visualização de eventos disponíveis.
  
  ```python
  @events_router.post("/", status_code=status.HTTP_200_OK, response_model=s.Events)
  def get_events(events_input: s.EventsInput):
      ...
  ```

- **Dependências**: Importa `Depends`, `APIRouter`, e `Session` do SQLAlchemy, além de modelos e esquemas relacionados a eventos.

- **Descrição**: Este arquivo contém a lógica para gerenciar a busca e visualização de eventos, permitindo que os usuários acessem informações sobre eventos disponíveis.

#### `user.py`

- **Função**: Gerencia as rotas relacionadas a usuários, incluindo a recuperação de informações do perfil do usuário atual.
  
  ```python
  @user_router.get("/me", status_code=status.HTTP_200_OK, response_model=s.User)
  def get_current_user_profile(current_user: m.User = Depends(get_current_user)):
      ...
  ```

- **Dependências**: Importa `Depends`, `APIRouter`, e modelos relacionados a usuários.

- **Descrição**: Este arquivo contém a lógica para gerenciar informações do usuário, permitindo que os usuários acessem seus perfis e dados associados.

---

### Inter-relações

A estrutura da pasta `./api/routes` é projetada para ser modular e interconectada. Aqui estão algumas das principais inter-relações:

- **`__init__.py` e Outros Arquivos**: O arquivo `__init__.py` importa routers de `auth`, `events`, e `user`, permitindo que a aplicação acesse todas as rotas definidas nesses arquivos.

- **`auth.py` e `oauth2.py`**: As rotas de autenticação em `auth.py` utilizam funções de `oauth2.py` para gerar e verificar tokens de acesso, garantindo que apenas usuários autenticados possam acessar recursos protegidos.

- **`events.py` e `models`**: As rotas em `events.py` interagem com os modelos de eventos para buscar e retornar informações sobre eventos disponíveis.

- **`user.py` e `models`**: As rotas em `user.py` utilizam modelos de usuários para recuperar informações do perfil do usuário atual.

---

## Conclusão

A pasta `./api/routes` é fundamental para a arquitetura da API, organizando a lógica de autenticação, eventos e usuários de maneira coesa. Cada arquivo desempenha um papel específico, e suas inter-relações garantem que a API funcione de maneira eficiente e segura.
