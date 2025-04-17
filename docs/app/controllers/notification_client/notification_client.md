# Documentação da Estrutura da Pasta `./app/controllers/notification_client`

## Visão Geral

A pasta `./app/controllers/notification_client` contém os controladores responsáveis pela gestão de notificações na aplicação. Esses controladores lidam com o envio de notificações para usuários e salas, utilizando diferentes canais, como SSE (Server-Sent Events). A estrutura modular permite uma fácil extensão e manutenção do sistema de notificações.

## Sumário

- [Pasta: `./app/controllers/notification_client`](#pasta-appcontrollersnotification_client)
  - [Arquivos e Funcionalidades](#arquivos-e-funcionalidades)
    - [__init__.py](#__init__.py)
    - [flask.py](#flask.py)
    - [notification.py](#notification.py)

## Arquivos e Funcionalidades

### Pasta: `./app/controllers/notification_client`

- **Propósito**: Controladores que gerenciam a lógica de envio de notificações na aplicação.

#### `__init__.py`

- **Função**: Inicializa o módulo de notificações, permitindo a importação de suas classes e funções em outros módulos.
  
  ```python
  # ruff: noqa: F401
  from .flask import FlaskSSENotification
  from .notification import NotificationType
  ```

- **Dependências**: Nenhuma.

#### `flask.py`

- **Função**: Implementa a lógica de envio de notificações utilizando o Flask SSE (Server-Sent Events).
  
  ```python
  class FlaskSSENotification(NotificationClient):
      def send_notification(
          self,
          data: dict,
          channel: str,
      ):
          sse.publish(data, channel=channel)
  ```

- **Dependências**: Importa `sse` do `flask_sse` e `NotificationClient` do módulo `notification`.

- **Parâmetros principais**:
  - `data`: Um dicionário contendo os dados da notificação a ser enviada.
  - `channel`: O canal para o qual a notificação será enviada.

- **Exemplo de uso**:
  
  ```python
  notification_client = FlaskSSENotification()
  notification_client.send_notification({"message": "Hello!"}, "notification:channel_id")
  ```

#### `notification.py`

- **Função**: Define a classe `NotificationClient` e métodos para gerenciar o envio de notificações para usuários e salas.
  
  ```python
  class NotificationClient(ABC):
      def send_notification(
          self,
          data: dict,
          channel: str,
      ): ...

      def notify_users(
          self,
          users: Iterable[m.User],
          payload: dict,
          session: orm.Session,
          notification_type: NotificationType,
      ):
          ...
  ```

- **Dependências**: Importa `Iterable` do módulo `typing`, `Enum` do módulo `enum`, e `BaseModel` do `pydantic`.

- **Métodos principais**:
  - `send_notification`: Método abstrato para enviar notificações.
  - `notify_users`: Salva notificações no banco de dados e envia notificações para os usuários.
  - `notify_room`: Envia notificações para uma sala específica.
  - `notify_admin`: Envia notificações para administradores.

---

### Diagrama de Pasta

```
app/
└── controllers/
    └── notification_client/
        ├── __init__.py
        ├── flask.py
        └── notification.py
```

---

### Advertências

- **⚠️ Arquivos Sensíveis**: Certifique-se de não expor informações sensíveis, como chaves de API ou credenciais, em arquivos de configuração ou código-fonte.
