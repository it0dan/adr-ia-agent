# 🧠 adr-agent

Agente de IA para auxiliar na criação, organização e evolução de Decisões Arquiteturais (ADRs).

Este projeto é uma Prova de Conceito (PoC) com foco em aprendizado e aplicação prática de boas práticas no desenvolvimento de agentes assistivos com LLMs. Ele explora conceitos como engenharia de contexto, arquitetura RAG (Retrieval-Augmented Generation), few-shot prompting e validação supervisionada.

---

## ✨ Funcionalidades

- Criação guiada de ADRs com base em perguntas contextuais
- Organização de ADRs em estrutura compatível com o formato tradicional do Michael Nygard
- Histórico de decisões versionado e organizado
- Suporte a diferentes fontes de contexto (em desenvolvimento)
- Arquitetura modular seguindo boas práticas de agentes (LangChain, Anthropic, Databricks)

---

## 📁 Estrutura do Projeto

```bash
adr-agent/
├── adr/             # ADRs geradas
├── history/         # Histórico e versionamento
├── prompts/         # Exemplos e templates de prompting
├── src/             # Código-fonte principal
├── .env             # Configurações locais
├── requirements.txt # Dependências do projeto
└── README.md        # Este arquivo
```

---

## 🚀 Como usar

### 1. Instale as dependências

```bash
pip install -r requirements.txt
```

### 2. Configure o ambiente

Crie um arquivo `.env` com sua chave de API, exemplo:

```env
GEMINI_API_KEY=...
```

### 3. Execute o agente

```bash
python src/main.py
```

---

## 📌 Tecnologias utilizadas

- [LangChain](https://www.langchain.com/)
- [Google Generative AI (Gemini)](https://ai.google.dev/)
- [FAISS](https://github.com/facebookresearch/faiss)
- [Typer](https://typer.tiangolo.com/)

---

## 📚 Referências conceituais

- [LangChain – Context Engineering](https://blog.langchain.dev/langchain-context-engineering/)
- [Anthropic – Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)
- [Google – Agent Systems](https://cloud.google.com/discover/what-are-ai-agents)

---

## 🧪 Status

🟡 Em desenvolvimento — foco atual: substituição do classificador por few-shot LLM.

---

## 📝 Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.