# Documentação da Estrutura da Pasta `./app/schema`

## Visão Geral

A pasta `./app/schema` contém definições de esquemas (schemas) utilizados para validação e serialização de dados na aplicação. Esses esquemas são construídos usando a biblioteca Pydantic, que fornece uma maneira fácil de validar e manipular dados. A estrutura modular permite fácil manutenção e reutilização dos esquemas em diferentes partes da aplicação.

## Sumário

- [Pasta: `./app/schema`](#pasta-appschema)
  - [Arquivos e Funcionalidades](#arquivos-e-funcionalidades)
    - [__init__.py](#__init__.py)
    - [bard_response.py](#bard_response.py)
    - [chat_auth.py](#chat_auth.py)
    - [chat_buy.py](#chat_buy.py)
    - [chat_sell.py](#chat_sell.py)
    - [efi.py](#efi.py)
    - [event.py](#event.py)
    - [notification.py](#notification.py)
    - [pagination.py](#pagination.py)
    - [ticket.py](#ticket.py)
    - [token.py](#token.py)
    - [user.py](#user.py)

## Arquivos e Funcionalidades

### Pasta: `./app/schema`

- **Propósito**: Definir esquemas utilizados para validação e serialização de dados.

#### `__init__.py`

- **Função**: Inicializa o módulo de esquemas, permitindo a importação de suas classes e funções em outros módulos.
  
  ```python
  from .user import User  # noqa: F401
  from .event import Event  # noqa: F401
  ```

- **Dependências**: Importa modelos de usuários e eventos.

- **Descrição**: Este arquivo serve como um ponto de entrada para o módulo `schema`, permitindo que outras partes da aplicação acessem os esquemas definidos dentro dele.

#### `bard_response.py`

- **Função**: Define o esquema para a resposta do modelo Bard, que é utilizado para traduções e informações sobre eventos.
  
  ```python
  class BardResponse(BaseModel):
      event_name: str
      official_url: str
      location: str
      venue: str
      date: str
      time: str

      model_config = SettingsConfigDict(from_attributes=True)
  ```

- **Dependências**: Importa `BaseModel` e `SettingsConfigDict` do Pydantic.

- **Descrição**: Este esquema é utilizado para validar e estruturar as respostas recebidas da API Bard.

#### `chat_auth.py`

- **Função**: Define esquemas relacionados à autenticação de usuários no chat.
  
  ```python
  class ChatAuthParams(ChatAuthRequiredParams):
      ticket_unique_id: str | None = None
      user_message: str | None = None
      ...
  ```

- **Dependências**: Importa `BaseModel` e `SettingsConfigDict`.

- **Descrição**: Este arquivo contém esquemas que ajudam a validar os dados de autenticação dos usuários no chat.

#### `chat_buy.py`

- **Função**: Define esquemas para a compra de ingressos através do chat.
  
  ```python
  class ChatBuyEventParams(ChatBuyRequiredParams):
      user_message: str | None = None
      ...
  ```

- **Dependências**: Importa `BaseModel` e `SettingsConfigDict`.

- **Descrição**: Este arquivo contém esquemas que ajudam a validar os dados necessários para a compra de ingressos.

#### `chat_sell.py`

- **Função**: Define esquemas para a venda de ingressos através do chat.
  
  ```python
  class ChatSellEventParams(ChatSellRequiredParams):
      user_message: str | None = None
      ...
  ```

- **Dependências**: Importa `BaseModel` e `SettingsConfigDict`.

- **Descrição**: Este arquivo contém esquemas que ajudam a validar os dados necessários para a venda de ingressos.

#### `efi.py`

- **Função**: Define esquemas relacionados à integração com a API Efi.
  
  ```python
  class EfiCredentials(BaseModel):
      client_id: str
      client_secret: str
      ...
  ```

- **Dependências**: Importa `BaseModel`.

- **Descrição**: Este arquivo contém esquemas que ajudam a validar os dados necessários para interagir com a API Efi.

#### `event.py`

- **Função**: Define esquemas para eventos.
  
  ```python
  class Event(BaseModel):
      unique_id: str
      name: str
      ...
  ```

- **Dependências**: Importa `BaseModel` e `SettingsConfigDict`.

- **Descrição**: Este arquivo contém esquemas que ajudam a validar os dados relacionados a eventos.

#### `notification.py`

- **Função**: Define esquemas para notificações.
  
  ```python
  class NotificationNewUserRegistered(BaseModel):
      username: str
  ```

- **Dependências**: Importa `BaseModel`.

- **Descrição**: Este arquivo contém esquemas que ajudam a validar os dados relacionados a notificações enviadas aos usuários.

#### `pagination.py`

- **Função**: Define o esquema para a paginação de dados.
  
  ```python
  class Pagination(BaseModel):
      page: int
      total: int
      ...
  ```

- **Dependências**: Importa `BaseModel`.

- **Descrição**: Este arquivo contém um esquema que ajuda a estruturar e validar dados de paginação.

#### `ticket.py`

- **Função**: Define esquemas para tickets.
  
  ```python
  class TicketFilter(BaseModel):
      location: str | None = None
      ...
  ```

- **Dependências**: Importa `BaseModel` e `SettingsConfigDict`.

- **Descrição**: Este arquivo contém esquemas que ajudam a validar os dados relacionados a tickets.

#### `token.py`

- **Função**: Define esquemas para tokens de autenticação.
  
  ```python
  class Token(BaseModel):
      access_token: str
      token_type: str = "bearer"
  ```

- **Dependências**: Importa `BaseModel`.

- **Descrição**: Este arquivo contém esquemas que ajudam a validar os dados relacionados a tokens de autenticação.

#### `user.py`

- **Função**: Define esquemas para usuários.
  
  ```python
  class User(BaseModel):
      id: int
      email: str
      ...
  ```

- **Dependências**: Importa `BaseModel` e `SettingsConfigDict`.

- **Descrição**: Este arquivo contém esquemas que ajudam a validar os dados relacionados a usuários.

---

### Diagrama de Pasta

```
app/
└── schema/
    ├── __init__.py
    ├── bard_response.py
    ├── chat_auth.py
    ├── chat_buy.py
    ├── chat_sell.py
    ├── efi.py
    ├── event.py
    ├── notification.py
    ├── pagination.py
    ├── ticket.py
    ├── token.py
    └── user.py
```

---

### Advertências

- **⚠️ Arquivos Sensíveis**: Certifique-se de não expor informações sensíveis, como chaves de API ou credenciais, em arquivos de configuração ou código-fonte.
