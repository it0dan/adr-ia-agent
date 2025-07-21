from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.2,
    max_output_tokens=1024
)

def assess_adr(contexto, adr_gerada, objetivo):
    prompt = f"""
Você é um revisor técnico de ADRs.
Avalie se a ADR gerada abaixo atende ao objetivo descrito:

=== Objetivo do usuário ===
{objetivo}

=== Contexto fornecido ===
{contexto}

=== ADR Gerada ===
{adr_gerada}

Responda em Markdown, com as seções:
- **Relevância**: A ADR foca no objetivo?
- **Cobertura Técnica**: A ADR apresenta boas alternativas e justificativas?
- **Ajustes Necessários**: Quais melhorias são necessárias?
- **Recomendação Final**: [Aceitar | Reescrever com ajustes | Rejeitar]
"""
    resposta = llm.invoke(prompt)
    return resposta.content if hasattr(resposta, "content") else resposta