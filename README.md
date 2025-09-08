# Desafio MBA Engenharia de Software com IA - Full Cycle

## Tecnologias obrigatórias

- **Linguagem**: Python
- **Framework**: LangChain
- **Banco de dados**: Postgres + pgVector
- **Execução do banco de dados**: Docker & Docker Compose (docker-compose fornecido no repositório de exemplo)

---

## Pacotes recomendados

- **Split**: from langchain_text_splitters import RecursiveCharacterTextSplitter
- **Embeddings (OpenAI)**: from langchain_openai import OpenAIEmbeddings
- **Embeddings (Gemini)**: from langchain_google_gemini import GoogleGenerativeAIEmbeddings
- **PDF**: from langchain_community.document_loaders import PyPDFLoader
- **Ingestão**: from langchain_postgres import PGVector
- **Busca**: similarity_search_with_score(query, k=10)

---

## OpenAI

- Crie um **API Key** da OpenAI
- **Modelo de embeddings**: text-embedding-3-small
- **Modelo de LLM para responder**: gpt-5-nano

## Gemini

- Crie uma **API Key** da Google
- **Modelo de embeddings**: models/embedding-001
- **Modelo de LLM para responder**: gemini-2.5-flash-lite

---

## VirtualEnv para Python

Crie e ative um ambiente virtual antes de instalar as dependências:

```bash
python3 -m venv venv
source venv/bin/activate
```

Instale as dependências através do arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## Ordem de execução

1. Crie um arquivo `.env` baseado no arquivo `.env.example` e adicione os dados que faltam:

- GOOGLE_API_KEY e/ou OPENAI_API_KEY
- DATABASE_URL
- PGVECTOR_COLLECTION_NAME
- PDF_PATH

2. Subir o banco de dados:

```bash
docker compose up -d
```

3. Executar ingestão do PDF:

```bash
python3 src/ingest.py
```

4. Rodar o chat:

```bash
python3 src/chat.py
```

---
