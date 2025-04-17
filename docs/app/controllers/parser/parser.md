# Documentação da Estrutura da Pasta `./app/controllers/parser`

## Visão Geral

A pasta `./app/controllers/parser` contém os controladores responsáveis pela extração de dados de diferentes fontes de eventos, como sites de venda de ingressos. Esses controladores utilizam técnicas de web scraping para coletar informações sobre eventos, como datas, locais e preços, e armazená-las no banco de dados. A estrutura modular permite fácil manutenção e adição de novos parsers conforme necessário.

## Sumário

- [Pasta: `./app/controllers/parser`](#pasta-appparser)
  - [Arquivos e Funcionalidades](#arquivos-e-funcionalidades)
    - [__init__.py](#__init__.py)
    - [eventium.py](#eventium.py)
    - [ingresse.py](#ingresse.py)
    - [selenium.py](#selenium.py)
    - [t4f.py](#t4f.py)
    - [ticketmaster.py](#ticketmaster.py)
    - [utils.py](#utils.py)
    - [viagogo.py](#viagogo.py)

## Arquivos e Funcionalidades

### Pasta: `./app/controllers/parser`

- **Propósito**: Controladores que gerenciam a lógica de extração de dados de eventos de diferentes fontes.

#### `__init__.py`

- **Função**: Inicializa o módulo de parsing, permitindo a importação de suas classes e funções em outros módulos.
  
  ```python
  # ruff: noqa: F401
  from .ingresse import parse as parse_ingresse
  from .ticketmaster import parse as parse_ticketmaster
  from .eventium import EventiumParser
  from .t4f import T4FParser
  from .viagogo import ViagogoParser
  ```

- **Dependências**: Nenhuma.

#### `eventium.py`

- **Função**: Implementa a lógica de extração de dados de eventos do site Eventium, incluindo a navegação pelas categorias e eventos.
  
  ```python
  class EventiumParser:
      def parse(self):
          ...
  ```

- **Dependências**: Importa `WebDriverWait`, `By`, `EC` do Selenium e `m` de `app.models`.

#### `ingresse.py`

- **Função**: Gerencia a extração de dados de eventos do site Ingresse, incluindo a seleção de categorias e a coleta de informações de eventos.
  
  ```python
  def parse():
      ...
  ```

- **Dependências**: Importa `sa` de `sqlalchemy` e `m` de `app.models`.

#### `selenium.py`

- **Função**: Configura o ambiente do Selenium para a execução de scraping, incluindo a inicialização do navegador e o gerenciamento de sessões.
  
  ```python
  class ParserEnv:
      def setup(self, retry: int = 0) -> Remote | None:
          ...
  ```

- **Dependências**: Importa `webdriver` e `Options` do Selenium, além de `log` de `app.logger`.

#### `t4f.py`

- **Função**: Implementa a lógica de extração de dados do site Tickets for Fun, incluindo a navegação por categorias e eventos.
  
  ```python
  class T4FParser:
      def parse(self):
          ...
  ```

- **Dependências**: Importa `m` de `app.models` e `log` de `app.logger`.

#### `ticketmaster.py`

- **Função**: Gerencia a extração de dados de eventos do site Ticketmaster, incluindo a busca de eventos e a coleta de informações relevantes.
  
  ```python
  def parse():
      ...
  ```

- **Dependências**: Importa `WebDriverWait`, `By`, `EC` do Selenium.

#### `utils.py`

- **Função**: Contém funções utilitárias para manipulação de datas, categorias e imagens durante o processo de scraping.
  
  ```python
  def parse_ingresse_dates(date_string):
      ...
  ```

- **Dependências**: Importa `requests`, `mimetypes` e `datetime`.

#### `viagogo.py`

- **Função**: Implementa a lógica de extração de dados do site Viagogo, incluindo a navegação por eventos e locais.
  
  ```python
  class ViagogoParser:
      def parse(self):
          ...
  ```

- **Dependências**: Importa `m` de `app.models` e `log` de `app.logger`.

---

### Diagrama de Pasta

```
app/
└── controllers/
    └── parser/
        ├── __init__.py
        ├── eventium.py
        ├── ingresse.py
        ├── selenium.py
        ├── t4f.py
        ├── ticketmaster.py
        ├── utils.py
        └── viagogo.py
```

---

### Advertências

- **⚠️ Arquivos Sensíveis**: Certifique-se de não expor informações sensíveis, como chaves de API ou credenciais, em arquivos de configuração ou código-fonte.
