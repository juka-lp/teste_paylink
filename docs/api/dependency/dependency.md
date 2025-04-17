# Documentação da Estrutura da Pasta `./api/dependency`

## Visão Geral

A pasta `./api/dependency` contém definições de dependências que são utilizadas nas rotas da API. Essas dependências incluem funções para gerenciar o banco de dados e autenticação de usuários. A estrutura modular permite uma organização clara e facilita a reutilização de código em diferentes partes da API.

## Sumário

- [Pasta: `./api/dependency`](#pasta-apidependency)
  - [Arquivos e Funcionalidades](#arquivos-e-funcionalidades)
    - [__init__.py](#__init__.py)
    - [database.py](#database.py)
    - [user.py](#user.py)

## Arquivos e Funcionalidades

### Pasta: `./api/dependency`

- **Propósito**: Definir dependências que gerenciam a interação com o banco de dados e a autenticação de usuários na API.

#### `__init__.py`

- **Função**: Inicializa o módulo de dependências, permitindo a importação de suas classes e funções em outros módulos.
  
  ```python
  from .user import get_current_user, get_user  # noqa: F401
  from .database import get_db  # noqa: F401
  ```

- **Dependências**: Importa funções de `user` e `database`.

- **Descrição**: Este arquivo serve como um ponto de entrada para o módulo `dependency`, permitindo que outras partes da aplicação acessem as dependências definidas dentro dele.

#### `database.py`

- **Função**: Define a função `get_db`, que fornece uma sessão de banco de dados para ser utilizada nas rotas da API.
  
  ```python
  def get_db() -> Generator[Session, None, None]:
      with db.Session() as session:
          yield session
  ```

- **Dependências**: Importa `Generator` e `Session` do SQLAlchemy.

- **Descrição**: Este arquivo contém a lógica para gerenciar a conexão com o banco de dados, garantindo que uma sessão de banco de dados esteja disponível para as rotas que a utilizam.

#### `user.py`

- **Função**: Define funções relacionadas à autenticação e recuperação de informações do usuário.
  
  ```python
  def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> m.User:
      ...
  ```

- **Dependências**: Importa `Depends`, `HTTPException`, e `Session` do FastAPI, além de `sa` para interações com o banco de dados.

- **Descrição**: Este arquivo contém a lógica para recuperar o usuário atual com base no token de autenticação, garantindo que apenas usuários autenticados possam acessar recursos protegidos da API.

---

### Inter-relações

A estrutura da pasta `./api/dependency` é projetada para ser modular e interconectada. Aqui estão algumas das principais inter-relações:

- **`__init__.py` e `user.py`**: O arquivo `__init__.py` importa funções do `user.py`, permitindo que a lógica de autenticação e recuperação de usuários esteja disponível em outras partes da aplicação.

- **`user.py` e `database.py`**: As funções em `user.py` utilizam a função `get_db` de `database.py` para acessar o banco de dados e recuperar informações do usuário.

- **`database.py` e Controladores**: A função `get_db` é utilizada por controladores em outras partes da aplicação para garantir que uma sessão de banco de dados esteja disponível ao processar requisições.

---

## Conclusão

A pasta `./api/dependency` é fundamental para a arquitetura da API, organizando a lógica de autenticação e gerenciamento de banco de dados de maneira coesa. Cada arquivo desempenha um papel específico, e suas inter-relações garantem que a API funcione de maneira eficiente e segura.
