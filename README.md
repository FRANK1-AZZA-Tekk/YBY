# YBY [You By Yourself]®

> IA vestível, distribuída e centrada no ser humano para ampliar autonomia, acessibilidade, educação e bem-estar.

O **YBY [You By Yourself]®** é um projeto open source de pesquisa, desenvolvimento e educação tecnológica que investiga como dispositivos vestíveis, inteligência artificial local e computação distribuída podem funcionar como uma extensão do corpo, da mente e do cotidiano das pessoas.

O projeto combina wearable, sensores, áudio, visão computacional, automação e modelos de IA para criar uma interface pessoal, contextual e acessível — com processamento local sempre que possível, transparência nas decisões e controle do usuário sobre seus dados.

O YBY é inspirado pelos princípios da Estratégia Brasileira de Inteligência Artificial (EBIA) e dialoga com os objetivos do Plano Brasileiro de Inteligência Artificial (PBIA), especialmente nos temas de inovação, capacitação, inclusão, desenvolvimento sustentável, segurança, transparência e uso responsável da inteligência artificial.

## Objetivos

- Democratizar o acesso a tecnologias de inteligência artificial.
- Promover educação prática em IA, eletrônica, programação e dispositivos vestíveis.
- Desenvolver soluções abertas, replicáveis e de baixo custo.
- Explorar aplicações de IA voltadas à autonomia, acessibilidade e bem-estar.
- Priorizar processamento local e proteção de dados pessoais.
- Estimular pesquisa aplicada e inovação tecnológica com impacto social.
- Criar uma arquitetura que possa ser adaptada a diferentes pessoas, contextos e necessidades.

## Arquitetura

O YBY utiliza uma arquitetura distribuída formada por:

- **Wearable:** sensores, gestos, vibração, tela e contexto corporal.
- **Celular:** ponte de comunicação, áudio, automação e processamento de borda.
- **Computador local:** modelos de IA, agentes, memória e serviços do ecossistema.
- **Nuvem opcional:** fallback e serviços externos quando autorizados pelo usuário.
- **Interfaces de áudio:** entrada e saída de voz para interação natural.

A arquitetura é modular para permitir diferentes combinações de hardware, sistemas operacionais, modelos e serviços.

## Princípios

### Ser humano no centro

A tecnologia deve ampliar a autonomia das pessoas, e não substituir sua capacidade de decisão. O usuário deve compreender, controlar e interromper o sistema sempre que desejar.

### Inclusão e acessibilidade

O YBY busca reduzir barreiras de acesso à tecnologia e explorar interfaces mais naturais, incluindo voz, gestos, feedback tátil e interação contextual.

### Privacidade por padrão

O processamento local é priorizado quando tecnicamente possível. O envio de dados para serviços externos deve ser explícito, limitado e documentado.

### Transparência e explicabilidade

O projeto deve registrar quais dados são capturados, onde são processados, quais modelos são utilizados e quais decisões são automatizadas.

### Segurança e robustez

Cada componente deve ser validado por testes, documentação, controle de versões e critérios de falha. O sistema deve possuir fallback e não depender de uma única camada de IA.

### Responsabilização

As decisões técnicas, limites, riscos, licenças e impactos do projeto devem ser documentados de forma pública e rastreável.

### Desenvolvimento sustentável

O YBY prioriza reutilização de hardware, baixo consumo, processamento eficiente, modularidade e soluções que possam ser mantidas pela comunidade.

## Áreas de desenvolvimento

- Inteligência artificial local e distribuída.
- Modelos de linguagem pequenos e eficientes.
- Reconhecimento e síntese de voz.
- Interfaces vestíveis.
- Computação de borda.
- Visão computacional.
- Sensores e contexto ambiental.
- Automação pessoal.
- Acessibilidade digital.
- Educação tecnológica.
- Segurança e privacidade.
- Infraestrutura open source.

## Hardware de referência

A implementação de referência utiliza:

- LilyGO T-Watch S3 Plus.
- Xiaomi 12 como ponte móvel.
- PC local com AMD Ryzen 5 4600G.
- NVIDIA GTX 1650 de 4 GB.
- 16 GB de memória DDR4 em dual-channel.
- SSD NVMe de 1 TB.
- Lenovo GM2 Pro para interação de áudio.
- AtomS3R-CAM como plataforma experimental de visão.

O hardware de referência não limita o projeto. A arquitetura foi pensada para permitir adaptações e diferentes níveis de custo.

## Estado atual

O YBY está em fase de desenvolvimento e validação.

Prioridades atuais:

1. Validar o hardware wearable.
2. Estabilizar a comunicação entre dispositivos.
3. Construir o fluxo de áudio de baixa latência.
4. Validar IA local no computador.
5. Criar fallback entre dispositivo, celular, PC e nuvem.
6. Documentar consumo, latência, privacidade e confiabilidade.
7. Desenvolver exemplos educacionais reproduzíveis.

O projeto não deve ser considerado um produto médico, sistema de emergência ou substituto de profissionais especializados.

## Como contribuir

Contribuições são bem-vindas em:

- Firmware.
- Eletrônica.
- IA.
- Software.
- Documentação.
- Acessibilidade.
- Segurança.
- Testes.
- Tradução.
- Educação.
- Design de interação.
- Redução de custo e consumo.

Antes de contribuir, leia:

- `AGENTS.md`
- `CONTRIBUTING.md`
- `CODE_OF_CONDUCT.md`
- `SECURITY.md`
- `docs/`

## Visão

Construir uma plataforma aberta de inteligência pessoal que ajude pessoas a aprender, criar, se orientar e interagir com o mundo de maneira mais autônoma, acessível, segura e consciente.

> YBY significa You By Yourself: tecnologia para ampliar a autonomia humana, não para substituí-la.

## Alinhamento institucional

O YBY dialoga com os princípios e objetivos públicos da Estratégia Brasileira de Inteligência Artificial (EBIA) e do Plano Brasileiro de Inteligência Artificial (PBIA), especialmente nos eixos de pesquisa, inovação, capacitação, inclusão, bem-estar, segurança, transparência e desenvolvimento responsável.

Esse alinhamento não representa vínculo, apoio, financiamento ou reconhecimento oficial por parte do Governo Federal.

## Licença

A licença do projeto ainda será definida de acordo com os componentes de software, firmware, documentação, modelos e hardware utilizados.

artificial-intelligence
open-source
wearable
edge-ai
assistive-technology
accessibility
education
privacy
computer-vision
voice-assistant
esp32
esp32-s3
t-watch
lilygo
embedded-systems
machine-learning
local-ai
responsible-ai
brazil
Brasil
inteligência artificial 

Código e firmware: Apache License 2.0
Documentação: CC BY-SA 4.0
Esquemas e arquivos de hardware: CERN-OHL-S-2.0
Datasets próprios: CC BY 4.0 ou CC0, conforme o caso
