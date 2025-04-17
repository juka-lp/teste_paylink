# Documentação da Estrutura da Pasta `./app/core/constants`

## Visão Geral

A pasta `./app/core/constants` contém constantes e mapeamentos que são utilizados em toda a aplicação. Essas constantes incluem acrônimos de estados, mapeamentos de categorias de ingressos e outras informações que ajudam a manter a consistência e a legibilidade do código. A estrutura modular permite fácil acesso e manutenção dessas constantes.

## Sumário

- [Pasta: `./app/core/constants`](#pasta-appcoreconstants)
  - [Arquivos e Funcionalidades](#arquivos-e-funcionalidades)
    - [__init__.py](#__init__.py)
    - [chat.py](#chat.py)
    - [states_constants.py](#states_constants.py)

## Arquivos e Funcionalidades

### Pasta: `./app/core/constants`

- **Propósito**: Armazenar constantes e mapeamentos utilizados em toda a aplicação.

#### `__init__.py`

- **Função**: Inicializa o módulo de constantes, permitindo a importação de suas classes e funções em outros módulos.
  
  ```python
  from .states_constants import STATES_ACRONYM  # noqa: F401
  from .chat import FULL_TICKET_CATEGORY_TITLE_MAP, TICKET_CATEGORY_TITLE_MAP  # noqa: F401
  ```

- **Dependências**: Importa `STATES_ACRONYM` de `states_constants` e `FULL_TICKET_CATEGORY_TITLE_MAP`, `TICKET_CATEGORY_TITLE_MAP` de `chat`.

- **Descrição**: Este arquivo serve como um ponto de entrada para o módulo `constants`, permitindo que outras partes da aplicação acessem as constantes definidas dentro dele. Através do `__init__.py`, é possível organizar e expor as constantes que são essenciais para o funcionamento da aplicação.

#### `chat.py`

- **Função**: Define mapeamentos de títulos de categorias de ingressos, facilitando a tradução e apresentação das categorias no sistema.
  
  ```python
  FULL_TICKET_CATEGORY_TITLE_MAP = {
      TicketCategory.REGULAR.value: TicketCategory.REGULAR.value.title(),
      TicketCategory.STUDENT.value: TicketCategory.STUDENT.value.title(),
      TicketCategory.SOCIAL.value: TicketCategory.SOCIAL.value.title(),
      TicketCategory.ELDERLY.value: TicketCategory.ELDERLY.value.title(),
      TicketCategory.PCD.value: "PcD",
      TicketCategory.OTHER.value: "outra".title(),
  }
  ```

- **Dependências**: Importa `TicketCategory` do módulo `app.enums`.

- **Descrição**: Este arquivo contém mapeamentos que associam os valores das categorias de ingressos a suas representações em formato legível. Isso é útil para exibir informações de forma amigável ao usuário.

#### `states_constants.py`

- **Função**: Define um conjunto de acrônimos de estados brasileiros, que podem ser utilizados em diversas partes da aplicação.
  
  ```python
  STATES_ACRONYM = {
      "AC",
      "AL",
      "AP",
      "AM",
      "BA",
      "CE",
      "DF",
      "ES",
      "GO",
      "MA",
      "MT",
      "MS",
      "MG",
      "PA",
      "PB",
      "PR",
      "PE",
      "PI",
      "RJ",
      "RN",
      "RS",
      "RO",
      "RR",
      "SC",
      "SP",
      "SE",
      "TO",
  }
  ```

- **Dependências**: Nenhuma.

- **Descrição**: Este arquivo contém uma coleção de acrônimos que representam os estados brasileiros. Esses acrônimos podem ser utilizados em formulários, relatórios e outras partes da aplicação onde a identificação de estados é necessária.

---

### Diagrama de Pasta

```
app/
└── core/
    └── constants/
        ├── __init__.py
        ├── chat.py
        └── states_constants.py
```

---

### Advertências

- **⚠️ Arquivos Sensíveis**: Certifique-se de não expor informações sensíveis, como chaves de API ou credenciais, em arquivos de configuração ou código-fonte.
