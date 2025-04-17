# Documentação da Estrutura da Pasta `./app/core/enums`

## Visão Geral

A pasta `./app/core/enums` contém definições de enums (tipos enumerados) que são utilizados em toda a aplicação. Esses enums ajudam a padronizar valores e estados, tornando o código mais legível e fácil de manter. A estrutura modular permite fácil acesso e reutilização desses enums em diferentes partes da aplicação.

## Sumário

- [Pasta: `./app/core/enums`](#pasta-appcoreenums)
  - [Arquivos e Funcionalidades](#arquivos-e-funcionalidades)
    - [__init__.py](#__init__.py)
    - [profile.py](#profile.py)
    - [ticket.py](#ticket.py)

## Arquivos e Funcionalidades

### Pasta: `./app/core/enums`

- **Propósito**: Definir enums que representam categorias, estados e perfis utilizados na aplicação.

#### `__init__.py`

- **Função**: Inicializa o módulo de enums, permitindo a importação de suas classes e funções em outros módulos.
  
  ```python
  from .ticket import TicketCategory, TicketStatus, PriceCategory  # noqa: F401
  from .profile import AdminStatus  # noqa: F401
  ```

- **Dependências**: Importa `TicketCategory`, `TicketStatus`, `PriceCategory` de `ticket` e `AdminStatus` de `profile`.

- **Descrição**: Este arquivo serve como um ponto de entrada para o módulo `enums`, permitindo que outras partes da aplicação acessem os enums definidos dentro dele. Através do `__init__.py`, é possível organizar e expor os enums que são essenciais para o funcionamento da aplicação.

#### `profile.py`

- **Função**: Define o enum `AdminStatus`, que representa os diferentes tipos de status que um usuário pode ter dentro da aplicação.
  
  ```python
  class AdminStatus(Enum):
      Buyer = "Buyer"
      FT = "FT"
      SELLER = "Seller"
      DISPUTE = "Dispute"
  ```

- **Dependências**: Nenhuma.

- **Descrição**: Este enum é utilizado para categorizar os diferentes papéis que um usuário pode desempenhar na aplicação, facilitando a gestão de permissões e funcionalidades específicas para cada tipo de usuário.

#### `ticket.py`

- **Função**: Define enums relacionados a tickets, incluindo categorias, status e preços.
  
  ```python
  class TicketCategory(Enum):
      REGULAR = "inteira"
      STUDENT = "estudante"
      SOCIAL = "social"
      ELDERLY = "idoso"
      PCD = "PCD"
      OTHER = "outro"

  class PriceCategory(Enum):
      FULL = "Full Entry"
      HALF = "Half Entry"

  class TicketStatus(Enum):
      AVAILABLE = "For sale"
      RESERVED = "Reserved"
      SOLD = "Sold"
      DISPUTED = "Disputed"
      TRANSFERRED = "Transferred"
      PENDING_TRANSFER = "Pending transfer"
      EXPIRED = "Expirado"
  ```

- **Dependências**: Nenhuma.

- **Descrição**: Esses enums são utilizados para categorizar tickets em diferentes tipos, status e faixas de preço. Eles ajudam a manter a consistência e a clareza em todo o código que lida com tickets, permitindo que a lógica de negócios seja implementada de forma mais intuitiva.

---

### Diagrama de Pasta

```
app/
└── core/
    └── enums/
        ├── __init__.py
        ├── profile.py
        └── ticket.py
```

---

### Advertências

- **⚠️ Arquivos Sensíveis**: Certifique-se de não expor informações sensíveis, como chaves de API ou credenciais, em arquivos de configuração ou código-fonte.
