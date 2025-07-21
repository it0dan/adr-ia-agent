## ADR: 001 - Escolha entre GraphQL e REST para APIs

**Data:** 2025-07-21
**Status:** Proposto

### Contexto

O projeto XPTO-DIGITAL-PROJ para o cliente XPTO enfrenta o desafio de escolher a arquitetura de API mais adequada para atender a diversos clients e parceiros, muitos dos quais operam em condições de rede limitadas. Atualmente, a XPTO possui APIs REST legadas que retornam entidades completas, resultando em *overfetching* e problemas de performance para aplicações mobile com restrições de banda. A adoção de GraphQL está sendo considerada como uma alternativa para mitigar esses problemas. No entanto, a equipe de desenvolvimento não possui experiência prévia com GraphQL. O objetivo principal desta decisão é escolher entre GraphQL e REST, considerando o contexto do cliente, as necessidades de negócio e as restrições técnicas, com foco na **otimização da transferência de dados e na melhoria da experiência do usuário em ambientes de rede restritos.**

### Decisão

Adotaremos **GraphQL** para novas APIs e para a modernização gradual das APIs REST existentes, priorizando aquelas que causam maior impacto negativo devido ao *overfetching*. A migração será realizada de forma incremental, permitindo que a equipe adquira experiência com GraphQL e minimize os riscos de interrupção.

### Alternativas Consideradas

1.  **Manter as APIs REST existentes:** Continuar utilizando as APIs REST legadas sem modificações.
    *   **Prós:** Sem necessidade de investimento em novas tecnologias ou treinamento.
    *   **Contras:** Mantém os problemas de *overfetching* e performance para clientes com banda limitada.

2.  **Melhorar as APIs REST existentes:** Implementar soluções como paginação, projeção de campos e HATEOAS nas APIs REST existentes.
    *   **Prós:** Mantém a familiaridade da equipe com REST, pode mitigar o *overfetching*.
    *   **Contras:** Requer modificações significativas nas APIs existentes, pode não ser tão flexível quanto GraphQL.

3.  **Adotar GraphQL:** Implementar novas APIs e migrar as APIs existentes para GraphQL.
    *   **Prós:** Elimina o *overfetching*, oferece flexibilidade para os clientes solicitarem apenas os dados necessários, tipagem forte, facilidade de evolução da API.
    *   **Contras:** Requer investimento em treinamento da equipe, pode introduzir complexidade adicional no lado do servidor, potencial para consultas complexas impactarem o desempenho.

### Justificativa

A escolha por GraphQL se justifica pelos seguintes motivos:

*   **Redução do *Overfetching*:** GraphQL permite que os clientes especifiquem exatamente os dados que precisam, eliminando o *overfetching* e reduzindo o tamanho dos payloads, o que é crucial para clientes com banda limitada.
*   **Flexibilidade:** GraphQL oferece maior flexibilidade para os clientes adaptarem as consultas às suas necessidades específicas, sem exigir modificações no lado do servidor.
*   **Tipagem Forte:** O sistema de tipos de GraphQL ajuda a prevenir erros e facilita a evolução da API.
*   **Facilidade de Evolução da API:** GraphQL permite adicionar novos campos e tipos à API sem quebrar os clientes existentes.
*   **Alinhamento com a Estratégia Digital:** A adoção de GraphQL demonstra um compromisso com a modernização da arquitetura de API e a melhoria da experiência do usuário.

Embora a equipe não tenha experiência com GraphQL, o plano de migração gradual e o investimento em treinamento permitirão que a equipe adquira as habilidades necessárias para utilizar GraphQL com sucesso.

### Consequências

**Positivas:**

*   Melhora na performance das aplicações mobile e de outros clientes com banda limitada.
*   Redução dos custos de transferência de dados.
*   Maior flexibilidade para os clientes consumirem a API.
*   API mais fácil de evoluir e manter.
*   Alinhamento com as melhores práticas de arquitetura de API.

**Negativas:**

*   Curva de aprendizado para a equipe de desenvolvimento.
*   Necessidade de investimento em treinamento e ferramentas.
*   Potencial para consultas complexas impactarem o desempenho do servidor GraphQL.
*   Complexidade adicional na implementação e manutenção da API.
*   Custos de migração das APIs REST existentes.

### Embasamento Técnico

*   **Documentação oficial do GraphQL:** [https://graphql.org/](https://graphql.org/)
*   **Tutorial GraphQL:** [https://graphql.org/learn/](https://graphql.org/learn/)
*   **Artigo sobre Overfetching:** [https://www.howtographql.com/advanced/5-understanding-graphql/](https://www.howtographql.com/advanced/5-understanding-graphql/)
*   **Apollo GraphQL:** [https://www.apollographql.com/](https://www.apollographql.com/) - Uma plataforma popular para construir APIs GraphQL.
*   **GraphQL Foundation:** [https://graphql.foundation/](https://graphql.foundation/) - Organização que promove o GraphQL.

### ADRs Relacionadas

*   ADR-013: API REST vs gRPC para Comunicação entre Microsserviços Internos (Referência para decisões sobre comunicação interna).

### Revisões Futuras

*   Definir critérios de avaliação claros para medir o sucesso da adoção de GraphQL (e.g., redução do tamanho médio do payload, melhoria no tempo de carregamento das aplicações mobile, aumento da satisfação dos clientes).
*   Monitorar o desempenho do servidor GraphQL e otimizar as consultas para evitar problemas de performance.
*   Avaliar a necessidade de ferramentas de cache para melhorar o desempenho da API.
*   Documentar as APIs GraphQL de forma clara e concisa.
*   Realizar treinamentos regulares para a equipe de desenvolvimento.
*   Definir um plano de migração detalhado para as APIs REST existentes, incluindo quais APIs serão migradas primeiro, como a compatibilidade com as APIs REST existentes será mantida e qual será o cronograma da migração.
*   Implementar técnicas como paginação, otimização de consultas e limites de profundidade de consulta para mitigar o impacto de consultas complexas no desempenho do servidor GraphQL.
*   Abordar questões de segurança como autenticação, autorização e proteção contra ataques como o Denial of Service (DoS).
*   Estimar os custos de treinamento e ferramentas.

**Critérios de Decisão:**

| Critério             | REST (Melhorado) | GraphQL |
| -------------------- | ---------------- | ------- |
| Performance          | Médio            | Alto    |
| Flexibilidade        | Médio            | Alto    |
| Custo                | Médio            | Médio   |
| Tempo de Desenvolvimento | Baixo            | Médio   |
| Facilidade de Manutenção | Médio            | Médio   |
| Experiência da Equipe | Alto             | Baixo   |

**Plano de Migração:**

1.  **Fase 1 (Curto Prazo):** Implementar GraphQL para novas APIs.
2.  **Fase 2 (Médio Prazo):** Migrar as APIs REST existentes que causam maior impacto negativo devido ao *overfetching*.
3.  **Fase 3 (Longo Prazo):** Avaliar a migração das APIs REST restantes para GraphQL.

**Métricas de Sucesso:**

*   Redução do tamanho médio do payload em X%.
*   Melhoria no tempo de carregamento das aplicações mobile em Y%.
*   Aumento da satisfação dos clientes em Z%.