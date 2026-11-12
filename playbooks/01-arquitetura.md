# Arquitetura de carrossel: diferentes peças exigem diferentes histórias

## Uma pergunta antes da criação

O leitor termina o carrossel sabendo ou sentindo **o que** que não sabia/sentia no começo? Um bom mapa responde isso com uma transformação de percepção, não com uma listinha de assuntos.

### Demonstração 1: mesma tese, quatro arquiteturas diferentes

Tese-base: "o cliente desiste quando mudar parece trabalhoso".

**LISTA (6 slides):** 1 "Os 4 'fretes' invisíveis da sua venda" (capa), 2 "1. Ele precisa te explicar tudo de novo" (cena de três formularios iguais), 3 "2. Ninguem diz quem assume a implementação" (duas cadeiras vazias), 4 "3. A proposta chega como um manual de 28 páginas" (documento gigante surreal), 5 "4. A equipe demora para responder" (relogio e conversa), 6 "Antes de desconto, elimine uma dessas quatro etapas" (síntese). Aqui o numero/itens e o ritmo modular fazem sentido.

**EDUCACIONAL (7 slides):** 1 "Ele queria comprar. Não queria passar pela sua implementação."; 2 cena: produto bom, processo ruim; 3 diagrama com benefício esperado x custo de mudar; 4 demonstração dos 3 custos percebidos; 5 exemplo antes/depois de onboarding; 6 pergunta "Qual etapa faz seu cliente dizer 'depois'?"; 7 síntese visual. O centro é o modelo, não uma lista exaustiva.

**STORYTELLING (7 slides):** 1 "O cliente disse SIM. E nunca comecou."; 2 contexto da venda; 3 tarefa inesperada de configuracao; 4 imagem de escada gigante de etapas; 5 virada "o sim foi pra promessa, não pro trabalho"; 6 implementação simplificada; 7 síntese. O centro é a tensão narrativa.

**OPINIAO (5 slides):** 1 "Seu produto pode estar perdendo para o 'deixa pra depois'."; 2 provocação ao discurso de "falta de lead"; 3 mostrar status quo; 4 "Antes de pedir mais demanda, diminua o custo de começar"; 5 CTA/reflexao. O centro é posicionamento.

**Lição:** a técnica de interacao, a imagem do objeto surrealista e os blocos de texto mudam conforme a forma. Não transformar tudo em PAS ou AIDA só porque e conhecido.

## O papel narrativo de cada tela, na prática

| Papel | O que esta na cabeca do leitor | Copy executada | Visual executado |
| --- | --- | --- | --- |
| Capa | "Pera, como assim?" | "A empresa aumentou o preco. E ficou mais fácil vender." | Etiqueta de preco crescendo fisicamente e encobrindo uma porta aberta |
| Identificação | "Eu já passei por isso" | "Faltam R$ 3,50. Você coloca a meia que nem precisava." | Três opções em UI limpa, meia como objeto próprio |
| Contexto | "Entendi o que mudou" | "Antes o benefício comecava em R$ 79. Depois foi para R$ 19." | Dois tickets, movimento de substituição, legenda que nomeia limiar |
| Evidencia | "Agora tem motivo" | "A pessoa não precisava de mais um recurso. Precisava de uma resposta mais clara." | Recorte de proposta antes/depois com apenas a passagem relevante |
| Virada | "O que eu achei estava incompleto" | "Você vendeu o software. Não vendeu o trabalho de implantar." | Imagem de caixa fechada com chave de fora |
| Ponte | "Tem mais uma camada aqui" | "Se você acha que a lição e frete grátis vende mais, entendeu só a parte óbvia." | Tipografia, pessoa saindo pela porta, seta grande a direita |
| Aplicação | "Eu consigo usar isso" | "Qual é o 'frete' do seu processo comercial?" | Barra de estados quero isso / talvez depois |
| Fecho | "Vou lembrar disso" | "Antes de baixar o preco, tire o 'frete' da sua venda." | Etiqueta removida de carrinho, muito espaco livre |

## Teste real de progressão, com duas versões

**Versão RUIM:** Slide 1 "5 dicas de CRM"; 2 "Organize contatos"; 3 "Atualize oportunidades"; 4 "Faca follow-up"; 5 "Use relatorios". Nada faz o leitor mudar de ideia. Os slides podem ser trocados de ordem sem alteracao da experiencia.

**Versão TRABALHADA:** 1 "Seu CRM esta atualizado. Mas quem ficou sem resposta?"; 2 cliente diz "me chama sexta"; 3 card atualizado para "negociacao" mas próximo passo vazio; 4 "o problema não é falta de dado, e falta de dono"; 5 demonstração: dono + prazo + ação minima na mesma etapa; 6 "se o CRM não orienta o próximo movimento, ele só descreve o passado". Agora existe progressão causal e uma tese que sobrevive ao conjunto.

## Mapa obrigatório antes de desenhar

Para cada slide registre: `função`, `copy exata`, `conhecimento entregue`, `conclusão óbvia do leitor`, `nova tensão`, `o que o próximo realmente entrega`, `intensidade visual`, `recurso visual`. **A primeira proposta deve ser um mapa, não oito imagens aleatorias.**

Um mapa preenchido encontra-se em `examples/casos/03-agentes-de-ia.md` e nos outros casos completos. Não imponha limites rigidos de palavras: um slide de noticia pode conter mais texto que um manifesto. O critério e absorcao, não uma conta cega de caracteres.
