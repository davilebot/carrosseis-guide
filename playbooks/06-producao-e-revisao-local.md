# Produção, entrega e microedicao sem destruir o aprovado

## A regra nasceu de um erro real

O usuário pediu ajustar só uma frase do slide 4. Quando o sistema regenerava a imagem completa, alterava objetos, cor, tipografia, imagem e até outros slides. Ele pediu os oito arquivos separados para conseguir revisar apenas a tela escolhida.

**Regra v4:** objetos já aprovados são patrimonio da peca. Alterar somente onde o problema exige, com comparação antes/depois. Se não houver arquivo editavel, editar localmente e declarar as limitacoes de preservação; não prometer identidade pixel a pixel quando a ferramenta repinta áreas grandes.

## Exemplo executado: o slide 4 de um carrossel de oito

**Antes:** "Isso não é generosidade, e uma aposta" + personagem saindo na porta + 4 cartões "mais conversões", "menos abandono", "mais confiança", "mais recorrencia" + botão "próximo". **Problema:** os quatro tópicos são vagos e não ligam aposta a equação de valor; o botão não materializa o convite para arrastar.

**Depois aprovado:** manter o homem/porta; título e frase da aposta; remover os quatro cartões; acrescentar a provocação "Se você acha que a lição aqui é frete grátis vende mais, você entendeu só a parte óbvia"; seta grande desenhada para a direita. **Por que:** não éxpor o modelo cedo, questionar a conclusão prematura e criar uma ponte com a equação do slide 5.

**Escopo preservado:** imagens 1,2,3,5,6,7,8 devem permanecer. O slide 5 explica o que o 4 provoca. Só a tela 4 e editada.

## Exemplo de auditoria com resultado

**Solicitacao:** "Aumente o respiro da capa". **Saida ruim:** regenerar a capa com outra caixa, outro título e outra cor. **Saida correta:** preservar copy, objeto, fundo e paleta; recuar bloco textual 60px da borda superior e 50px da esquerda, aumentar faixa de respiro inferior, reposicionar só se necessário. Entregar imagem alterada e comparativo.

**Solicitacao:** "Não gostei da tipografia do título". **Saida correta:** apresentar 2 alternativas tipograficas com a MESMA copy é MESMA imagem. Não mudar a cena, o objeto ou o número de slides.

## Como preparar a arte para revisão

- Preferir texto em camadas editáveis; imagem conceptual/3D em camada separada, fundo editavel, acentos separados.
- Nomear: `slide-01.png` a `slide-08.png` e arquivos-fonte editáveis quando a ferramenta permitir.
- Se produzir uma montagem 4x2 para aprovação, ela não substitui as telas individuais. Uma miniatura não é tamanho final.
- Trabalhar em uma proporção decidida no briefing; no teste do Mercado Livre a montagem mais quadrada foi melhor que images estreitas. Usar 4:5 para teste quando o usuário não indicar outra coisa, sem afirmar normas atualizadas da plataforma.
- Fazer revisão em tamanho de celular, sem confiar na miniatura da montagem.

## Controle de alteracoes

```
PEDIDO: "Trocar apenas o texto final do slide 4"
TRAVADO: slides 1-3 e 5-8
PERMANECE NO 4: homem saindo na porta, fundo, teal, margens, título, copy da aposta
MUDA NO 4: fecho e seta
ANTES: 4 tópicos e CTA pequeno
DEPOIS: uma provocação curta e seta expressiva
VERIFICACAO: arquivos travados idênticos no antes/depois
```

Se o editor não fornece controle de camadas, o agente deve separar o que pode preservar com seguranca e não alegar garantia impossivel. Quando possível, compara hashes dos slides não mexidos. **Um pedido pequeno pede a menor mudanca eficaz, não uma revisão geral.**

## Auditoria final de arte

1. A headline ainda e legível no tamanho de celular?
2. O elemento surrealista comunica a ideia ou só ocupa espaco?
3. Margens e respiro nas bordas continuam confortaveis?
4. O slide de conteúdo esta subordinado a explicação?
5. O sentido da seta/diagrama e claro sem legenda?
6. A imagem/contexto da marca estudada substituiu o sistema do autor?
7. Existem textos gerados pela IA com erros de ortografia/numeros?
8. Slides congelados estao preservados?
9. O próximo slide entrega a expectativa criada?
