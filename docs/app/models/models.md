# Documentação da Estrutura da Pasta `./app/models`

## Visão Geral

A pasta `./app/models` contém as definições dos modelos de dados utilizados na aplicação. Esses modelos representam as entidades principais do sistema, como usuários, eventos, tickets, e suas relações. A estrutura modular permite fácil manutenção e extensão dos modelos conforme a aplicação evolui.

## Sumário

- [Pasta: `./app/models`](#pasta-appmodels)
  - [Arquivos e Funcionalidades](#arquivos-e-funcionalidades)
    - [__init__.py](#__init__.py)
    - [utils.py](#utils.py)
    - [data_cookies_page.py](#data_cookies_page.py)
    - [room.py](#room.py)
    - [global_fee_settings.py](#global_fee_settings.py)
    - [data_event_page.py](#data_event_page.py)
    - [translation.py](#translation.py)
    - [user_notification.py](#user_notification.py)
    - [notification.py](#notification.py)
    - [data_privacy_page.py](#data_privacy_page.py)
    - [data_help_page.py](#data_help_page.py)
    - [message.py](#message.py)
    - [category.py](#category.py)
    - [data_terms_page.py](#data_terms_page.py)
    - [notifications_config.py](#notifications_config.py)
    - [data_home_page.py](#data_home_page.py)
    - [payment.py](#payment.py)
    - [ticket.py](#ticket.py)
    - [users_events.py](#users_events.py)
    - [user.py](#user.py)
    - [location.py](#location.py)
    - [address.py](#address.py)
    - [question.py](#question.py)
    - [review.py](#review.py)
    - [feedback.py](#feedback.py)
    - [picture.py](#picture.py)
    - [data_ticket_page.py](#data_ticket_page.py)
    - [event.py](#event.py)

## Arquivos e Funcionalidades

### Pasta: `./app/models`

- **Propósito**: Definir modelos que representam as entidades principais do sistema.

#### `__init__.py`

- **Função**: Inicializa o módulo de modelos, permitindo a importação de suas classes e funções em outros módulos.
  
  ```python
  from .user import User  # noqa: F401
  from .event import Event  # noqa: F401
  ```

- **Dependências**: Importa modelos de usuários e eventos.

- **Descrição**: Este arquivo serve como um ponto de entrada para o módulo `models`, permitindo que outras partes da aplicação acessem os modelos definidos dentro dele.

#### `utils.py`

- **Função**: Contém funções utilitárias para manipulação de dados e operações comuns entre os modelos.
  
  ```python
  class ModelMixin:
      def save(self, commit=True):
          ...
  ```

- **Dependências**: Importa `db` de `app.database`.

- **Descrição**: Este arquivo fornece métodos comuns para salvar e excluir instâncias de modelos, facilitando a interação com o banco de dados.

#### `data_cookies_page.py`

- **Função**: Define o modelo para a página de política de cookies.
  
  ```python
  class DataCookiesPage(db.Model, ModelMixin):
      ...
  ```

- **Dependências**: Importa `ModelMixin`.

- **Descrição**: Este modelo é utilizado para armazenar informações relacionadas à política de cookies da aplicação.

#### `room.py`

- **Função**: Define o modelo para salas de chat ou disputas.
  
  ```python
  class Room(db.Model, ModelMixin):
      ...
  ```

- **Dependências**: Importa `ModelMixin`.

- **Descrição**: Este modelo é utilizado para gerenciar as interações entre usuários em salas de chat ou disputas.

#### `global_fee_settings.py`

- **Função**: Define o modelo para as configurações de taxas globais da aplicação.
  
  ```python
  class GlobalFeeSettings(db.Model, ModelMixin):
      ...
  ```

- **Dependências**: Importa `ModelMixin`.

- **Descrição**: Este modelo armazena as taxas de serviço e limites de compra e venda aplicáveis a todos os usuários.

#### `data_event_page.py`

- **Função**: Define o modelo para a página de eventos.
  
  ```python
  class DataEventPage(db.Model, ModelMixin):
      ...
  ```

- **Dependências**: Importa `ModelMixin`.

- **Descrição**: Este modelo é utilizado para armazenar informações exibidas na página de eventos.

#### `translation.py`

- **Função**: Define o modelo para traduções de textos na aplicação.
  
  ```python
  class Translation(db.Model, ModelMixin):
      ...
  ```

- **Dependências**: Importa `ModelMixin`.

- **Descrição**: Este modelo é utilizado para armazenar traduções de textos em diferentes idiomas.

#### `user_notification.py`

- **Função**: Define o modelo para notificações de usuários.
  
  ```python
  class UserNotification(db.Model):
      ...
  ```

- **Dependências**: Importa `db`.

- **Descrição**: Este modelo é utilizado para gerenciar as notificações associadas a cada usuário.

#### `notification.py`

- **Função**: Define o modelo para notificações gerais da aplicação.
  
  ```python
  class Notification(db.Model, ModelMixin):
      ...
  ```

- **Dependências**: Importa `ModelMixin`.

- **Descrição**: Este modelo é utilizado para armazenar notificações que podem ser enviadas aos usuários.

#### `data_privacy_page.py`

- **Função**: Define o modelo para a página de política de privacidade.
  
  ```python
  class DataPrivacyPage(db.Model, ModelMixin):
      ...
  ```

- **Dependências**: Importa `ModelMixin`.

- **Descrição**: Este modelo é utilizado para armazenar informações relacionadas à política de privacidade da aplicação.

#### `data_help_page.py`

- **Função**: Define o modelo para a página de ajuda.
  
  ```python
  class DataHelpPage(db.Model, ModelMixin):
      ...
  ```

- **Dependências**: Importa `ModelMixin`.

- **Descrição**: Este modelo é utilizado para armazenar informações e perguntas frequentes na página de ajuda.

#### `message.py`

- **Função**: Define o modelo para mensagens de chat ou disputas.
  
  ```python
  class Message(db.Model, ModelMixin):
      ...
  ```

- **Dependências**: Importa `ModelMixin`.

- **Descrição**: Este modelo é utilizado para gerenciar mensagens enviadas entre usuários.

#### `category.py`

- **Função**: Define o modelo para categorias de eventos.
  
  ```python
  class Category(db.Model, ModelMixin):
      ...
  ```

- **Dependências**: Importa `ModelMixin`.

- **Descrição**: Este modelo é utilizado para armazenar informações sobre categorias de eventos.

#### `data_terms_page.py`

- **Função**: Define o modelo para a página de termos de uso.
  
  ```python
  class DataTermsPage(db.Model, ModelMixin):
      ...
  ```

- **Dependências**: Importa `ModelMixin`.

- **Descrição**: Este modelo é utilizado para armazenar informações relacionadas aos termos de uso da aplicação.

#### `notifications_config.py`

- **Função**: Define o modelo para configurações de notificações de usuários.
  
  ```python
  class NotificationsConfig(db.Model, ModelMixin):
      ...
  ```

- **Dependências**: Importa `ModelMixin`.

- **Descrição**: Este modelo é utilizado para gerenciar quais notificações os usuários desejam receber.

#### `data_home_page.py`

- **Função**: Define o modelo para a página inicial da aplicação.
  
  ```python
  class DataHomePage(db.Model, ModelMixin):
      ...
  ```

- **Dependências**: Importa `ModelMixin`.

- **Descrição**: Este modelo é utilizado para armazenar informações exibidas na página inicial da aplicação.

#### `payment.py`

- **Função**: Define o modelo para gerenciar pagamentos.
  
  ```python
  class Payment(db.Model, ModelMixin):
      ...
  ```

- **Dependências**: Importa `ModelMixin`.

- **Descrição**: Este modelo é utilizado para armazenar informações sobre transações de pagamento.

#### `ticket.py`

- **Função**: Define o modelo para tickets de eventos.
  
  ```python
  class Ticket(db.Model, ModelMixin):
      ...
  ```

- **Dependências**: Importa `ModelMixin`.

- **Descrição**: Este modelo é utilizado para gerenciar informações sobre tickets vendidos e disponíveis.

#### `users_events.py`

- **Função**: Define a tabela de associação entre usuários e eventos.
  
  ```python
  users_events = sa.Table(
      "users_events",
      db.Model.metadata,
      ...
  )
  ```

- **Dependências**: Importa `db`.

- **Descrição**: Este arquivo contém a definição de uma tabela de associação que permite que usuários se inscrevam em eventos.

#### `user.py`

- **Função**: Define o modelo para usuários da aplicação.
  
  ```python
  class User(db.Model, UserMixin, ModelMixin):
      ...
  ```

- **Dependências**: Importa `UserMixin` e `ModelMixin`.

- **Descrição**: Este modelo é utilizado para gerenciar informações sobre os usuários da aplicação, incluindo autenticação e perfis.

#### `location.py`

- **Função**: Define o modelo para locais de eventos.
  
  ```python
  class Location(db.Model, ModelMixin):
      ...
  ```

- **Dependências**: Importa `ModelMixin`.

- **Descrição**: Este modelo é utilizado para armazenar informações sobre locais onde os eventos ocorrerão.

#### `address.py`

- **Função**: Define o modelo para endereços de usuários.
  
  ```python
  class Address(db.Model, ModelMixin):
      ...
  ```

- **Dependências**: Importa `ModelMixin`.

- **Descrição**: Este modelo é utilizado para gerenciar informações sobre endereços associados a usuários.

#### `question.py`

- **Função**: Define o modelo para perguntas frequentes.
  
  ```python
  class Question(db.Model, ModelMixin):
      ...
  ```

- **Dependências**: Importa `ModelMixin`.

- **Descrição**: Este modelo é utilizado para armazenar perguntas e respostas frequentes na aplicação.

#### `review.py`

- **Função**: Define o modelo para avaliações de usuários.
  
  ```python
  class Review(db.Model, ModelMixin):
      ...
  ```

- **Dependências**: Importa `ModelMixin`.

- **Descrição**: Este modelo é utilizado para gerenciar avaliações deixadas por usuários sobre eventos ou serviços.

#### `feedback.py`

- **Função**: Define o modelo para feedback de usuários.
  
  ```python
  class Feedback(db.Model, ModelMixin):
      ...
  ```

- **Dependências**: Importa `ModelMixin`.

- **Descrição**: Este modelo é utilizado para coletar feedback dos usuários sobre a aplicação.

#### `picture.py`

- **Função**: Define o modelo para imagens carregadas na aplicação.
  
  ```python
  class Picture(db.Model, ModelMixin):
      ...
  ```

- **Dependências**: Importa `ModelMixin`.

- **Descrição**: Este modelo é utilizado para armazenar informações sobre imagens associadas a eventos, usuários e categorias.

#### `data_ticket_page.py`

- **Função**: Define o modelo para a página de tickets.
  
  ```python
  class DataTicketPage(db.Model, ModelMixin):
      ...
  ```

- **Dependências**: Importa `ModelMixin`.

- **Descrição**: Este modelo é utilizado para armazenar informações exibidas na página de tickets.

#### `event.py`

- **Função**: Define o modelo para eventos.
  
  ```python
  class Event(db.Model, ModelMixin):
      ...
  ```

- **Dependências**: Importa `ModelMixin`.

- **Descrição**: Este modelo é utilizado para gerenciar informações sobre eventos, incluindo nome, data e local.

---

### Diagrama de Pasta

```
app/
└── models/
    ├── __init__.py
    ├── utils.py
    ├── data_cookies_page.py
    ├── room.py
    ├── global_fee_settings.py
    ├── data_event_page.py
    ├── translation.py
    ├── user_notification.py
    ├── notification.py
    ├── data_privacy_page.py
    ├── data_help_page.py
    ├── message.py
    ├── category.py
    ├── data_terms_page.py
    ├── notifications_config.py
    ├── data_home_page.py
    ├── payment.py
    ├── ticket.py
    ├── users_events.py
    ├── user.py
    ├── location.py
    ├── address.py
    ├── question.py
    ├── review.py
    ├── feedback.py
    ├── picture.py
    ├── data_ticket_page.py
    └── event.py
```

---

### Advertências

- **⚠️ Arquivos Sensíveis**: Certifique-se de não expor informações sensíveis, como chaves de API ou credenciais, em arquivos de configuração ou código-fonte.
