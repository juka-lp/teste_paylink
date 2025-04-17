# Documentação da Estrutura da Pasta `./app/views/admin`

## Visão Geral

A pasta `./app/views/admin` contém as definições das rotas e controladores que gerenciam a interação do administrador com a aplicação. Esses arquivos são responsáveis por renderizar templates, processar formulários e gerenciar a lógica de negócios relacionada a diferentes partes da administração, como gerenciamento de usuários, eventos, categorias, e configurações. A estrutura modular permite fácil manutenção e extensão das funcionalidades administrativas da aplicação.

## Sumário

- [Pasta: `./app/views/admin`](#pasta-appviewsadmin)
  - [Arquivos e Funcionalidades](#arquivos-e-funcionalidades)
    - [__init__.py](#__init__.py)
    - [admin.py](#admin.py)
    - [category.py](#category.py)
    - [data_cookies_page.py](#data_cookies_page.py)
    - [data_event_page.py](#data_event_page.py)
    - [data_home_page.py](#data_home_page.py)
    - [data_privacy_page.py](#data_privacy_page.py)
    - [data_terms_page.py](#data_terms_page.py)
    - [data_ticket_page.py](#data_ticket_page.py)
    - [event.py](#event.py)
    - [feedback.py](#feedback.py)
    - [location.py](#location.py)
    - [notification.py](#notification.py)
    - [seller_payments.py](#seller_payments.py)
    - [settings.py](#settings.py)
    - [tasks.py](#tasks.py)
    - [translations.py](#translations.py)
    - [users.py](#users.py)

## Arquivos e Funcionalidades

### Pasta: `./app/views/admin`

- **Propósito**: Definir rotas e controladores que gerenciam a interação do administrador com a aplicação.

#### `__init__.py`

- **Função**: Inicializa o módulo de views administrativas, permitindo a importação de suas classes e funções em outros módulos.
  
  ```python
  from .admin import admin_blueprint  # noqa: F401
  from .category import category_blueprint  # noqa: F401
  from .data_cookies_page import data_cookies_page_blueprint  # noqa: F401
  from .data_event_page import data_event_page_blueprint  # noqa: F401
  from .data_home_page import data_home_page_blueprint  # noqa: F401
  from .data_privacy_page import data_privacy_page_blueprint  # noqa: F401
  from .data_terms_page import data_terms_page_blueprint  # noqa: F401
  from .data_ticket_page import data_ticket_page_blueprint  # noqa: F401
  from .event import event_blueprint  # noqa: F401
  from .feedback import feedback_blueprint  # noqa: F401
  from .location import location_blueprint  # noqa: F401
  from .notification import notification_blueprint  # noqa: F401
  from .seller_payments import blueprint_seller_payments  # noqa: F401
  from .settings import settings_blueprint  # noqa: F401
  from .tasks import tasks_blueprint  # noqa: F401
  from .translations import translations_blueprint  # noqa: F401
  from .users import blueprint_user  # noqa: F401
  ```

- **Dependências**: Importa blueprints de diferentes módulos de views administrativas.

- **Descrição**: Este arquivo serve como um ponto de entrada para o módulo `admin`, permitindo que outras partes da aplicação acessem as rotas administrativas definidas dentro dele.

#### `admin.py`

- **Função**: Gerencia as rotas principais do painel administrativo, incluindo redirecionamento para a lista de usuários.
  
  ```python
  @admin_blueprint.route("/")
  def admin():
      log(log.INFO, "Admin page requested by [%s]", current_user.id)
      return redirect(url_for("admin.user.get_all"))
  ```

- **Dependências**: Importa `current_user` e `log`.

- **Descrição**: Este arquivo contém a lógica para renderizar a página inicial do painel administrativo.

#### `category.py`

- **Função**: Gerencia as rotas relacionadas a categorias de eventos, incluindo a visualização, adição, edição e exclusão de categorias.
  
  ```python
  @category_blueprint.route("/")
  def get_categories():
      ...
  ```

- **Dependências**: Importa `models`, `forms`, e `db`.

- **Descrição**: Este arquivo contém as rotas que permitem aos administradores gerenciar categorias de eventos.

#### `data_cookies_page.py`

- **Função**: Gerencia as rotas relacionadas à página de política de cookies, incluindo a visualização e edição de dados.
  
  ```python
  @data_cookies_page_blueprint.route("/")
  def get_all():
      ...
  ```

- **Dependências**: Importa `models` e `forms`.

- **Descrição**: Este arquivo contém as rotas que permitem aos administradores gerenciar a política de cookies da aplicação.

#### `data_event_page.py`

- **Função**: Gerencia as rotas relacionadas à página de eventos, incluindo a visualização e edição de dados.
  
  ```python
  @data_event_page_blueprint.route("/")
  def get_all():
      ...
  ```

- **Dependências**: Importa `models` e `forms`.

- **Descrição**: Este arquivo contém as rotas que permitem aos administradores gerenciar informações exibidas na página de eventos.

#### `data_home_page.py`

- **Função**: Gerencia as rotas relacionadas à página inicial, incluindo a visualização e edição de dados.
  
  ```python
  @data_home_page_blueprint.route("/")
  def get_all():
      ...
  ```

- **Dependências**: Importa `models` e `forms`.

- **Descrição**: Este arquivo contém as rotas que permitem aos administradores gerenciar informações exibidas na página inicial da aplicação.

#### `data_privacy_page.py`

- **Função**: Gerencia as rotas relacionadas à página de política de privacidade, incluindo a visualização e edição de dados.
  
  ```python
  @data_privacy_page_blueprint.route("/")
  def get_all():
      ...
  ```

- **Dependências**: Importa `models` e `forms`.

- **Descrição**: Este arquivo contém as rotas que permitem aos administradores gerenciar a política de privacidade da aplicação.

#### `data_terms_page.py`

- **Função**: Gerencia as rotas relacionadas à página de termos de uso, incluindo a visualização e edição de dados.
  
  ```python
  @data_terms_page_blueprint.route("/")
  def get_all():
      ...
  ```

- **Dependências**: Importa `models` e `forms`.

- **Descrição**: Este arquivo contém as rotas que permitem aos administradores gerenciar os termos de uso da aplicação.

#### `data_ticket_page.py`

- **Função**: Gerencia as rotas relacionadas à página de tickets, incluindo a visualização e edição de dados.
  
  ```python
  @data_ticket_page_blueprint.route("/")
  def get_all():
      ...
  ```

- **Dependências**: Importa `models` e `forms`.

- **Descrição**: Este arquivo contém as rotas que permitem aos administradores gerenciar informações exibidas na página de tickets.

#### `event.py`

- **Função**: Gerencia as rotas relacionadas a eventos, incluindo a visualização, adição, edição e exclusão de eventos.
  
  ```python
  @event_blueprint.route("/")
  def get_events():
      ...
  ```

- **Dependências**: Importa `models`, `forms`, e `db`.

- **Descrição**: Este arquivo contém as rotas que permitem aos administradores gerenciar eventos.

#### `feedback.py`

- **Função**: Gerencia as rotas relacionadas ao feedback dos usuários, incluindo a visualização e edição de feedbacks.
  
  ```python
  @feedback_blueprint.route("/")
  def get_feedbacks():
      ...
  ```

- **Dependências**: Importa `models` e `forms`.

- **Descrição**: Este arquivo contém as rotas que permitem aos administradores gerenciar feedbacks deixados por usuários.

#### `location.py`

- **Função**: Gerencia as rotas relacionadas a locais de eventos, incluindo a visualização, adição, edição e exclusão de locais.
  
  ```python
  @location_blueprint.route("/")
  def get_locations():
      ...
  ```

- **Dependências**: Importa `models`, `forms`, e `db`.

- **Descrição**: Este arquivo contém as rotas que permitem aos administradores gerenciar locais onde os eventos ocorrerão.

#### `notification.py`

- **Função**: Gerencia as rotas relacionadas a notificações, incluindo a visualização e gerenciamento de notificações de usuários.
  
  ```python
  @notification_blueprint.route("/")
  def get_notifications():
      ...
  ```

- **Dependências**: Importa `models` e `db`.

- **Descrição**: Este arquivo contém as rotas que permitem aos administradores visualizar e gerenciar notificações.

#### `seller_payments.py`

- **Função**: Gerencia as rotas relacionadas a pagamentos de vendedores, incluindo a visualização e gerenciamento de pagamentos.
  
  ```python
  @blueprint_seller_payments.route("/")
  def list_payments():
      ...
  ```

- **Dependências**: Importa `models` e `db`.

- **Descrição**: Este arquivo contém as rotas que permitem aos administradores gerenciar pagamentos feitos a vendedores.

#### `settings.py`

- **Função**: Gerencia as rotas relacionadas às configurações da aplicação, incluindo a visualização e edição de configurações globais.
  
  ```python
  @settings_blueprint.route("/")
  def general():
      ...
  ```

- **Dependências**: Importa `models`, `forms`, e `db`.

- **Descrição**: Este arquivo contém as rotas que permitem aos administradores gerenciar as configurações da aplicação.

#### `tasks.py`

- **Função**: Gerencia as rotas relacionadas a tarefas agendadas, como envio de e-mails e notificações.
  
  ```python
  @tasks_blueprint.route("/send_email", methods=["POST"])
  def send_email():
      ...
  ```

- **Dependências**: Importa `models` e `db`.

- **Descrição**: Este arquivo contém as rotas que permitem a execução de tarefas agendadas na aplicação.

#### `translations.py`

- **Função**: Gerencia as rotas relacionadas a traduções, incluindo a visualização e edição de traduções de textos.
  
  ```python
  @translations_blueprint.route("/")
  def get_translations():
      ...
  ```

- **Dependências**: Importa `models` e `forms`.

- **Descrição**: Este arquivo contém as rotas que permitem aos administradores gerenciar traduções de textos na aplicação.

#### `users.py`

- **Função**: Gerencia as rotas relacionadas a usuários, incluindo a visualização, adição, edição e exclusão de usuários.
  
  ```python
  @blueprint_user.route("/")
  def get_all():
      ...
  ```

- **Dependências**: Importa `models`, `forms`, e `db`.

- **Descrição**: Este arquivo contém as rotas que permitem aos administradores gerenciar usuários da aplicação.

---

### Diagrama de Pasta

```
app/
└── views/
    └── admin/
        ├── __init__.py
        ├── admin.py
        ├── category.py
        ├── data_cookies_page.py
        ├── data_event_page.py
        ├── data_home_page.py
        ├── data_privacy_page.py
        ├── data_terms_page.py
        ├── data_ticket_page.py
        ├── event.py
        ├── feedback.py
        ├── location.py
        ├── notification.py
        ├── seller_payments.py
        ├── settings.py
        ├── tasks.py
        ├── translations.py
        └── users.py
```

---

### Advertências

- **⚠️ Arquivos Sensíveis**: Certifique-se de não expor informações sensíveis, como chaves de API ou credenciais, em arquivos de configuração ou código-fonte.
