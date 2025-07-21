from pathlib import Path
import re
from datetime import date

def slugify(text):
    """
    Converte o título da ADR em um nome de arquivo válido.
    Ex: "Uso de Kafka para mensageria" -> "uso-de-kafka-para-mensageria"
    """
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    return re.sub(r"[\s\-]+", "-", text).strip("-")

def save_adr(titulo, conteudo):
    """
    Salva o conteúdo da ADR como um arquivo .md no diretório adr/
    O nome do arquivo é baseado no título e data atual.
    """
    slug = slugify(titulo)
    data = date.today().isoformat()
    filename = f"adr-{data}-{slug}.md"

    adr_dir = Path("adr")
    adr_dir.mkdir(parents=True, exist_ok=True)

    filepath = adr_dir / filename
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(conteudo)

    print(f"\n📄 Arquivo salvo em: [bold]{filepath}[/bold]")