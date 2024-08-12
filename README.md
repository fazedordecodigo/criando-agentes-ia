# Iniciando com este curso

Estamos muito animados por você iniciar este curso e ver que se inspira em criar aplicações com IA Generativa!

Para tornar o seu tempo bem-sucedido(a), criamos esta página que descreve as etapas de configuração, requisitos técnicos e como obter ajuda quando precisar.

## Etapas de Configuração

Para começar este curso, você precisará concluir as seguintes etapas.

### 1. Faça um Fork deste Repositório

[Faça um fork deste repositório](https://github.com/fazedordecodigo/criando-agentes-ia/fork) para a sua própria conta no GitHub para que possa alterar qualquer código e concluir os desafios. Você também pode [marcar com uma (🌟) este repositório](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars) para encontrar com mais facilidade esse repositório.

### 2. Crie um Codespaces

Para evitar problemas de dependência ao executar o código, recomendamos a execução deste curso em um Codespaces do GitHub.

Isso pode ser criado selecionando a opção `Code` na sua versão `birfucada` deste repositório e selecionando a opção **Codespaces**.

### 3. Armazenando Suas Chaves da API

Manter suas chaves da API seguras e protegidas é importante quando você cria qualquer tipo de aplicação. Recomendamos que você não armazene suas chaves da API diretamente no código com o qual está trabalhando. Pois a inclusão dessas informações num repositório público pode resultar em custos indesejados e problemas a você.

![Dialog showing buttons to create a codespace](./00-setup/images/who-will-pay.webp)

## Como Executar Localmente no seu Computador

Para executar o código localmente no seu computador, você precisará ter alguma versão do [Python instalada](https://www.python.org/downloads).

Para utilizar o repositório, você precisará clonar primeiramente:

```shell
git clone https://github.com/fazedordecodigo/criando-agentes-ia.git
cd criando-agentes-ia
```

Agora, você tem tudo configurado e pode começar a aprender e trabalhar com o código.

### Instalando Poetry (etapa opcional)

Existem vantagens em instalar o **[Poetry](https://python-poetry.org/docs/)** para gerenciar as dependências e o ambiente virtual de seu projeto Python de maneira mais eficiente e organizada. O Poetry facilita o controle das versões das bibliotecas, a instalação de dependências e a criação de arquivos de configuração, como o `pyproject.toml`. A seguir, estão as instruções para instalar o Poetry e integrá-lo ao seu projeto.

#### Passo 1: Instalação do Poetry

Para instalar o Poetry, você pode executar o seguinte comando diretamente no terminal:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Este comando irá baixar e executar o script de instalação do Poetry. Caso prefira, você pode consultar o site oficial do Poetry para outras opções de instalação, como via Homebrew ou diretamente pelo gerenciador de pacotes de sua distribuição Linux.

#### Passo 2: Configuração do Poetry no Projeto

Após a instalação, você precisará adicionar o Poetry ao seu PATH, caso o instalador não tenha feito isso automaticamente. Para verificar se a instalação foi bem-sucedida, execute o seguinte comando:

```bash
poetry --version
```

Se o Poetry estiver corretamente instalado, ele retornará a versão instalada. Agora, você pode iniciar um novo projeto Python ou configurar o Poetry em um projeto existente.

#### Passo 3: Iniciando um Novo Projeto com Poetry

Para criar um novo projeto com o Poetry, navegue até o diretório onde deseja criar o projeto e execute:

```bash
poetry new nome-do-projeto
```

Isso criará uma nova pasta chamada `nome-do-projeto` com a estrutura básica de um projeto Python, incluindo o arquivo `pyproject.toml` que o Poetry usa para gerenciar as dependências e configurações do projeto.

#### Passo 4: Adicionando o Poetry a um Projeto Existente

Se você já tem um projeto Python existente e deseja adicionar o Poetry, basta executar o comando abaixo dentro do diretório do projeto:

```bash
poetry init
```

Este comando iniciará um assistente interativo que ajudará a configurar o arquivo `pyproject.toml`. Ele irá perguntar sobre as dependências e outras configurações do projeto. Responda às perguntas conforme necessário ou simplesmente pressione `Enter` para aceitar as opções padrão.

#### Passo 5: Instalando Dependências

Após a configuração inicial, você pode adicionar dependências ao seu projeto usando o comando:

```bash
poetry add nome-da-dependencia
```

O Poetry instalará a dependência e atualizará o arquivo `pyproject.toml` com a versão exata, garantindo que seu ambiente permaneça consistente.

#### Passo 6: Usando o Ambiente Virtual do Poetry

O Poetry gerencia automaticamente o ambiente virtual para seu projeto. Para ativá-lo, você pode usar o comando:

```bash
poetry shell
```

Dentro deste ambiente, todas as dependências instaladas estarão disponíveis. Para executar comandos no ambiente virtual sem ativá-lo explicitamente, você pode prefixar o comando com `poetry run`, como:

```bash
poetry run python script.py
```

#### Passo 7: Gerenciamento de Dependências

Para ver todas as dependências instaladas e suas versões, use:

```bash
poetry show
```

Para atualizar as dependências para a última versão compatível, execute:

```bash
poetry update
```

Com esses passos, você estará pronto para utilizar o Poetry em seu projeto Python, aproveitando suas funcionalidades para um gerenciamento de dependências mais eficaz e organizado.

### Usando o Visual Studio Code com a Extensão do Python

Provavelmente a melhor maneira de usar o currículo é abrindo no [Visual Studio Code](http://code.visualstudio.com/) com a [Extensão Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python).

> **Observação**: Uma vez que você clonar e abrir o diretório no VS Code, ele automaticamente vai sugerir que você instale as extensões do Python. Você também precisará instalar o `Poetry` conforme descrito acima.

> **Observação**: Se o VS Code sugerir que você reabra o repositório em um container, você precisará recusar isso para usar a instalação local do Python. 

### Usando o Jupyter no Navegador

Você também pode usar o ambiente Jupyter diretamente do navegador em seu próprio computador. Na verdade, tanto o Jupyter clássico quanto o Jupyter Hub proporcionam um ambiente de desenvolvimento bastante conveniente com autocompletamento, destaque de código, etc.

Para iniciar o Jupyter localmente, vá para o diretório do curso e execute:

```bash
jupyter notebook
```

ou

```bash
jupyterhub
```

Você pode navegar para qualquer um dos arquivos `.ipynb`, abre esses arquivos e comece a trabalhar.

### Executando em um Contêiner

Uma alternativa à instalação do Python seria executar o código em um contêiner. Como nosso repositório contém uma pasta especial chamada `.devcontainer`, que instrui como criar um contêiner para este repositório, o VS Code oferecerá a opção de reabrir o código em um contêiner. Isso requer a instalação do Docker e é mais complexo. Assim sendo, recomendado para usuários mais experientes.

Uma das melhores maneiras de manter suas chaves da API seguras ao usar GitHub Codespaces é usando `Codespace Secrets`. Siga este guia sobre como [gerenciar segredos para seus Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces).


## Usando o Serviço Azure OpenAI pela Primeira Vez

Se esta for a primeira vez que você está trabalhando com o serviço Azure OpenAI, siga este guia sobre como [criar e implantar um recurso do Serviço Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst).
