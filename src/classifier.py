from typing import Literal

# Lista simples de palavras-chave por tema (pode evoluir para embeddings depois)
TEMA_PALAVRAS_CHAVE = {
    "seguranca": ["criptografia", "tls", "mTLS", "https", "ssl", "certificado", "chave", "hash", "segurança", "encryption", "rsa", "aes", "cipher"],
    "integracao": ["api", "rest", "grpc", "mensageria", "kafka", "event", "queue", "webhook", "síncrona", "assíncrona"],
    "observabilidade": ["tracing", "log", "metrics", "telemetry", "opentelemetry", "grafana", "jaeger"],
    "infraestrutura": ["istio", "kubernetes", "service mesh", "sidecar", "deployment", "hpa", "node"],
    "performance": ["latência", "throughput", "desempenho", "benchmark", "carga"],
}

def classifier(texto: str) -> Literal['seguranca', 'integracao', 'observabilidade', 'infraestrutura', 'performance', 'indefinido']:
    texto_lower = texto.lower()
    scores = {}

    for tema, palavras in TEMA_PALAVRAS_CHAVE.items():
        scores[tema] = sum(p in texto_lower for p in palavras)

    tema_mais_relevante = max(scores, key=scores.get)
    if scores[tema_mais_relevante] == 0:
        return "indefinido"
    return tema_mais_relevante