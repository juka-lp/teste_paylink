# Documentação da Estrutura da Pasta `./app/forms`

## Visão Geral

A pasta `./app/forms` contém definições de formulários utilizados na aplicação, que são essenciais para a coleta e validação de dados do usuário. Esses formulários são construídos usando a biblioteca Flask-WTF, que fornece uma interface para criar formulários web de forma segura e eficiente. A estrutura modular permite fácil manutenção e reutilização dos formulários em diferentes partes da aplicação.

## Sumário

- [Pasta: `./app/forms`](#pasta-appforms)
  - [Arquivos e Funcionalidades](#arquivos-e-funcionalidades)
    - [__init__.py](#__init__.py)
    - [auth.py](#auth.py)
    - [category.py](#category.py)
    - [chat.py](#chat.py)
    - [data_event_page.py](#data_event_page.py)
    - [data_home_page.py](#data_home_page.py)
    - [data_privacy_page.py](#data_privacy_page.py)
    - [data_terms_page.py](#data_terms_page.py)
    - [data_ticket_page.py](#data_ticket_page.py)
    - [dispute.py](#dispute.py)
    - [event.py](#event.py)
    - [feedback.py](#feedback.py)
    - [location.py](#location.py)
    - [orders.py](#orders.py)
    - [settings.py](#settings.py)
    - [ticket.py](#ticket.py)
    - [translation.py](#translation.py)
    - [user.py](#user.py)

## Arquivos e Funcionalidades

### Pasta: `./app/forms`

- **Propósito**: Definir formulários utilizados para a coleta e validação de dados do usuário.

#### `__init__.py`

- **Função**: Inicializa o módulo de formulários, permitindo a importação de suas classes e funções em outros módulos.
  
  ```python
  from .auth import (  # noqa: F401
      LoginForm,
      RegistrationForm,
      ForgotForm,
      ChangePasswordForm,
      VerificationCodeForm,
  )
  ```

- **Dependências**: Importa formulários de autenticação de `auth`.

- **Descrição**: Este arquivo serve como um ponto de entrada para o módulo `forms`, permitindo que outras partes da aplicação acessem os formulários definidos dentro dele.

#### `auth.py`

- **Função**: Define formulários relacionados à autenticação de usuários, incluindo login e registro.
  
  ```python
  class LoginForm(FlaskForm):
      user_id = StringField("Username", [DataRequired()])
      password = PasswordField("Password", [DataRequired()])
      submit = SubmitField("Login")
  ```

- **Dependências**: Importa `FlaskForm` e `wtforms`.

- **Descrição**: Este arquivo contém formulários para login, registro e recuperação de senha, garantindo que os dados sejam validados corretamente.

#### `category.py`

- **Função**: Define formulários para a criação e edição de categorias de eventos.
  
  ```python
  class CategoryForm(FlaskForm):
      name = StringField("Category", [DataRequired(), Length(min=3, max=64)])
      picture = FileField("Picture")
      submit = SubmitField("Submit")
  ```

- **Dependências**: Importa `FlaskForm` e `wtforms`.

- **Descrição**: Este arquivo é utilizado para gerenciar categorias de eventos, permitindo que os administradores adicionem ou editem categorias.

#### `chat.py`

- **Função**: Define formulários para upload de arquivos e autenticação no chat.
  
  ```python
  class ChatFileUploadForm(FlaskForm):
      ticket_unique_id = StringField("ticket_unique_id", [DataRequired()])
      ...
  ```

- **Dependências**: Importa `FlaskForm` e `FileField`.

- **Descrição**: Este arquivo contém formulários que permitem o upload de arquivos e a autenticação de usuários no chat.

#### `data_event_page.py`

- **Função**: Define formulários para gerenciar dados da página de eventos.
  
  ```python
  class DataEventPageForm(FlaskForm):
      main_header = StringField("Main header", validators=[Optional()])
      submit = SubmitField("Save")
  ```

- **Dependências**: Importa `FlaskForm` e `wtforms`.

- **Descrição**: Este arquivo é utilizado para gerenciar informações exibidas na página de eventos.

#### `data_home_page.py`

- **Função**: Define formulários para gerenciar dados da página inicial.
  
  ```python
  class DataHomePageForm(FlaskForm):
      main_header = StringField("Main header", validators=[Optional()])
      submit = SubmitField("Save")
  ```

- **Dependências**: Importa `FlaskForm` e `wtforms`.

- **Descrição**: Este arquivo é utilizado para gerenciar informações exibidas na página inicial da aplicação.

#### `data_privacy_page.py`

- **Função**: Define formulários para gerenciar dados da página de privacidade.
  
  ```python
  class DataPrivacyPageForm(FlaskForm):
      main_header = StringField("Main header", validators=[Optional()])
      submit = SubmitField("Save")
  ```

- **Dependências**: Importa `FlaskForm` e `wtforms`.

- **Descrição**: Este arquivo é utilizado para gerenciar informações exibidas na página de privacidade da aplicação.

#### `data_terms_page.py`

- **Função**: Define formulários para gerenciar dados da página de termos de uso.
  
  ```python
  class DataTermsPageForm(FlaskForm):
      main_header = StringField("Main header", validators=[Optional()])
      submit = SubmitField("Save")
  ```

- **Dependências**: Importa `FlaskForm` e `wtforms`.

- **Descrição**: Este arquivo é utilizado para gerenciar informações exibidas na página de termos de uso da aplicação.

#### `data_ticket_page.py`

- **Função**: Define formulários para gerenciar dados da página de tickets.
  
  ```python
  class DataTicketPageForm(FlaskForm):
      main_header = StringField("Main header", validators=[Optional()])
      submit = SubmitField("Save")
  ```

- **Dependências**: Importa `FlaskForm` e `wtforms`.

- **Descrição**: Este arquivo é utilizado para gerenciar informações exibidas na página de tickets da aplicação.

#### `dispute.py`

- **Função**: Define formulários para gerenciar mensagens de disputa.
  
  ```python
  class MessageForm(FlaskForm):
      room_unique_id = StringField("room_unique_id", [DataRequired()])
      message = StringField("message", [DataRequired()])
  ```

- **Dependências**: Importa `FlaskForm` e `wtforms`.

- **Descrição**: Este arquivo é utilizado para coletar informações sobre disputas entre usuários.

#### `event.py`

- **Função**: Define formulários para gerenciar eventos.
  
  ```python
  class EventForm(FlaskForm):
      name = StringField("Event name", [DataRequired(), Length(min=2, max=128)])
      ...
  ```

- **Dependências**: Importa `FlaskForm` e `wtforms`.

- **Descrição**: Este arquivo é utilizado para coletar informações sobre eventos, incluindo nome, data e local.

#### `feedback.py`

- **Função**: Define formulários para coletar feedback dos usuários.
  
  ```python
  class FeedbackForm(FlaskForm):
      author = StringField("Name", validators=[DataRequired()])
      ...
  ```

- **Dependências**: Importa `FlaskForm` e `wtforms`.

- **Descrição**: Este arquivo é utilizado para coletar feedback dos usuários sobre a aplicação.

#### `location.py`

- **Função**: Define formulários para gerenciar locais de eventos.
  
  ```python
  class LocationForm(FlaskForm):
      name = StringField("Location", [DataRequired(), Length(min=3, max=64)])
      ...
  ```

- **Dependências**: Importa `FlaskForm` e `wtforms`.

- **Descrição**: Este arquivo é utilizado para coletar informações sobre locais onde os eventos ocorrerão.

#### `orders.py`

- **Função**: Define formulários para gerenciar pedidos de compra de ingressos.
  
  ```python
  class OrderForm(FlaskForm):
      room_unique_id = StringField("Chat Room ID", validators=[DataRequired()])
  ```

- **Dependências**: Importa `FlaskForm` e `wtforms`.

- **Descrição**: Este arquivo é utilizado para coletar informações sobre pedidos de compra de ingressos.

#### `settings.py`

- **Função**: Define formulários para gerenciar configurações da aplicação.
  
  ```python
  class FeeSettingsForm(FlaskForm):
      service_fee_buyer = IntegerField("service_fee_buyer", validators=[Optional()])
      ...
  ```

- **Dependências**: Importa `FlaskForm` e `wtforms`.

- **Descrição**: Este arquivo é utilizado para coletar informações sobre as taxas e limites de venda e compra.

#### `ticket.py`

- **Função**: Define formulários para gerenciar tickets.
  
  ```python
  class TicketForm(FlaskForm):
      description = StringField("Description", [DataRequired(), Length(min=0, max=256)])
      ...
  ```

- **Dependências**: Importa `FlaskForm` e `wtforms`.

- **Descrição**: Este arquivo é utilizado para coletar informações sobre tickets, incluindo descrição e categoria.

#### `translation.py`

- **Função**: Define formulários para gerenciar traduções de textos.
  
  ```python
  class TranslationForm(FlaskForm):
      name = StringField("Name")
      ...
  ```

- **Dependências**: Importa `FlaskForm` e `wtforms`.

- **Descrição**: Este arquivo é utilizado para coletar informações sobre traduções de textos na aplicação.

#### `user.py`

- **Função**: Define formulários para gerenciar informações de usuários.
  
  ```python
  class UserForm(FlaskForm):
      email = StringField("Email", [DataRequired(), Email()])
      ...
  ```

- **Dependências**: Importa `FlaskForm` e `wtforms`.

- **Descrição**: Este arquivo é utilizado para coletar informações sobre usuários, incluindo email e nome.

---

### Diagrama de Pasta

```
app/
└── forms/
    ├── __init__.py
    ├── auth.py
    ├── category.py
    ├── chat.py
    ├── data_event_page.py
    ├── data_home_page.py
    ├── data_privacy_page.py
    ├── data_terms_page.py
    ├── data_ticket_page.py
    ├── dispute.py
    ├── event.py
    ├── feedback.py
    ├── location.py
    ├── orders.py
    ├── settings.py
    ├── ticket.py
    ├── translation.py
    └── user.py
```

---

### Advertências

- **⚠️ Arquivos Sensíveis**: Certifique-se de não expor informações sensíveis, como chaves de API ou credenciais, em arquivos de configuração ou código-fonte.
