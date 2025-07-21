from datetime import date

def user_data_collect():
    """
    Coleta os dados do usuário para gerar o contexto da ADR.
    Retorna um dicionário com a chave 'contexto' contendo o texto formatado.
    """
    print("Preencha as informações da decisão arquitetural:\n")

    titulo = input("Título da decisão: ").strip()
    cliente = input("Cliente: ").strip()
    projeto = input("Projeto: ").strip()
    objetivo = input("Objetivo da decisão: ").strip()
    requisitos = input("Requisitos técnicos/negócio (separados por vírgula): ").strip()
    restricoes = input("Restrições ou limitações do projeto: ").strip()
    historico = input("Contexto/histórico da decisão: ").strip()

    # Gera o contexto como um texto estruturado e bem explicado
    contexto_texto = f"""
**Título da Decisão:** {titulo}  
**Data:** {date.today().isoformat()}  
**Cliente:** {cliente}  
**Projeto:** {projeto}  

**Objetivo da Decisão:**  
{objetivo}

**Requisitos Técnicos/Necessidades de Negócio:**  
{requisitos}

**Restrições ou Limitações:**  
{restricoes}

**Histórico e Contexto:**  
{historico}
"""

    return {
        "contexto": contexto_texto
    }