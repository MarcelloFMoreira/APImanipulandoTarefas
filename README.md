# Gerenciador de Tarefas

Este é um gerenciador de tarefas simples, desenvolvido utilizando **Flask** para o backend e **HTML/CSS/JavaScript** para o frontend. Ele permite gerenciar suas tarefas (adicionar, listar, marcar como concluídas ou pendentes e remover) em um banco de dados **SQL Server**, com cache implementado via **Redis** para otimizar a performance.

## Tecnologias Utilizadas

- **Backend**: Flask, PyODBC, Redis
- **Frontend**: HTML, CSS, JavaScript
- **Banco de Dados**: SQL Server
- **Cache**: Redis

## Funcionalidades

- **Listar Tarefas**: Recupera e exibe todas as tarefas do banco de dados, utilizando cache para melhorar a performance.
- **Adicionar Tarefa**: Permite adicionar uma nova tarefa ao banco de dados.
- **Marcar como Completa**: Atualiza o status de uma tarefa para "completa".
- **Marcar como Pendente**: Atualiza o status de uma tarefa para "pendente".
- **Remover Tarefa**: Remove uma tarefa do banco de dados.

## Pré-requisitos

Antes de executar o projeto, certifique-se de que você tem:

- Python 3.x instalado.
- Redis instalado e em execução.
- SQL Server configurado e acessível.
- As bibliotecas necessárias instaladas:

  ```bash
  pip install Flask Flask-CORS pyodbc redis



## Configuração do Banco de Dados

1. Crie um banco de dados no SQL Server chamado `PythonSQL`.
2. Crie uma tabela chamada `Tarefas` com a seguinte estrutura:

    ```sql
    CREATE TABLE Tarefas (
        id INT IDENTITY(1,1) PRIMARY KEY,
        nome_tarefa NVARCHAR(255),
        stat NVARCHAR(50)
    );

    
## Executando o Projeto

### Clone o repositório:

    git clone https://github.com/seu-usuario/gerenciador-de-tarefas.git

### Navegue até o diretório do projeto:

    cd APImanipulandoTarefas
    
### Execute o servidor Flask:
      python app.py
