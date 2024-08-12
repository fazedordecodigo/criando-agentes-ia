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

![Dialog showing buttons to create a codespace](./images/who-will-pay.webp)

## Como Executar Localmente no seu Computador

Para executar o código localmente no seu computador, você precisará ter alguma versão do [Python instalada](https://www.python.org/downloads).

Para utilizar o repositório, você precisará clonar primeiramente:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Agora, você tem tudo configurado e pode começar a aprender e trabalhar com o código.

### Instalando o miniconda (etapa opcional)

Existem vantagens em instalar o **[miniconda](https://conda.io/en/latest/miniconda.html)** - que é uma instalação bastante leve que suporta o gerenciador de pacotes `conda` para diferentes **ambientes virtuais** do Python. O `conda` facilita a instalação e alternância entre diferentes versões e pacotes do Python e também a instalação de pacotes que não estão disponíveis via `pip`.

Depois de instalar o miniconda, você precisará clonar o repositório (se ainda não o fez) e criar um ambiente virtual a ser usado neste curso:

Antes de executar a etapa abaixo, tenha certeza de que você já possui um arquivo *environment.yml*. O arquivo *environment.yml* é usado para criar um ambiente conda com as dependências necessárias e que pode se parecer com isto:

```yml
name: <environment-name>
channels:  
 - defaults
dependencies:  
- python=<python-version>  
- openai  
- python-dotenv
```

Você pode substituir `<environment-name>` pelo nome do seu ambiente conda e `<python-version>` pela versão do Python que você deseja usar. Coloque o arquivo *environment.yml* criado na pasta *.devcontainer* do seu repositório.

Agora que você criou um arquivo *environment.yml*, você pode criar um ambiente conda com o seguinte comando:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

Se você tiver problemas, consulte este link sobre a criação de [ambientes conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

### Usando o Visual Studio Code com a Extensão do Python

Provavelmente a melhor maneira de usar o currículo é abrindo no [Visual Studio Code](http://code.visualstudio.com/) com a [Extensão Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst).

> **Observação**: Uma vez que você clonar e abrir o diretório no VS Code, ele automaticamente vai sugerir que você instale as extensões do Python. Você também precisará instalar o `Miniconda` conforme descrito acima.

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
