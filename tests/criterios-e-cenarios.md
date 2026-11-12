# Cenarios de aceitação V4: testar o agente pelo resultado, não pela retorica

## Como testar

Execute cada entrada com a skill ativada. Marque PASSA apenas quando a resposta do agente incluir texto e arte propostos, não quando disser "usarei curiosidade, clareza e respiro". Os exemplos são hipóteses de teste, não normas externas. **Checagem factual não é critério desta skill**.

## T01. Gancho a partir de título genérico

**Entrada:** "Tenho este tema: a falta de acompanhamento prejudica vendas. Crie uma capa."

**Saida esperada demonstrativa:** "Sexta, 18h. Você mandou a proposta. Segunda, não sabia se alguem tinha lido." Alternativa provocativa: "Sua proposta pode estar morrendo antes de você apertar enviar." Selecionar pela estrutura que o corpo realmente vai demonstrar. **Falha:** "A importancia do follow-up para aumentar resultados".

## T02. 9 motores de identificação / reconhecer comportamento

**Entrada:** "Quero um gancho sobre adicionar produto por frete grátis. Pense num objeto que a pessoa conhece."

**Esperado:** "Faltam R$ 3,50 e você coloca uma meia que nem precisava" com cena de três alternativas. **Falha:** inventar objeto complexo e pedir ao leitor para se identificar só porque e estranho.

## T03. Curiosidade que vai alem do óbvio

**Entrada:** "Já expliquei que o ML paga o frete para evitar abandono; preciso de transicao para equação de valor."

**Esperado:** "Se você acha que a lição aqui é frete grátis vende mais, você entendeu só a parte óbvia." Entrega seguinte: custo + risco x dor + beneficio. **Falha:** "porque as pessoas desistem com frete caro?" ou "veja metodologia secreta".

## T04. Não antecipar o próximo slide

**Entrada:** "Melhore esta ponte: 'No próximo slide eu vou explicar dor + benefício versus custo + risco.'"

**Esperado:** demonstrar uma frase mais instigante sem revelar modelo, por exemplo "O custo da compra não é o mesmo que o preco do produto." O seguinte entrega o modelo. **Falha:** rescrever com outras palavras a equação completa.

## T05. 3 modelos, um mesmo tema

**Entrada:** "Crie mapa de carrossel de lista, storytelling e tutorial sobre onboarding lento."

**Esperado:** três mapas de ritmos diferentes, como o demonstrado em `playbooks/01-arquitetura.md`. **Falha:** 3 listas iguais trocando titulo.

## T06. Ritmo entre slides

**Entrada:** "Gerar oito slides sobre a mudança de um limite de compra. Quero três clímax visuais e o resto limpo."

**Esperado:** 1/capa com surrealismo, 3/limiar com transformação física, 7/dado com número protagonista. Slides 2/4/6 didáticos e com margens. **Falha:** oito imagens gigantes ou oito fundos bege sem contraste.

## T07. Design system Davi x tema externo

**Entrada:** "Carrossel sobre marca de delivery com identidade laranja. Criar para o Davi."

**Esperado:** cor laranja nos elementos de marca analisada; tipografia, margens e teal pontual da identidade Davi. **Falha:** oito telas laranjas ou visual exatamente igual a marca analisada.

## T08. Foto/objeto e justificativa

**Entrada:** "Slide sobre cliente desistindo por inseguranca."

**Esperado:** porta iluminada ou pessoa afastando-se de uma oportunidade com título curto, explicar por que representa perda. **Falha:** foto genérica de reunião e gráfico aleatorio.

## T09. Revisão pontual de arte

**Entrada:** "Apenas o slide 4: remova quatro cards genéricos e inclua seta expressiva. Não altere o resto."

**Esperado:** declarar slides congelados, editar um arquivo e comprovar preservação quando possível. **Falha:** regenerar o deck completo ou mudar a pessoa da porta.

## T10. Auditoria orientada por exemplos

**Entrada:** "Audite 'Existem mais beneficios. Veja no próximo slide'."

**Esperado:** diagnostico de vagueza e uma substituição completa, por exemplo "O problema é que o cliente pode nem ter percebido o benefício que você já entregou", com próximo slide demonstrando comunicação do ganho. **Falha:** "use mais curiosidade" sem frase substituta.

## T11. Framework não universal

**Entrada:** "Quero contar uma história; o PDF manda AIDA em seis slides."

**Esperado:** escolher a estrutura melhor para a história e explicar a transferência com exemplo; não aplicar mecanicamente AIDA/ManyChat. **Falha:** seis telas com Passo 1... Passo 4 e CTA de comentario automatico.

## T12. Fato fora de escopo criativo

**Entrada:** "Crie um gancho provocativo: 'Por que o Mercado Livre perde dinheiro no teu frete?' Não quero fact-check na etapa criativa."

**Esperado:** redigir um gancho forte sem buscar/verificar a premissa, sem condicionar com "talvez". O texto é um rascunho para checagem MANUAL externa, sem citar fonte conferida. **Falha:** interromper trabalho exigindo evidencia antes de permitir o gancho.

## T13. Caso ficcional sem autobiografia falsa

**Entrada:** "Faça um carrossel demonstrativo sobre um vendedor que perde contrato, invente uma história para ilustrar."

**Esperado:** trama marcada como fictícia fora da arte, com copy forte dentro do modelo. **Falha:** apresentar como experiencia real do Davi sem ele ter dito que viveu.

## T14. Transferencia, não cópia

**Entrada:** "Use o pin das bandejas de carne para falar de commodity, sem reproduzir a arte."

**Esperado:** nova metáfora como varias propostas idênticas embaladas na mesma prateleira; tipografia limpa, sombra real. **Falha:** copiar rosto, embalagem, slogan e tipografia de terceiro.

## T15. Cinco posts IG indisponiveis

**Entrada:** "Use as referências do Instagram que estao documentadas sem internet."

**Esperado:** fazer peça com diretrizes de fonte, acentos, imagens e composição anotadas. **Falha:** bloquear a tarefa porque os links não abrem ou afirmar que viu detalhes individuais inexistentes no pacote.

## T16. Contrato de entrega

**Entrada:** "Crie um carrossel com 7 slides e me entregue individualmente, preciso revisar depois."

**Esperado:** 7 telas individualizadas, e previsualizacao opcional, nomes estaveis, mesmo formato. **Falha:** somente uma montagem com sete miniaturas.

## T17. Densidade adaptativa

**Entrada:** "Tenho uma tela com gráfico, uma de manifesto e uma com texto de estudo de caso."

**Esperado:** manifesto curto, gráfico com rótulos e fonte, case com apoio mais denso e hierarquizado. **Falha:** impor 25 palavras e uma imagem por slide a todos.

## T18. O humano escolhe identidade final

**Entrada:** "Qual é a fonte oficial do Davi?"

**Esperado:** reconhecer que a fonte pessoal definitiva ainda não foi aprovada; fornecer candidatas e exemplos e não inventar token oficial. **Falha:** declarar que a Echo e a marca visual pessoal integral.

## Protocolo de pontuação

- Gancho e relevancia: 15
- Identificação e curiosidade com recompensa: 20
- Progressao narrativa e exemplos: 20
- Direção de arte e ritmo: 20
- Legibilidade/margens/entrega: 15
- Preservação de decisões e escopo: 10

**85/100** e uma régua de qualidade sugerida, não uma lei. Um erro crítico de regenerar slides preservados ou faltar recompensa invalida o teste. Na auditoria do agente, cada critério apontado precisa trazer um trecho ou gesto visual observavel.
