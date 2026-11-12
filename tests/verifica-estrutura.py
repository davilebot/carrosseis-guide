#!/usr/bin/env python3
"""Smoke-test local da estrutura da skill. Nao executa teste criativo/modelo."""
from pathlib import Path
import re
import sys
root=Path(__file__).resolve().parents[1]
required=[
 'SKILL.md','README.md','profiles/davi.md','playbooks/01-arquitetura.md',
 'playbooks/02-ganchos-identificacao.md','playbooks/03-ganchos-curiosidade.md',
 'playbooks/04-retencao-e-frameworks.md','playbooks/05-direcao-de-arte.md',
 'playbooks/06-producao-e-revisao-local.md','playbooks/07-escopo-editorial.md',
 'examples/banco-80-ganchos.md','examples/transicoes-antes-depois.md',
 'examples/receitas-visuais.md','examples/casos/01-mercado-livre.md',
 'examples/casos/02-concorrente-barato.md',
 'referencias/diagnostico-pdf-12-paginas.md',
 'referencias/pinterest-anotado.md',
 'referencias/instagram-e-pinterest.md',
 'assets/diagnostico/diagnostico-carrosseis-virais.pdf',
 'assets/mercado-livre/slide-04-final.png',
]
errors=[]
for f in required:
 if not (root/f).is_file():errors.append('FALTA: '+f)
for label,glob,n in [('Pinterest','pin*.jpg',9),('Concorrente','*.png',14),('Sam','*.png',8)]:
 folder={'Pinterest':'assets/pinterest','Concorrente':'assets/concorrente-barato','Sam':'assets/sam-gaudet'}[label]
 got=sum(1 for p in (root/folder).glob(glob) if not p.name.startswith('._') and (label!='Concorrente' or p.name[:2].isdigit()))
 if got!=n:errors.append(f'{label}: {got}, esperado {n}')
sk=(root/'SKILL.md').read_text(encoding='utf-8')
if not sk.startswith('---\n'):errors.append('SKILL.md sem frontmatter')
if 'não' not in sk.lower():errors.append('revisar escopo')
print(f'Arquivos: {sum(1 for p in root.rglob("*") if p.is_file())}')
print('Smoke-test estrutura:', 'OK' if not errors else 'FALHOU')
for e in errors:print(' -',e)
sys.exit(1 if errors else 0)
