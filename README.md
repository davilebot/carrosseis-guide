# Carrosséis Premium V4

Skill autocontida para **criar, auditar, comparar e refinar carrosséis**. Versão compilada a partir da conversa de refinamento do carrossel do Mercado Livre, do PDF de 12 páginas, dos dois conjuntos de Pinterest e do pacote ZIP de guias e referências de conteúdo. O material prioriza exemplos já executados, com explicação do por que é como adaptar.

## Instalacao

A estrutura deste arquivo ZIP contém a pasta `carrosseis-premium/`. Extraia-a e instale como pasta de skills do agente. A entrada da skill é `SKILL.md`; mantenha as pastas `playbooks/`, `examples/`, `referencias/`, `profiles/`, `assets/` e `tests/` ao lado do arquivo principal. Dependendo do agente, o caminho da pasta de skills pode ser `.agents/skills/` ou `.claude/skills/`.

## Exemplos de invocacao

- `Use $carrosseis-premium para gerar um carrossel de 7 slides sobre por que clientes demoram a responder propostas. Quero estilo Davi.`
- `Use $carrosseis-premium para auditar esta copy. Me traga antes/depois de ganchos, transições e CTA. Não mexa em fatos.`
- `Use $carrosseis-premium para revisar somente o slide 4. Preserve os outros sete e a imagem principal.`
- `Use $carrosseis-premium para criar um carrossel de lista usando o sistema visual do cliente [X], sem aplicar a paleta do Davi.`

## Princípio mais importante

**Não basta dizer o que fazer. Mostre o resultado da técnica sendo aplicada.** Todo playbook inclui exemplos concretos. Análise o material e generalize a lógica, não o assunto. O estudo do Mercado Livre é um precedente, não o padrão universal.

## Fact-check fora de escopo

Criação e revisão conteudista não fazem pesquisa factual, não énfraquecem o gancho com condicionais, não bloqueiam copy por falta de citações. A verificação é uma etapa manual externa definida pelo usuario. Confira a política editorial da skill antes de aplicar.

## Canais e imagem

Os exemplos priorizam Instagram e LinkedIn. A proporção usada nos testes foi aproximadamente 4:5 por slide. Verifique as especificacoes da plataforma no momento de publicar, no seu fluxo externo. Não dependa de links externos para executar a skill.

## Arquivos da referência

- `referencias/diagnostico-pdf-12-paginas.md` comenta página a página o PDF original e inclui exemplos de adaptacao; PDF original em `assets/diagnostico/`.
- `referencias/pinterest-anotado.md` explica as 9 telas fornecidas dos pins; arquivos JPEG em `assets/pinterest/`.
- `referencias/instagram-e-pinterest.md` mapeia as 36 capturas locais dos cinco posts, as nove imagens do Pinterest e os registros textuais do Notion.
- `examples/casos/02-concorrente-barato.md` decupa o carrossel próprio do usuário de 14 slides; PNGs em `assets/concorrente-barato/`.
- `examples/casos/01-mercado-livre.md` preserva decisões aprovadas/rejeitadas e a origem da frase "só a parte óbvia"; imagens de teste em `assets/mercado-livre/`.

## Licenciamento de referências

Imagens e capturas de criadores de terceiros foram fornecidas como material de estudo. São referências, **não assets livres para republicacao**. A skill não inclui nenhum arquivo de fonte tipográfica. Consulte `NOTAS-DE-ORIGEM.md`.
