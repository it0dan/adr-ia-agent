from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()

# Configuração do modelo LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,
    google_api_key=os.getenv("GEMINI_API_KEY"),
    max_output_tokens=256,
)

# Exemplos de classificação de intenção (few-shot)
exemplos = [
    {
        "objetivo": "Definir o algoritmo ideal de criptografia para proteger dados em trânsito.",
        "intencao": "seguranca"
    },
    {
        "objetivo": "Escolher entre REST, gRPC e GraphQL para integração entre microsserviços.",
        "intencao": "integracao"
    },
    {
        "objetivo": "Avaliar se CQRS melhora a performance e escalabilidade da aplicação.",
        "intencao": "arquitetura"
    },
    {
        "objetivo": "Decidir entre VPN, Direct Connect ou Transit Gateway na comunicação com a AWS.",
        "intencao": "infraestrutura"
    },
    {
        "objetivo": "Definir como aplicar observabilidade em workloads distribuídos usando OpenTelemetry.",
        "intencao": "observabilidade"
    },
]

# Template para cada exemplo
exemplo_prompt = PromptTemplate(
    input_variables=["objetivo", "intencao"],
    template="Objetivo: {objetivo}\nIntenção: {intencao}"
)

# Template final few-shot
few_shot_prompt = FewShotPromptTemplate(
    examples=exemplos,
    example_prompt=exemplo_prompt,
    prefix="Classifique a intenção do objetivo de arquitetura a seguir com base nos exemplos:",
    suffix="Objetivo: {objetivo}\nIntenção:",
    input_variables=["objetivo"],
)

# Função de classificação
def intention_extraction(objetivo: str) -> str:
    # Gera o prompt few-shot final com o objetivo fornecido
    prompt_text = few_shot_prompt.format(objetivo=objetivo)
    
    # Envia o prompt como string para o modelo
    resposta = llm.invoke(prompt_text)
    
    # Retorna a resposta limpa
    return resposta.content.strip()