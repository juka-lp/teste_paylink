# Documentação da Estrutura da Pasta `./app/core/utils`

## Visão Geral

A pasta `./app/core/utils` contém funções utilitárias e classes que fornecem suporte a várias funcionalidades da aplicação. Essas utilidades incluem manipulação de documentos, formatação de dados, registro de logs, manipulação de números de telefone, estratégias de validação, gerenciamento de fuso horário e validação de URLs. A estrutura modular permite fácil acesso e reutilização dessas funções em diferentes partes da aplicação.

## Sumário

- [Pasta: `./app/core/utils`](#pasta-appcoreutils)
  - [Arquivos e Funcionalidades](#arquivos-e-funcionalidades)
    - [__init__.py](#__init__.py)
    - [document.py](#document.py)
    - [form.py](#form.py)
    - [logger.py](#logger.py)
    - [mask.py](#mask.py)
    - [phone.py](#phone.py)
    - [strategy.py](#strategy.py)
    - [timezone.py](#timezone.py)
    - [url.py](#url.py)

## Arquivos e Funcionalidades

### Pasta: `./app/core/utils`

- **Propósito**: Fornecer funções utilitárias e classes que suportam a lógica de negócios da aplicação.

#### `__init__.py`

- **Função**: Inicializa o módulo de utilitários, permitindo a importação de suas classes e funções em outros módulos.
  
  ```python
  from .document import DocumentService  # noqa: F401
  from .timezone import Timezone  # noqa: F401
  from .mask import mask_info  # noqa: F401
  ```

- **Dependências**: Importa `DocumentService`, `Timezone` e `mask_info` de seus respectivos módulos.

- **Descrição**: Este arquivo serve como um ponto de entrada para o módulo `utils`, permitindo que outras partes da aplicação acessem as funcionalidades definidas dentro dele.

#### `document.py`

- **Função**: Contém funções para manipulação e validação de documentos, como CPF.
  
  ```python
  class DocumentService:
      @staticmethod
      def clean(document: str) -> str:
          ...
  ```

- **Dependências**: Nenhuma.

- **Descrição**: Este arquivo fornece métodos para limpar e validar documentos, garantindo que os dados estejam em um formato adequado para processamento.

#### `form.py`

- **Função**: Contém funções para validação de campos de formulários, incluindo verificação de comprimento e formatação.
  
  ```python
  def validate_field_length(name, key, value):
      ...
  ```

- **Dependências**: Importa `pt` de `app.controllers.jinja_globals`.

- **Descrição**: Este arquivo é utilizado para garantir que os dados inseridos em formulários atendam a critérios específicos, ajudando a manter a integridade dos dados.

#### `logger.py`

- **Função**: Implementa a lógica de registro de logs, enviando informações para um webhook do Discord.
  
  ```python
  class DiscordLogger:
      def send_log(self, title: str, description: str, details: dict, color: int):
          ...
  ```

- **Dependências**: Importa `requests` e `datetime`.

- **Descrição**: Este arquivo fornece uma interface para registrar eventos e erros, facilitando a monitoração e depuração da aplicação.

#### `mask.py`

- **Função**: Contém funções para mascarar informações sensíveis, como CPF e números de telefone.
  
  ```python
  def mask_info(input, type):
      ...
  ```

- **Dependências**: Nenhuma.

- **Descrição**: Este arquivo é utilizado para formatar informações sensíveis de maneira que não sejam facilmente identificáveis, ajudando a proteger dados pessoais.

#### `phone.py`

- **Função**: Fornece funções para manipulação e validação de números de telefone.
  
  ```python
  class PhoneUtils:
      def generate_customer_phone(self, phone: str):
          ...
  ```

- **Dependências**: Importa `PagarmePhoneData` de `app.schema`.

- **Descrição**: Este arquivo contém métodos para gerar e validar números de telefone, assegurando que os dados estejam em um formato adequado para uso.

#### `strategy.py`

- **Função**: Define estratégias de validação para diferentes tipos de chaves, como CPF, telefone e e-mail.
  
  ```python
  class PixKeyValidationStrategy(ABC):
      @abstractmethod
      def validate(self, key: str) -> tuple[str, bool]:
          ...
  ```

- **Dependências**: Importa `ABC` e `abstractmethod` do módulo `abc`, além de `parse` e `is_valid_number` da biblioteca `phonenumbers`.

- **Descrição**: Este arquivo fornece uma interface para diferentes estratégias de validação, permitindo que a aplicação valide entradas de forma flexível e extensível.

#### `timezone.py`

- **Função**: Gerencia operações relacionadas a fusos horários, incluindo conversões e manipulações de datas.
  
  ```python
  class Timezone:
      @staticmethod
      def now():
          ...
  ```

- **Dependências**: Importa `datetime` e `pytz`.

- **Descrição**: Este arquivo fornece métodos para trabalhar com fusos horários, facilitando a manipulação de datas e horas em diferentes contextos.

#### `url.py`

- **Função**: Contém funções para validação de URLs, garantindo que estejam em um formato correto.
  
  ```python
  def validate_url(url):
      ...
  ```

- **Dependências**: Nenhuma.

- **Descrição**: Este arquivo é utilizado para verificar se as URLs fornecidas estão em um formato válido, ajudando a evitar erros em links e redirecionamentos.

---

### Diagrama de Pasta

```
app/
└── core/
    └── utils/
        ├── __init__.py
        ├── document.py
        ├── form.py
        ├── logger.py
        ├── mask.py
        ├── phone.py
        ├── strategy.py
        ├── timezone.py
        └── url.py
```

---

### Advertências

- **⚠️ Arquivos Sensíveis**: Certifique-se de não expor informações sensíveis, como chaves de API ou credenciais, em arquivos de configuração ou código-fonte.
