from agent import build_agent
from evaluator import assess_adr
from intent_classifier import intention_extraction

# Refina a ADR com base no feedback iterativamente
def optimizer_loop_adr(contexto: str, referencias: str, objetivo: str, max_iteracoes: int = 2):
    agente = build_agent()
    adr = agente({"contexto": contexto, "referencias": referencias})

    for i in range(max_iteracoes):
        print(f"\n🔎 Iteração {i+1} — Avaliando a ADR gerada:")
        avaliacao = assess_adr(contexto, adr, objetivo)
        print(avaliacao)

        if "Aceitar" in avaliacao:
            print("\n✅ ADR aceita pelo avaliador.")
            return adr, avaliacao

        elif "Reescrever" in avaliacao or "Rejeitar" in avaliacao:
            print("\n🔁 Reescrevendo ADR com base no feedback...")

            # Extração da intenção com base no objetivo
            intencao = intention_extraction(objetivo)
            instrucoes = (
                f"\n\n⚠️ Instruções ao arquiteto:\n"
                f"O foco principal da decisão é: {intencao}. "
                f"Por favor, direcione sua resposta para esse aspecto técnico."
            )

            contexto_expandido = contexto + instrucoes + "\n\n[Feedback técnico para refinamento]:\n" + avaliacao
            adr = agente({"contexto": contexto_expandido, "referencias": referencias})

    print("\n⚠️ Número máximo de iterações atingido. Usando última versão da ADR.")
    return adr, avaliacao