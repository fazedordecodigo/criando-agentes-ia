### Configurando Seu Ambiente de Desenvolvimento

Configuramos este repositório e curso com um [container de desenvolvimento](https://containers.dev) que possui um runtime Universal capaz de suportar desenvolvimento em Python3, .NET, Node.js e Java. A configuração relacionada está definida no arquivo `devcontainer.json`, localizado na pasta `.devcontainer/`, na raiz deste repositório.

Para ativar o container de desenvolvimento, inicie-o no [GitHub Codespaces](https://docs.github.com/en/codespaces/overview) (para um runtime hospedado na nuvem) ou no [Docker Desktop](https://docs.docker.com/desktop/) (para um runtime hospedado em dispositivo local). Leia [esta documentação](https://code.visualstudio.com/docs/devcontainers/containers) para mais detalhes sobre como containers de desenvolvimento funcionam no VS Code.

> [!DICA]  
> Recomendamos usar o GitHub Codespaces para um início rápido com esforço mínimo. Ele oferece uma [cota generosa de uso gratuito](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts) para contas pessoais. Configure [tempos de inatividade](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces) para interromper ou excluir codespaces inativos para maximizar o uso da sua cota.


## 1. Executando as Tarefas

Cada aula terá tarefas _opcionais_ que podem ser fornecidas em uma ou mais linguagens de programação, incluindo: Python, .NET/C#, Java e JavaScript/TypeScript. Esta seção fornece orientações gerais relacionadas à execução dessas tarefas.

### 1.1 Tarefas em Python

As tarefas em Python são fornecidas como aplicativos (`arquivos .py`) ou Jupyter notebooks (`arquivos .ipynb`).
- Para executar o notebook, abra-o no Visual Studio Code, depois clique em _Select Kernel_ (no canto superior direito) e selecione a opção padrão Python 3 exibida. Agora você pode clicar em _Run All_ para executar o notebook.
- Para executar aplicativos Python a partir da linha de comando, siga as instruções específicas da tarefa para garantir que você selecione os arquivos corretos e forneça os argumentos necessários.

## 2. Configurando Provedores

As tarefas **podem** também ser configuradas para funcionar com uma ou mais implantações de Modelo de Linguagem de Grande Escala (LLM) através de um provedor de serviços suportado, como OpenAI, Azure ou Hugging Face. Estes fornecem um _endpoint hospedado_ (API) que podemos acessar programaticamente com as credenciais corretas (chave de API ou token). Neste curso, discutimos os seguintes provedores:

- [OpenAI](https://platform.openai.com/docs/models) com diversos modelos, incluindo a série GPT.
- [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/) para modelos OpenAI com foco em prontidão empresarial.
- [Hugging Face](https://huggingface.co/docs/hub/index) para modelos open-source e servidor de inferência.

**Você precisará usar suas próprias contas para esses exercícios**. As tarefas são opcionais, então você pode escolher configurar um, todos ou nenhum dos provedores, dependendo de seus interesses. Algumas orientações para cadastro:

| Cadastro | Custo | Chave API | Playground | Comentários |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup) | [Preços](https://openai.com/pricing#language-models) | [Baseado em Projetos](https://platform.openai.com/api-keys) | [No-Code, Web](https://platform.openai.com/playground) | Vários Modelos Disponíveis |
| [Azure](https://aka.ms/azure/free) | [Preços](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) | [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart) | [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart) | [Documentacao Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/) |
| [Hugging Face](https://huggingface.co/join) | [Preços](https://huggingface.co/pricing) | [Tokens de Acesso](https://huggingface.co/docs/hub/security-tokens) | [Hugging Chat](https://huggingface.co/chat/) | [Hugging Chat tem modelos limitados](https://huggingface.co/chat/models) |
| | | | | |

Siga as instruções abaixo para _configurar_ este repositório para uso com diferentes provedores. Tarefas que requerem um provedor específico conterão uma dessas tags em seus nomes de arquivo:
- `aoai` - requer endpoint Azure OpenAI, chave
- `oai` - requer endpoint OpenAI, chave
- `hf` - requer token Hugging Face

Você pode configurar um, nenhum ou todos os provedores. As tarefas relacionadas simplesmente apresentarão erro se as credenciais estiverem ausentes.

### 2.1 Criar arquivo `.env`

Assumimos que você já leu as orientações acima, se inscreveu com o provedor relevante e obteve as credenciais de autenticação necessárias (API_KEY ou token). No caso do Azure OpenAI, assumimos que você também tem uma implantação válida do serviço Azure OpenAI (endpoint) com pelo menos um modelo GPT implantado para conclusão de chat.

O próximo passo é configurar suas **variáveis de ambiente local** da seguinte forma:

1. Procure na pasta raiz um arquivo `.env.copy` que deve ter o seguinte conteúdo:

   ```bash
   # Provedor OpenAI
   OPENAI_API_KEY='<adicione sua chave API OpenAI aqui>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # O padrão já está definido!
   AZURE_OPENAI_API_KEY='<adicione sua chave AOAI aqui>'
   AZURE_OPENAI_ENDPOINT='<adicione seu endpoint do serviço AOIA aqui>'
   AZURE_OPENAI_DEPLOYMENT='<adicione o nome do seu modelo de conclusão de chat aqui>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<adicione o nome do seu modelo de embeddings aqui>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<adicione sua chave API ou token do Hugging Face aqui>'
   ```

2. Copie esse arquivo para `.env` usando o comando abaixo. Este arquivo é _gitignore-d_, mantendo seus segredos seguros.

   ```bash
   cp .env.copy .env
   ```

3. Preencha os valores (substitua os placeholders à direita de `=`) conforme descrito na próxima seção.

3. (Opcional) Se você usar o GitHub Codespaces, você tem a opção de salvar as variáveis de ambiente como _segredos do Codespaces_ associados a este repositório. Nesse caso, você não precisará configurar um arquivo .env local. **No entanto, observe que esta opção funciona apenas se você usar o GitHub Codespaces.** Você ainda precisará configurar o arquivo .env se usar Docker Desktop.

### 2.2 Preencher o arquivo `.env`

Vamos dar uma olhada rápida nos nomes das variáveis para entender o que elas representam:

| Variável  | Descrição  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Este é o token de acesso do usuário configurado em seu perfil |
| OPENAI_API_KEY | Esta é a chave de autorização para usar o serviço para endpoints OpenAI não Azure |
| AZURE_OPENAI_KEY | Esta é a chave de autorização para usar o serviço |
| AZURE_OPENAI_ENDPOINT | Este é o endpoint implantado para um recurso Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Este é o endpoint de implantação do modelo de _geração de texto_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Este é o endpoint de implantação do modelo de _embeddings de texto_ |
| | |

Nota: As últimas duas variáveis do Azure OpenAI refletem um modelo padrão