# Documentação da Estrutura da Pasta `./app/commands`

## Visão Geral

A pasta `./app/commands` contém scripts de comandos que são utilizados para executar várias operações administrativas e de manutenção no projeto. Esses comandos são registrados no contexto da aplicação Flask e podem ser executados através da interface de linha de comando (CLI). Eles são essenciais para a gestão de dados, configuração de usuários, manipulação de eventos e outras funcionalidades administrativas.

## Sumário

- [Estrutura da Pasta](#estrutura-da-pasta)
- [Arquivo `__init__.py`](#arquivo-initpy)

## Estrutura da Pasta

```
app/
└── commands/
    ├── __init__.py
```

### Arquivo: `__init__.py`

- **Propósito**: Este arquivo contém a definição de vários comandos que podem ser executados na linha de comando para gerenciar a aplicação. Os comandos incluem operações como criação de usuários, ativação de contas, manipulação de eventos e backup de banco de dados.

#### Comandos Definidos

1. **`db_populate(count: int)`**
   - **Descrição**: Preenche o banco de dados com dados fictícios.
   - **Parâmetros**: 
     - `count`: Número de instâncias a serem criadas (padrão: 100).
   - **Execução**: 
     ```bash
     flask db_populate --count 50
     ```

2. **`create-admin-from-config()`**
   - **Descrição**: Cria uma conta de super administrador a partir de configurações predefinidas.
   - **Execução**: 
     ```bash
     flask create-admin-from-config
     ```

3. **`create-admin()`**
   - **Descrição**: Cria uma conta de super administrador com entrada dinâmica do usuário.
   - **Execução**: 
     ```bash
     flask create-admin
     ```

4. **`activate-user(email: str)`**
   - **Descrição**: Ativa um usuário pelo e-mail fornecido.
   - **Parâmetros**: 
     - `email`: E-mail do usuário a ser ativado.
   - **Execução**: 
     ```bash
     flask activate-user --email user@example.com
     ```

5. **`print-users()`**
   - **Descrição**: Imprime todos os usuários registrados no banco de dados.
   - **Execução**: 
     ```bash
     flask print-users
     ```

6. **`delete-user(email: str)`**
   - **Descrição**: Deleta um usuário pelo e-mail fornecido.
   - **Parâmetros**: 
     - `email`: E-mail do usuário a ser deletado.
   - **Execução**: 
     ```bash
     flask delete-user --email user@example.com
     ```

7. **`backup-db()`**
   - **Descrição**: Realiza um backup do banco de dados.
   - **Execução**: 
     ```bash
     flask backup-db
     ```

8. **`clear-server(date: str)`**
   - **Descrição**: Limpa dados do servidor para usuários e eventos antes da data especificada.
   - **Parâmetros**: 
     - `date`: Data em formato `YYYY-MM-DD`.
   - **Execução**: 
     ```bash
     flask clear-server --date 2023-01-01
     ```

### Dependências e Relacionamentos

- O arquivo `__init__.py` importa várias bibliotecas e módulos, incluindo:
  - `click`: Para a criação de comandos CLI.
  - `sqlalchemy`: Para interações com o banco de dados.
  - `app.models`: Para manipulação de modelos de dados.
  - `app.controllers`: Para lógica de controle relacionada a usuários e eventos.

## Advertências

⚠️ **Cuidado com arquivos sensíveis**: Certifique-se de que as credenciais e informações sensíveis não sejam expostas em ambientes públicos. 
