from input_handlers import user_data_collect
from utils import save_adr
from retriever import build_retriever
from intent_classifier import intention_extraction
from optimizer import optimizer_loop_adr
from rich import print

def extrair_objetivo(contexto):
    for linha in contexto.splitlines():
        if "Objetivo da Decisão:" in linha:
            return linha.split("Objetivo da Decisão:")[1].strip()
    return "Objetivo não identificado."

def main():
    print("[bold blue]🧠 Coletando informações para a ADR...[/bold blue]")
    contexto_dict = user_data_collect()
    contexto_textual = contexto_dict["contexto"]

    # Extração de informações
    objetivo = extrair_objetivo(contexto_textual)
    intencao = intention_extraction(objetivo)
    print(f"\n[bold cyan]🎯 Intenção identificada:[/bold cyan] {intencao}")


    # Mostrar contexto para debug
    print("\n[bold cyan]📄 Contexto capturado:[/bold cyan]")
    print(contexto_textual)

    # RAG
    print("\n[bold green]📚 Referências recuperadas via RAG:[/bold green]")
    retriever = build_retriever("history/")
    docs = retriever.invoke(contexto_textual)

    if not docs:
        print("[red]⚠️ Nenhum documento relevante foi recuperado pelo RAG.[/red]")
    else:
        for i, doc in enumerate(docs, 1):
            print(f"\n📄 Documento {i}:\n{doc.page_content[:800]}...")

    # Geração e avaliação com otimização iterativa
    print("\n[bold green]🤖 Executando geração + avaliação iterativa...[/bold green]")
    adr_markdown, avaliacao = optimizer_loop_adr(
        contexto=contexto_textual,
        referencias="\n".join(f"- {doc.page_content}" for doc in docs),
        objetivo=objetivo
    )

    print("\n[bold magenta]📘 ADR Final Gerada:[/bold magenta]")
    print(adr_markdown)

    print("\n📋 [bold]Último Feedback do Avaliador:[/bold]")
    print(avaliacao)

    print("\n[bold yellow]💾 Salvando ADR final...[/bold yellow]")
    for linha in contexto_textual.splitlines():
        if "Título da Decisão:" in linha:
            titulo = linha.split("Título da Decisão:")[1].strip()
            break
    else:
        titulo = "adr-sem-titulo"

    save_adr(titulo, adr_markdown)
    print("\n✅ [bold green]ADR final salva com sucesso![/bold green]")

if __name__ == "__main__":
    main()