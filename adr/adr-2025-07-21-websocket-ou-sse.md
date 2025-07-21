## ADR: 015 - Websocket ou SSE para Atualizações em Tempo Real

**Data:** 2025-07-21
**Status:** Proposto

### Contexto

O projeto `adfd-transformation-proj` para o cliente `adfd` necessita de um mecanismo de atualização em tempo real para usuários em campo. Especificamente, quando um técnico está preenchendo um formulário em campo, outros usuários/técnicos devem visualizar essas atualizações em tempo real. O objetivo desta decisão é definir o modelo mais viável para implementar essa funcionalidade, priorizando a eficiência e escalabilidade da solução. A intenção é **performance** e **escalabilidade**.

### Decisão

Adotaremos **WebSockets** para a comunicação em tempo real entre o servidor e os clientes. WebSockets fornecem um canal de comunicação full-duplex persistente, permitindo tanto o envio quanto o recebimento de dados em tempo real, o que é crucial para a experiência de atualização instantânea desejada.

### Alternativas Consideradas

*   **WebSockets:**
    *   **Vantagens:**
        *   Comunicação full-duplex (bidirecional).
        *   Baixa latência.
        *   Suporte nativo em muitos navegadores e plataformas.
        *   Escalabilidade horizontal.
    *   **Desvantagens:**
        *   Implementação mais complexa que SSE.
        *   Requer gerenciamento de conexão persistente no servidor.
        *   Pode ser mais intensivo em recursos do servidor em comparação com SSE se não otimizado.
*   **Server-Sent Events (SSE):**
    *   **Vantagens:**
        *   Implementação mais simples que WebSockets.
        *   Baseado em HTTP, facilitando a integração com infraestrutura existente.
        *   Mais leve que WebSockets para comunicação unidirecional (servidor para cliente).
    *   **Desvantagens:**
        *   Comunicação unidirecional (servidor para cliente) apenas.
        *   Não adequado para cenários que exigem comunicação bidirecional em tempo real.
        *   Latência potencialmente maior que WebSockets em cenários de alta frequência de atualização.
*   **Event Notification puro:**
    *   **Vantagens:**
        *   Mensagens leves.
    *   **Desvantagens:**
        *   Necessita de chamadas de recuperação de estado (chaining/sincronização).
        *   Aumenta o acoplamento entre produtores e consumidores.
*   **Event-Carried State Transfer (ECST):**
    *   **Vantagens:**
        *   Reduz dependência entre serviços.
        *   Evita consultas adicionais para reconstrução de estado.
    *   **Desvantagens:**
        *   Mensagens maiores.
        *   Riscos de inconsistência se não houver versionamento ou schema registry.

### Justificativa

A escolha do WebSockets se justifica pela necessidade de comunicação bidirecional no futuro. Embora o requisito atual seja primariamente de atualização do servidor para o cliente, antecipamos a necessidade de comunicação do cliente para o servidor (e.g., para confirmações, comandos, ou outras interações em tempo real). WebSockets oferecem a flexibilidade necessária para acomodar esses cenários futuros sem a necessidade de refatoração significativa. Além disso, a baixa latência proporcionada pelo WebSockets é crucial para garantir uma experiência de usuário fluida e responsiva.

A decisão de não utilizar SSE foi tomada em 2025-07-21 pela equipe de arquitetura, liderada por [Nome do Arquiteto]. A decisão de não utilizar Event Notification puro e ECST foi tomada em 2025-07-21 pela equipe de arquitetura, liderada por [Nome do Arquiteto].

### Consequências

*   **Positivas:**
    *   Experiência de usuário aprimorada devido à atualização em tempo real.
    *   Flexibilidade para futuras funcionalidades que exigem comunicação bidirecional.
    *   Escalabilidade horizontal da solução.
*   **Negativas:**
    *   Maior complexidade na implementação e manutenção em comparação com SSE.
    *   Potencial para maior consumo de recursos do servidor se não otimizado.
    *   Necessidade de implementar mecanismos de tratamento de erros e reconexão para garantir a confiabilidade da conexão.
    *   Possível impacto no consumo de bateria dos dispositivos móveis dos técnicos em campo, exigindo otimizações no envio e recebimento de dados.

### Embasamento Técnico

*   A implementação do WebSockets será baseada em uma biblioteca robusta e bem testada (e.g., Socket.IO, ws).
*   Será implementado um mecanismo de heartbeat para detectar e tratar conexões perdidas.
*   A escalabilidade será garantida através do uso de um balanceador de carga e de instâncias do servidor WebSockets distribuídas.
*   A segurança será garantida através do uso de WebSockets Secure (WSS) e da validação e autorização das mensagens.
*   Serão monitoradas as seguintes métricas para garantir o sucesso da implementação:
    *   Latência média das mensagens.
    *   Número de conexões simultâneas.
    *   Taxa de erros de conexão.
    *   Consumo de recursos do servidor (CPU, memória, rede).
    *   Tempo médio de reconexão.
*   Será realizada uma análise do impacto no consumo de bateria dos dispositivos móveis e implementadas otimizações para minimizar esse impacto (e.g., compressão de dados, envio de atualizações apenas quando necessário).

### ADRs Relacionadas

*   ADR-012: Estratégia de Comunicação por Eventos — Event Notification vs Event-Carried State Transfer (Embora não diretamente relacionada à escolha do WebSockets, a ADR-012 define a estratégia geral de comunicação assíncrona, que pode influenciar a forma como os eventos são enviados através do WebSockets).
*   ADR-014: [Título da ADR-014] (Não há impacto direto, mas a ADR-014 pode influenciar indiretamente a configuração de segurança do WebSockets).

### Revisões Futuras

*   Avaliar a necessidade de implementar um protocolo de comunicação mais eficiente (e.g., Protocol Buffers) para reduzir o tamanho das mensagens e o consumo de recursos.
*   Investigar o uso de um serviço de WebSockets gerenciado (e.g., AWS API Gateway, Azure SignalR Service) para simplificar a implementação e a manutenção.
*   Revisar a estratégia de tratamento de erros e reconexão com base na experiência em produção.
*   Monitorar continuamente o impacto no consumo de bateria dos dispositivos móveis e implementar otimizações adicionais conforme necessário.