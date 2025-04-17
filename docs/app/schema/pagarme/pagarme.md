# Documentação da Estrutura da Pasta `./app/schema/pagarme`

## Visão Geral

A pasta `./app/schema/pagarme` contém definições de esquemas (schemas) utilizados para validação e serialização de dados específicos da integração com a API Pagar.me. Esses esquemas são construídos usando a biblioteca Pydantic, que fornece uma maneira fácil de validar e manipular dados. A estrutura modular permite fácil manutenção e reutilização dos esquemas em diferentes partes da aplicação.

## Sumário

- [Pasta: `./app/schema/pagarme`](#pasta-apppagarmep)
  - [Arquivos e Funcionalidades](#arquivos-e-funcionalidades)
    - [__init__.py](#__init__.py)
    - [address.py](#address.py)
    - [api.py](#api.py)
    - [customer.py](#customer.py)
    - [order.py](#order.py)
    - [payment.py](#payment.py)
    - [webhook.py](#webhook.py)

## Arquivos e Funcionalidades

### Pasta: `./app/schema/pagarme`

- **Propósito**: Definir esquemas utilizados para validação e serialização de dados relacionados à API Pagar.me.

#### `__init__.py`

- **Função**: Inicializa o módulo de esquemas Pagar.me, permitindo a importação de suas classes e funções em outros módulos.
  
  ```python
  from .api import PagarmeError, PagarPaging  # noqa: F401
  from .customer import PagarmeCustomerCreate, PagarmeCustomerOutput  # noqa: F401
  from .order import PagarmeCreateOrder, PagarmeCreateOrderResponsePix  # noqa: F401
  from .payment import PagarmePaymentCard  # noqa: F401
  from .webhook import PagarmeWebhookCustomer  # noqa: F401
  ```

- **Dependências**: Importa esquemas de `api`, `customer`, `order`, `payment` e `webhook`.

- **Descrição**: Este arquivo serve como um ponto de entrada para o módulo `pagarme`, permitindo que outras partes da aplicação acessem os esquemas definidos dentro dele.

#### `address.py`

- **Função**: Define o esquema para endereços de cobrança utilizados na API Pagar.me.
  
  ```python
  class PagarmeBillingAddress(BaseModel):
      country: str
      state: str
      line_1: str
      line_2: str | None = None
      zip_code: str
      city: str
  ```

- **Dependências**: Importa `BaseModel` do Pydantic.

- **Descrição**: Este esquema é utilizado para validar e estruturar os endereços de cobrança que são enviados para a API Pagar.me.

#### `api.py`

- **Função**: Define esquemas para erros e respostas da API Pagar.me.
  
  ```python
  class PagarmeError(BaseModel):
      status_code: int
      error: str
      details: str | None = None
  ```

- **Dependências**: Importa `BaseModel` do Pydantic.

- **Descrição**: Este arquivo contém esquemas que ajudam a validar e estruturar as respostas de erro da API Pagar.me.

#### `customer.py`

- **Função**: Define esquemas relacionados a clientes na API Pagar.me.
  
  ```python
  class PagarmeCustomerCreate(BaseModel):
      name: str
      email: str
      document: str
      phones: PagarmeCustomerPhones
  ```

- **Dependências**: Importa `BaseModel` e `PagarmeCustomerPhones`.

- **Descrição**: Este arquivo contém esquemas que ajudam a validar os dados necessários para criar e gerenciar clientes na API Pagar.me.

#### `order.py`

- **Função**: Define esquemas para criação e gerenciamento de pedidos na API Pagar.me.
  
  ```python
  class PagarmeCreateOrder(BaseModel):
      items: list[PagarmeItem]
      customer_id: str
      code: str | None = None
  ```

- **Dependências**: Importa `BaseModel` e `PagarmeItem`.

- **Descrição**: Este arquivo contém esquemas que ajudam a validar os dados necessários para criar e gerenciar pedidos na API Pagar.me.

#### `payment.py`

- **Função**: Define esquemas relacionados a pagamentos na API Pagar.me.
  
  ```python
  class PagarmePaymentCard(BaseModel):
      operation_type: str
      installments: int
      statement_descriptor: str
      card: PagarmeSplitCard
  ```

- **Dependências**: Importa `BaseModel` e `PagarmeSplitCard`.

- **Descrição**: Este arquivo contém esquemas que ajudam a validar os dados necessários para processar pagamentos na API Pagar.me.

#### `webhook.py`

- **Função**: Define esquemas para tratar dados recebidos via webhooks da API Pagar.me.
  
  ```python
  class PagarmeWebhookCustomer(BaseModel):
      id: str
      name: str
      email: str
      ...
  ```

- **Dependências**: Importa `BaseModel`.

- **Descrição**: Este arquivo contém esquemas que ajudam a validar e estruturar os dados recebidos através dos webhooks da API Pagar.me.

---

### Diagrama de Pasta

```
app/
└── schema/
    └── pagarme/
        ├── __init__.py
        ├── address.py
        ├── api.py
        ├── customer.py
        ├── order.py
        ├── payment.py
        └── webhook.py
```

---

### Advertências

- **⚠️ Arquivos Sensíveis**: Certifique-se de não expor informações sensíveis, como chaves de API ou credenciais, em arquivos de configuração ou código-fonte.
