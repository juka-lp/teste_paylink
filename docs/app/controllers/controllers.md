# Documentação da Estrutura da Pasta `./app/controllers`

## Visão Geral

A pasta `./app/controllers` contém os controladores que gerenciam a lógica de negócios da aplicação. Esses controladores são responsáveis por processar as requisições, interagir com os modelos de dados e retornar as respostas apropriadas. Eles desempenham um papel crucial na arquitetura MVC (Model-View-Controller) do projeto, separando a lógica de apresentação da lógica de negócios.

## Sumário

- [Pasta: `./app/controllers`](#pasta-appcontrollers)
  - [Arquivos e Funcionalidades](#arquivos-e-funcionalidades)
    - [utils.py](#utils.py)
    - [image_upload.py](#image_upload.py)
    - [chat_auth.py](#chat_auth.py)
    - [admin.py](#admin.py)
    - [bard.py](#bard.py)
    - [chat.py](#chat.py)
    - [chat_sell.py](#chat_sell.py)
    - [room.py](#room.py)
    - [chat_buy.py](#chat_buy.py)
    - [chat_shared.py](#chat_shared.py)
    - [events.py](#events.py)
    - [auth.py](#auth.py)
    - [pagination.py](#pagination.py)
    - [ticket.py](#ticket.py)
    - [user.py](#user.py)
    - [payments.py](#payments.py)
    - [mail.py](#mail.py)

## Arquivos e Funcionalidades

### Pasta: `./app/controllers`

- **Propósito**: Controladores que gerenciam a lógica de negócios da aplicação.

#### `utils.py`

- **Função**: Contém funções utilitárias para formatação de datas, manipulação de parâmetros e tradução de textos.
  
  ```python
  def today():
      return datetime.today().strftime("%d/%m/%Y")
  ```

- **Dependências**: Importa `Timezone` de `app.core.utils` e `config`.

#### `image_upload.py`

- **Função**: Gerencia o upload de imagens para o servidor, permitindo a associação de imagens a usuários e eventos.
  
  ```python
  def image_upload(user: m.User, image_type: ImageType):
      ...
  ```

- **Dependências**: Importa `Image` da biblioteca `PIL` e `m` de `app.models`.

#### `chat_auth.py`

- **Função**: Controla a autenticação de usuários no chat, incluindo registro e validação de informações pessoais.
  
  ```python
  def create_email(email: str, room: m.Room) -> tuple[s.ChatAuthEmailValidate, m.User | None]:
      ...
  ```

- **Dependências**: Importa `sa` de `sqlalchemy` e `m` de `app.models`.

#### `admin.py`

- **Função**: Fornece funcionalidades administrativas, como download de dados de tickets, eventos e usuários.
  
  ```python
  def download_tickets(tickets):
      ...
  ```

- **Dependências**: Importa `io` e `csv`.

#### `bard.py`

- **Função**: Interage com a API do Bard para tradução de textos e formatação de datas.
  
  ```python
  def bot_message_translation(text_en: str) -> tuple[str, bool]:
      ...
  ```

- **Dependências**: Importa `requests` e `json`.

#### `chat.py`

- **Função**: Gerencia a lógica do chat, incluindo a exibição da página inicial e o gerenciamento de mensagens.
  
  ```python
  def get_home(user_message: str, room: m.Room) -> str:
      ...
  ```

- **Dependências**: Importa `sa` de `sqlalchemy` e `m` de `app.models`.

#### `chat_sell.py`

- **Função**: Controla a lógica de venda de tickets no chat, incluindo a criação de tickets e a adição de informações.
  
  ```python
  def create_ticket(params: s.ChatSellTicketParams, room: m.Room) -> m.Ticket:
      ...
  ```

- **Dependências**: Importa `sa` de `sqlalchemy` e `m` de `app.models`.

#### `room.py`

- **Função**: Gerencia a criação de salas de chat.
  
  ```python
  def create_room() -> Room:
      ...
  ```

- **Dependências**: Importa `Room` de `app.models`.

#### `chat_buy.py`

- **Função**: Controla a lógica de compra de tickets no chat, incluindo a busca de eventos e tickets disponíveis.
  
  ```python
  def get_events_by_event_name(event_name: str, room: m.Room) -> list[m.Event]:
      ...
  ```

- **Dependências**: Importa `sa` de `sqlalchemy` e `m` de `app.models`.

#### `chat_shared.py`

- **Função**: Contém funções compartilhadas entre diferentes controladores de chat.
  
  ```python
  def redirect_home_and_clear_session():
      ...
  ```

- **Dependências**: Importa `make_response` e `render_template` do Flask.

#### `events.py`

- **Função**: Gerencia a lógica relacionada a eventos, incluindo filtragem e criação de eventos.
  
  ```python
  def get_filter_events():
      ...
  ```

- **Dependências**: Importa `sa` de `sqlalchemy` e `m` de `app.models`.

#### `auth.py`

- **Função**: Gerencia a autenticação de usuários, incluindo verificação de credenciais.
  
  ```python
  def verify_recaptcha(recaptcha_token: str, email: str) -> bool:
      ...
  ```

- **Dependências**: Importa `requests`.

#### `pagination.py`

- **Função**: Controla a lógica de paginação para listas de dados.
  
  ```python
  def create_pagination(total: int, page_size: int = 0, reset_page=True) -> s.Pagination:
      ...
  ```

- **Dependências**: Importa `request` do Flask.

#### `ticket.py`

- **Função**: Gerencia a lógica relacionada a tickets, incluindo busca e filtragem.
  
  ```python
  def get_all_tickets(filter: s.TicketFilter) -> tuple[int, list[Any]]:
      ...
  ```

- **Dependências**: Importa `sa` de `sqlalchemy` e `m` de `app.models`.

#### `user.py`

- **Função**: Gerencia a lógica relacionada a usuários, incluindo criação e remoção de usuários.
  
  ```python
  def delete_user(user: m.User):
      ...
  ```

- **Dependências**: Importa `m` de `app.models`.

#### `payments.py`

- **Função**: Gerencia a lógica de pagamentos, incluindo interações com a API de pagamento.
  
  ```python
  def get_pagarme_customer(customer_id: str) -> s.PagarmeCustomerOutput | s.PagarmeError:
      ...
  ```

- **Dependências**: Importa `requests` e `m` de `app.models`.

#### `mail.py`

- **Função**: Gerencia o envio de emails, incluindo a configuração do serviço de email.
  
  ```python
  def send_email(users: Iterable[m.User], subject: str, body: str):
      ...
  ```

- **Dependências**: Importa `Mail` e `Message` do Flask-Mail.

---

### Diagrama de Pasta

```
app/
├── controllers/
│   ├── utils.py
│   ├── image_upload.py
│   ├── chat_auth.py
│   ├── admin.py
│   ├── bard.py
│   ├── chat.py
│   ├── chat_sell.py
│   ├── room.py
│   ├── chat_buy.py
│   ├── chat_shared.py
│   ├── events.py
│   ├── auth.py
│   ├── pagination.py
│   ├── ticket.py
│   ├── user.py
│   ├── payments.py
│   └── mail.py
```

---

### Advertências

- **⚠️ Arquivos Sensíveis**: Certifique-se de não expor informações sensíveis, como chaves de API ou credenciais, em arquivos de configuração ou código-fonte.
