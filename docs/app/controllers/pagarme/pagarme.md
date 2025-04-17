# Documentação da Estrutura da Pasta `./app/controllers/pagarme`

## Visão Geral

A pasta `./app/controllers/pagarme` contém os controladores responsáveis pela integração com a API de pagamento Pagar.me. Esses controladores gerenciam a lógica de criação de pedidos, gerenciamento de clientes e cartões, além de tratar exceções específicas da API Pagar.me. A estrutura modular permite uma fácil manutenção e extensão da funcionalidade de pagamento.

## Sumário

- [Pasta: `./app/controllers/pagarme`](#pasta-apppagarme)
  - [Arquivos e Funcionalidades](#arquivos-e-funcionalidades)
    - [__init__.py](#__init__.py)
    - [exceptions.py](#exceptions.py)
    - [pagarme_client.py](#pagarme_client.py)

## Arquivos e Funcionalidades

### Pasta: `./app/controllers/pagarme`

- **Propósito**: Controladores que gerenciam a lógica de integração com a API de pagamento Pagar.me.

#### `__init__.py`

- **Função**: Inicializa o módulo Pagar.me, permitindo a importação de suas classes e funções em outros módulos.
  
  ```python
  # ruff: noqa: F401
  from .pagarme_client import PagarmeClient
  from .exceptions import APIGetCustomerError, WrongUrlError
  ```

- **Dependências**: Nenhuma.

#### `exceptions.py`

- **Função**: Define exceções personalizadas para tratar erros específicos relacionados à API Pagar.me.
  
  ```python
  class WrongUrlError(Exception):
      def __init__(self, base_url: str, path: str, path_params: dict):
          super().__init__(f"Wrong URL: base -> {base_url} path -> {path} params -> {path_params}")

  class APIGetCustomerError(Exception):
      def __init__(self):
          super().__init__("API error on getting customers from pagarme.")

  class APIConnectionError(Exception):
      def __init__(self):
          super().__init__("API connection error. Most cases it's because of wrong IP (Brazil).")

  class APICreateOrderError(Exception):
      def __init__(self, error_msg: str):
          super().__init__(f"Create order error. {error_msg}")
  ```

- **Dependências**: Nenhuma.

#### `pagarme_client.py`

- **Função**: Implementa a lógica de interação com a API Pagar.me, incluindo a criação de pedidos, gerenciamento de clientes e cartões.
  
  ```python
  class PagarmeClient:
      def create_order(self, order_data: s.PagarmeCreateOrderInput):
          ...
  ```

- **Dependências**: Importa `requests`, `BaseModel` e `ValidationError` do `pydantic`, além de `m` e `s` de `app.models` e `app.schema`, respectivamente.

- **Parâmetros principais**:
  - `order_data`: Um objeto do tipo `s.PagarmeCreateOrderInput` que contém os dados do pedido a ser criado.

- **Exemplo de uso**:
  
  ```python
  pagarme_client = PagarmeClient()
  pagarme_client.configure(config)
  response = pagarme_client.create_order(order_data)
  ```

---

### Diagrama de Pasta

```
app/
└── controllers/
    └── pagarme/
        ├── __init__.py
        ├── exceptions.py
        └── pagarme_client.py
```

---

### Advertências

- **⚠️ Arquivos Sensíveis**: Certifique-se de não expor informações sensíveis, como chaves de API ou credenciais, em arquivos de configuração ou código-fonte.
