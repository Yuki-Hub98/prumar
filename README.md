# 🧠 Backend - Prumar AI (FastAPI + LangGraph + LLM)

Este é o backend do sistema **Prumar AI**, responsável por:

* 💬 Processamento de chat com IA (LLM local via Ollama)
* ⚙️ Orquestração de agentes (LangGraph)
* 📡 Exposição de API REST (FastAPI)
* 🔗 Integração com frontend React

---

# 🚀 Tecnologias Utilizadas

* ⚡ FastAPI — API rápida e assíncrona
* 🔗 LangGraph — orquestração de agentes
* 🧠 LangChain — integração com LLMs
* 🤖 Ollama — execução local de modelos (ex: llama3)
* 📊 Langfuse — observabilidade (opcional)
* 🐍 Python 3.11

---

# 📦 Requisitos

Antes de rodar o projeto, você precisa ter instalado:

* 🐳 Docker
* 🐳 Docker Compose
* 🤖 Ollama (caso use LLM local)

---

# 🧠 Sobre o Ollama (LLM local)

O projeto utiliza LLM local via Ollama.

Certifique-se de que o Ollama está rodando:

```bash
ollama run llama3
```

---

# ⚙️ Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
OLLAMA_BASE_URL=http://host.docker.internal:11434
```

📌 Importante:

* Dentro do Docker, `localhost` NÃO funciona
* Use `host.docker.internal`

---

# 🐳 Docker

## 📌 Criar network externa

Antes de subir os containers:

```bash
docker network create projeto_prumar
```

---

## 📌 Build da aplicação

```bash
docker compose build
```

---

## 📌 Subir o backend

```bash
docker compose up
```

---

## 📌 Rodar em background

```bash
docker compose up -d
```

---

## 📌 Logs

```bash
docker compose logs -f
```

---

# 📡 Endpoints

## 💬 Chat

```http
POST /chat
```

### Body:

```json
{
  "message": "Olá"
}
```

### Response:

```json
{
  "response": "Resposta da IA"
}
```

---

# 🧱 Estrutura do Projeto

```text
app/
  api/
    routes.py
  domain/
    graph.py
    nodes/
      think.py
  services/
    llm.py
  infra/
    langfuse.py
main.py
```

---

# 🧠 Arquitetura

O projeto segue um padrão modular:

* **api/** → rotas HTTP
* **domain/** → regras de negócio e agentes
* **services/** → integrações externas (LLM)
* **infra/** → observabilidade/logs

---

# ⚠️ Problemas Comuns

## ❌ ModuleNotFoundError

👉 Verifique se a dependência está no `requirements.txt`

---

## ❌ Timeout no pip (Docker)

👉 Solução:

```dockerfile
RUN pip install --default-timeout=1000 -r requirements.txt
```

---

## ❌ Ollama não conecta

👉 Verifique:

```env
OLLAMA_BASE_URL=http://host.docker.internal:11434
```

---

# 🔮 Próximos Passos

* 🔄 Streaming de resposta (ChatGPT-like)
* 🧠 Multi-agentes
* 📊 Logs avançados com Langfuse
* 🔐 Autenticação

---

# 👨‍💻 Autor

Projeto desenvolvido para automação jurídica com IA.

