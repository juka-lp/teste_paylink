# Documentação da Estrutura da Pasta `./app/controllers/efi`

## Visão Geral

A pasta `./app/controllers/efi` contém os controladores relacionados à integração com a API de pagamento Efi. Esses controladores gerenciam a lógica de pagamento, incluindo o envio de pagamentos, configuração de webhooks e tratamento de exceções específicas da API Efi.

## Sumário

- [Pasta: `./app/controllers/efi`](#pasta-appcontrollersefi)
  - [Arquivos e Funcionalidades](#arquivos-e-funcionalidades)
    - [__init__.py](#__init__.py)
    - [efi.py](#efi.py)
    - [exceptions.py](#exceptions.py)

## Arquivos e Funcionalidades

### Pasta: `./app/controllers/efi`

- **Propósito**: Controladores que gerenciam a lógica de integração com a API de pagamento Efi.

#### `__init__.py`

- **Função**: Inicializa o módulo Efi, permitindo a importação de suas classes e funções em outros módulos.
  
  ```python
  # ruff: noqa: F401
  from .efi import EfiClient
  ```

- **Dependências**: Nenhuma.

#### `efi.py`

- **Função**: Implementa a lógica de interação com a API Efi, incluindo o envio de pagamentos e configuração de webhooks.
  
  ```python
  class EfiClient:
      ...
      def pay_pix(self, ticket: m.Ticket):
          ...
  ```

- **Dependências**: Importa `EfiPay` da biblioteca `efipay`, `log` de `app.logger`, e `m` de `app.models`.

- **Parâmetros principais**:
  - `ticket`: Um objeto do tipo `m.Ticket` que contém informações sobre o ticket a ser pago.

- **Exemplo de uso**:
  
  ```python
  efi_client = EfiClient()
  efi_client.configure(config)
  efi_client.pay_pix(ticket)
  ```

#### `exceptions.py`

- **Função**: Define exceções personalizadas para tratar erros específicos relacionados à API Efi.
  
  ```python
  class EfiResponseError(Exception):
      def __init__(self, message):
          super().__init__(message)
          log(log.ERROR, "Efi response error: %s", message)
  ```

- **Dependências**: Importa `m` de `app.models` e `log` de `app.logger`.

- **Exceções definidas**:
  - `EfiResponseError`: Erro genérico para respostas inválidas da API Efi.
  - `EfiPayResponseError`: Erro específico para falhas no pagamento.
  - `EfiPayNullableTicketError`: Erro quando um pagamento é feito com preço de ticket nulo.
  - `EfiSellerWithNoKeyError`: Erro quando um vendedor não possui uma chave EFI.

---

### Diagrama de Pasta

```
app/
└── controllers/
    └── efi/
        ├── __init__.py
        ├── efi.py
        └── exceptions.py
```

---

### Advertências

- **⚠️ Arquivos Sensíveis**: Certifique-se de não expor informações sensíveis, como chaves de API ou credenciais, em arquivos de configuração ou código-fonte.
