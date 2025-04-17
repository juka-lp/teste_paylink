# Documentação da Estrutura da Pasta `./app/views`

## Visão Geral

A pasta `./app/views` contém as definições das rotas e controladores que gerenciam a interação do usuário com a aplicação. Esses arquivos são responsáveis por renderizar templates, processar formulários e gerenciar a lógica de negócios relacionada a diferentes partes da aplicação, como autenticação, eventos, pagamentos e perfis de usuários. A estrutura modular permite fácil manutenção e extensão das funcionalidades da aplicação.

## Sumário

- [Pasta: `./app/views`](#pasta-appviews)
  - [Arquivos e Funcionalidades](#arquivos-e-funcionalidades)
    - [__init__.py](#__init__.py)
    - [auth.py](#auth.py)
    - [efi.py](#efi.py)
    - [events.py](#events.py)
    - [main.py](#main.py)
    - [notification.py](#notification.py)
    - [payments.py](#payments.py)
    - [profile.py](#profile.py)
    - [tasks.py](#tasks.py)
    - [tickets.py](#tickets.py)

## Arquivos e Funcionalidades

### Pasta: `./app/views`

- **Propósito**: Definir rotas e controladores que gerenciam a interação do usuário com a aplicação.

#### `__init__.py`

- **Função**: Inicializa o módulo de views, permitindo a importação de suas classes e funções em outros módulos.
  
  ```python
  from .auth import auth_blueprint  # noqa: F401
  from .main import main_blueprint  # noqa: F401
  from .events import events_blueprint  # noqa: F401
  from .tickets import tickets_blueprint  # noqa: F401
  from .admin import admin_blueprint  # noqa: F401
  from .payments import pay_blueprint  # noqa: F401
  from .notification import notification_blueprint  # noqa: F401
  from .profile import blueprint_profile  # noqa: F401
  from .chat import chat_blueprint  # noqa: F401
  from .efi import efi_blueprint  # noqa: F401
  ```

- **Dependências**: Importa blueprints de diferentes módulos de views.

- **Descrição**: Este arquivo serve como um ponto de entrada para o módulo `views`, permitindo que outras partes da aplicação acessem as rotas definidas dentro dele.

#### `auth.py`

- **Função**: Gerencia as rotas relacionadas à autenticação de usuários, incluindo registro, login, logout e recuperação de senha.
  
  ```python
  @auth_blueprint.route("/register", methods=["GET", "POST"])
  def register():
      ...
  ```

- **Dependências**: Importa `forms`, `models`, e `schema`.

- **Descrição**: Este arquivo contém as rotas e a lógica necessária para gerenciar a autenticação e o registro de usuários.

#### `efi.py`

- **Função**: Gerencia as rotas relacionadas à integração com a API Efi, incluindo webhooks e notificações.
  
  ```python
  @efi_blueprint.route("/webhook", methods=["GET", "POST"])
  def webhook():
      ...
  ```

- **Dependências**: Importa `models` e `schema`.

- **Descrição**: Este arquivo contém as rotas que lidam com a comunicação entre a aplicação e a API Efi.

#### `events.py`

- **Função**: Gerencia as rotas relacionadas a eventos, incluindo a exibição de eventos e a busca por eventos.
  
  ```python
  @events_blueprint.route("/", methods=["GET", "POST"])
  def get_events():
      ...
  ```

- **Dependências**: Importa `models`, `schema`, e `controllers`.

- **Descrição**: Este arquivo contém as rotas que permitem aos usuários visualizar e interagir com eventos.

#### `main.py`

- **Função**: Gerencia a rota principal da aplicação, incluindo a exibição da página inicial.
  
  ```python
  @main_blueprint.route("/")
  def index():
      ...
  ```

- **Dependências**: Importa `models` e `db`.

- **Descrição**: Este arquivo contém a lógica para renderizar a página inicial da aplicação.

#### `notification.py`

- **Função**: Gerencia as rotas relacionadas a notificações, incluindo a visualização e gerenciamento de notificações de usuários.
  
  ```python
  @notification_blueprint.route("/notifications", methods=["GET"])
  def get_notifications():
      ...
  ```

- **Dependências**: Importa `models` e `db`.

- **Descrição**: Este arquivo contém as rotas que permitem aos usuários visualizar suas notificações.

#### `payments.py`

- **Função**: Gerencia as rotas relacionadas a pagamentos, incluindo a criação de pedidos e processamento de pagamentos.
  
  ```python
  @pay_blueprint.route("/ticket_order", methods=["POST", "GET"])
  def ticket_order():
      ...
  ```

- **Dependências**: Importa `models`, `schema`, e `controllers`.

- **Descrição**: Este arquivo contém as rotas que permitem aos usuários realizar pagamentos e gerenciar suas transações.

#### `profile.py`

- **Função**: Gerencia as rotas relacionadas ao perfil do usuário, incluindo edição de informações pessoais e visualização de tickets.
  
  ```python
  @blueprint_profile.route("", methods=["GET"])
  @login_required
  def profile():
      ...
  ```

- **Dependências**: Importa `models`, `forms`, e `db`.

- **Descrição**: Este arquivo contém as rotas que permitem aos usuários gerenciar suas informações de perfil.

#### `tasks.py`

- **Função**: Gerencia as rotas relacionadas a tarefas agendadas, como envio de e-mails e notificações.
  
  ```python
  @tasks_blueprint.route("/send_email", methods=["POST"])
  def send_email():
      ...
  ```

- **Dependências**: Importa `models` e `db`.

- **Descrição**: Este arquivo contém as rotas que permitem a execução de tarefas agendadas na aplicação.

#### `tickets.py`

- **Função**: Gerencia as rotas relacionadas a tickets, incluindo a visualização e gerenciamento de tickets de eventos.
  
  ```python
  @tickets_blueprint.route("/", methods=["GET", "POST"])
  def get_all():
      ...
  ```

- **Dependências**: Importa `models`, `schema`, e `controllers`.

- **Descrição**: Este arquivo contém as rotas que permitem aos usuários visualizar e interagir com tickets de eventos.

---

### Diagrama de Pasta

```
app/
└── views/
    ├── __init__.py
    ├── auth.py
    ├── efi.py
    ├── events.py
    ├── main.py
    ├── notification.py
    ├── payments.py
    ├── profile.py
    ├── tasks.py
    └── tickets.py
```

---

### Advertências

- **⚠️ Arquivos Sensíveis**: Certifique-se de não expor informações sensíveis, como chaves de API ou credenciais, em arquivos de configuração ou código-fonte.
