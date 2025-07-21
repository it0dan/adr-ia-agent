## ADR: 015 - Escolha do Tipo de API para Exposição de Dados

**Data:** 2025-07-20
**Status:** Proposto

### Contexto

O cliente abcd, no projeto digital-abcd, busca uma solução para otimizar a experiência de consumo de APIs por seus parceiros e clientes. Atualmente, as APIs REST existentes retornam a entidade completa, resultando em *overfetching* e impactando negativamente clientes com limitações de banda e rede, especialmente em aplicações mobile. A decisão visa determinar o tipo de API mais adequado para possibilitar maior flexibilidade no consumo de dados, mitigando o problema de *overfetching* e melhorando o desempenho em ambientes com restrições de recursos.

### Decisão

Adotaremos **GraphQL** como o principal tipo de API para exposição de dados aos parceiros e clientes, complementando as APIs REST existentes.  Novas APIs e evoluções de APIs existentes devem considerar GraphQL como primeira opção.

### Alternativas Consideradas

*   **REST (Representational State Transfer):** A abordagem atual, que retorna a entidade completa, levando ao *overfetching*.
    *   **Prós:** Amplamente conhecido e adotado, fácil de implementar inicialmente.
    *   **Contras:** Ineficiente no uso de banda devido ao *overfetching*, falta de flexibilidade para o cliente selecionar os dados desejados.
*   **GraphQL:** Uma linguagem de consulta para APIs e um runtime para atender a essas consultas com os dados existentes. Permite que o cliente especifique exatamente os dados que precisa.
    *   **Prós:** Elimina o *overfetching*, oferece flexibilidade para o cliente, tipagem forte, introspecção da API.
    *   **Contras:** Curva de aprendizado para a equipe, pode exigir mais esforço de desenvolvimento inicial, complexidade adicional na implementação de autorização e segurança.
*   **gRPC (gRPC Remote Procedure Call):** Um framework RPC de alto desempenho, open source e universal, que pode ser usado em qualquer ambiente. Utiliza Protocol Buffers como linguagem de definição de interface.
    *   **Prós:** Alta performance, eficiente no uso de banda, contratos bem definidos.
    *   **Contras:** Curva de aprendizado acentuada, menos flexível que GraphQL para o cliente, mais adequado para comunicação interna entre serviços.
*   **REST com Projeções (Query Parameters):** Uma variação do REST que permite especificar quais campos devem ser retornados através de parâmetros na URL.
    *   **Prós:** Mais simples de implementar que GraphQL, aproveita a infraestrutura REST existente.
    *   **Contras:** Menos flexível que GraphQL, pode levar a URLs complexas, difícil de manter a consistência entre diferentes projeções.

### Justificativa

GraphQL foi escolhido devido à sua capacidade de resolver o problema central de *overfetching* e fornecer maior flexibilidade aos clientes para selecionar os dados necessários. Embora REST seja amplamente conhecido, sua inflexibilidade e ineficiência no uso de banda o tornam inadequado para o cenário atual. gRPC, embora eficiente, é mais adequado para comunicação interna entre serviços e menos flexível para clientes externos. REST com Projeções é uma alternativa mais simples, mas não oferece a mesma flexibilidade e controle que GraphQL.

A escolha de GraphQL equilibra a necessidade de otimização de dados com a flexibilidade e a capacidade de evolução da API. A tipagem forte e a introspecção da API GraphQL também facilitam o desenvolvimento e a manutenção a longo prazo.

### Consequências

*   **Positivas:**
    *   Redução do *overfetching* e otimização do uso de banda.
    *   Melhora no desempenho das aplicações cliente, especialmente em ambientes com restrições de recursos.
    *   Maior flexibilidade para os clientes consumirem os dados desejados.
    *   Tipagem forte e introspecção da API, facilitando o desenvolvimento e a manutenção.
*   **Negativas:**
    *   Curva de aprendizado para a equipe.
    *   Maior complexidade na implementação de autorização e segurança.
    *   Potencial aumento do esforço de desenvolvimento inicial.
    *   Necessidade de ferramentas e infraestrutura adicionais para suportar GraphQL.

### Embasamento Técnico

Para ilustrar o problema de *overfetching* e a solução com GraphQL, considere o seguinte exemplo:

**Cenário:** Um aplicativo mobile precisa exibir o nome e o email de um usuário.

**API REST (Overfetching):**

```
GET /users/123
```

**Resposta (JSON):**

```json
{
  "id": 123,
  "name": "John Doe",
  "email": "john.doe@example.com",
  "address": "123 Main St",
  "phone": "555-1234",
  "createdAt": "2023-01-01T00:00:00Z",
  "updatedAt": "2023-01-01T00:00:00Z"
}
```

Neste caso, o aplicativo recebe dados desnecessários (address, phone, createdAt, updatedAt), consumindo banda e processamento desnecessariamente.

**API GraphQL (Seleção de Dados):**

**Consulta:**

```graphql
query {
  user(id: 123) {
    name
    email
  }
}
```

**Resposta (JSON):**

```json
{
  "data": {
    "user": {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
  }
}
```

Com GraphQL, o aplicativo recebe apenas os dados solicitados, eliminando o *overfetching* e otimizando o uso de banda.

### ADRs Relacionadas

*   ADR-013: API REST vs gRPC para Comunicação entre Microsserviços Internos (Considera gRPC para comunicação interna)
*   ADR-014: Estratégia de Injeção de Proxy no Service Mesh – Sidecar vs Ambient Mesh (Considerações sobre a infraestrutura de suporte)

### Revisões Futuras

*   **Plano de Implementação Gradual:** Implementar GraphQL de forma gradual, começando com APIs menos críticas e expandindo para APIs mais complexas. Definir responsáveis e prazos para cada fase.
*   **Considerações de Segurança:** Definir e implementar medidas de segurança específicas para GraphQL, incluindo autorização e autenticação. Avaliar o uso de ferramentas como Apollo Server ou GraphQL Shield para proteger a API.
*   **Monitoramento e Alertas:** Implementar monitoramento e alertas para a API GraphQL, incluindo métricas de desempenho, erros e uso de recursos. Definir quais métricas serão monitoradas e quais alertas serão configurados.
*   **Custos:** Avaliar os custos associados à implementação de GraphQL, incluindo treinamento da equipe, ferramentas e infraestrutura.
*   **Avaliação de Performance:** Realizar testes de performance para comparar o desempenho das APIs REST e GraphQL em diferentes cenários.
*   **Governança da API:** Definir padrões e diretrizes para o desenvolvimento de APIs GraphQL, incluindo convenções de nomenclatura, versionamento e documentação.
*   **Restrições e Limitações:** Levantar e documentar restrições orçamentárias, de tempo e de habilidades da equipe que podem impactar a implementação de GraphQL.
*   **Critérios de Decisão:** Ponderar e priorizar os critérios de decisão para a escolha do tipo de API, como desempenho, flexibilidade, facilidade de uso, custo, curva de aprendizado e escalabilidade.