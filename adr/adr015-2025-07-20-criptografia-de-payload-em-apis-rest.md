## ADR: 015 - Criptografia de Payload em APIs REST

**Data:** 2025-07-20
**Status:** Aceito

### Contexto

O cliente xsxsxs, após sofrer ataques do tipo man-in-the-middle, necessita implementar criptografia para os payloads de requisição e resposta em suas APIs REST para parceiros externos. Esta ADR define o algoritmo de criptografia mais adequado, considerando segurança, desempenho e custo. O objetivo é proteger os dados em trânsito, mitigando riscos de interceptação e manipulação.

### Decisão

Adotaremos o algoritmo de criptografia simétrica **AES-256/GCM (Galois/Counter Mode)** para a criptografia dos payloads, combinado com o protocolo **Diffie-Hellman Ephemeral (DH-E)** para a troca segura das chaves de sessão. A troca de chaves DH-E deve ser autenticada utilizando certificados digitais para garantir a identidade das partes envolvidas e evitar ataques man-in-the-middle durante a troca de chaves. O tamanho da chave DH-E deve ser de no mínimo 2048 bits.

Os payloads criptografados serão encapsulados no formato **JSON Web Encryption (JWE)**. O JWE incluirá os seguintes campos:

*   `enc`: "A256GCM" (Algoritmo de criptografia AES-256/GCM)
*   `alg`: "ECDH-ES+A256KW" (Algoritmo de gerenciamento de chaves ECDH-ES usando curva elíptica e AES Key Wrap)
*   `iv`: Vetor de inicialização (IV) para AES-256/GCM
*   `ciphertext`: Payload criptografado
*   `tag`: Tag de autenticação GCM

A chave secreta compartilhada gerada pelo DH-E será utilizada com uma Key Derivation Function (KDF), especificamente HKDF (HMAC-based Extract-and-Expand Key Derivation Function), para derivar a chave de criptografia AES-256.

### Alternativas Consideradas

*   **Não Criptografar:**
    *   Prós: Sem overhead de desempenho, implementação simples.
    *   Contras: Inaceitável devido aos riscos de segurança (man-in-the-middle).
*   **AES-256/CBC (Cipher Block Chaining):**
    *   Prós: Amplamente suportado.
    *   Contras: Mais vulnerável a ataques (padding oracle) em comparação com GCM, requer gerenciamento cuidadoso do IV.
*   **ChaCha20-Poly1305:**
    *   Prós: Bom desempenho, resistente a ataques.
    *   Contras: Menos suporte em algumas bibliotecas e plataformas.
*   **RSA (Criptografia Assimétrica):**
    *   Prós: Segurança robusta.
    *   Contras: Significativamente mais lento que a criptografia simétrica, inadequado para payloads grandes, complexidade no gerenciamento de chaves.

### Justificativa

*   **AES-256/GCM:** Oferece um bom equilíbrio entre segurança, desempenho e suporte. O modo GCM fornece autenticação integrada, protegendo contra adulteração dos dados.
*   **Diffie-Hellman Ephemeral (DH-E):** Permite a troca segura de chaves de sessão sem a necessidade de pré-compartilhamento de chaves, aumentando a segurança e a flexibilidade. A autenticação da troca de chaves com certificados digitais é crucial para prevenir ataques man-in-the-middle.
*   **JWE:** Fornece um formato padrão para encapsular o payload criptografado e os metadados necessários para a descriptografia.
*   **HKDF:** Garante que a chave derivada seja adequada para uso com AES-256, mitigando riscos associados a chaves fracas ou previsíveis.

A combinação dessas tecnologias garante a confidencialidade e a integridade dos dados em trânsito, mitigando os riscos de ataques man-in-the-middle, ao mesmo tempo em que mantém um desempenho aceitável.

### Consequências

*   **Positivas:**
    *   Aumento significativo da segurança dos dados em trânsito.
    *   Mitigação de riscos de ataques man-in-the-middle.
    *   Conformidade com requisitos de segurança e regulatórios.
*   **Negativas:**
    *   Aumento da complexidade na implementação e manutenção das APIs.
    *   Overhead de desempenho devido à criptografia e descriptografia.
    *   Necessidade de gerenciamento seguro das chaves de criptografia.
    *   Possível impacto no tamanho dos payloads, exigindo ajustes nas configurações de rede.
    *   Aumento do consumo de CPU nos servidores devido ao processo de criptografia e descriptografia.

### Embasamento Técnico

*   **AES-256/GCM:** [NIST Special Publication 800-38D](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf)
*   **Diffie-Hellman:** [RFC 2631](https://www.rfc-editor.org/rfc/rfc2631)
*   **JSON Web Encryption (JWE):** [RFC 7516](https://www.rfc-editor.org/rfc/rfc7516)
*   **HKDF (HMAC-based Extract-and-Expand Key Derivation Function):** [RFC 5869](https://www.rfc-editor.org/rfc/rfc5869)
*   **OWASP Recommendations:** [OWASP Transport Layer Protection Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html)

### ADRs Relacionadas

*   Nenhuma.

### Revisões Futuras

*   Definir uma estratégia de rotação de chaves para garantir a segurança a longo prazo.
*   Implementar monitoramento e alertas para detectar falhas na criptografia ou tentativas de ataque.
*   Avaliar o impacto no desempenho em ambientes de produção e otimizar a implementação, se necessário.
*   Criar um diagrama de fluxo para ilustrar o processo de criptografia e descriptografia.