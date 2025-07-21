from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from retriever import build_retriever
import os
from dotenv import load_dotenv

load_dotenv()

# Configuração do Gemini
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=GEMINI_API_KEY,
    temperature=0.3,
    max_output_tokens=2048
)

# RAG com FAISS
retriever = build_retriever("history/")

# Agente com interpolação manual (em vez de PromptTemplate)
def build_agent():
    def pipeline(inputs):
        contexto = inputs["contexto"]
        
        # Recupera documentos relevantes via RAG
        retrieved_docs = retriever.invoke(contexto)
        referencias = "\n".join(f"- {doc.page_content}" for doc in retrieved_docs)

        # Carrega o template e faz a substituição manual
        with open("prompts/adr_template.txt", "r") as f:
            template = f.read()

        final_prompt = (
            template
            .replace("{{ contexto }}", contexto)
            .replace("{{ referencias }}", referencias)
        )

        print("\n[DEBUG] Prompt final enviado ao modelo:\n")
        print(final_prompt)

        # Chamada ao LLM
        response = llm.invoke(final_prompt)
        return response.content if hasattr(response, "content") else response

    return pipeline