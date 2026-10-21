# Agregador de Anúncios de Emprego

Projeto de Linguagens de Programação 2026/2027 — Grupo 22

- Tiago Marcos 25252
- Luís Belo 25793

## Descrição

As ofertas de emprego estão espalhadas por vários sites, o que torna a procura lenta.
A nossa aplicação junta anúncios de várias fontes num só sítio, onde é possível
pesquisar por cargo, filtrar por localização e área, e ver os detalhes e requisitos de cada vaga.

Os anúncios vão ser recolhidos da Web com Python (scraping) e guardados em ficheiro,
para a aplicação funcionar mesmo sem acesso aos sites.

## Interface

Interface gráfica para PC, feita com Tkinter. Os ecrãs foram desenhados no Figma:

- **Ecrã inicial** – pesquisa por cargo, filtros por localização e área, e lista de ofertas.
- **Detalhe da vaga** – descrição, requisitos, fonte, data e botão para abrir o anúncio original.

## Dados

Cada oferta é um tuplo e todas as ofertas ficam numa lista:

```python
("Programador Python júnior", "Beja", "Informática", "TechSul",
 ("Python e SQL", "Git"), "Desenvolvimento de aplicações...",
 "Site de empregos A", "20/10/2026", "https://exemplo.com/oferta/1")
```

Ordem dos campos: cargo, localização, área, empresa, requisitos, descrição, fonte, data, link.

## Organização

| Ficheiro | Para que serve |
|---|---|
| `main.py` | Arranca a aplicação e trata da interface |
| `dados.py` | Ofertas de exemplo (mais tarde, leitura/escrita em CSV/JSON) |
| `pesquisa.py` | Pesquisa por cargo e filtros por localização e área |
| `empregos.py` | Listagem das ofertas e detalhes de cada uma |

## Como executar

É preciso ter o Python 3 instalado.

```bash
python main.py
```

Por agora não há dependências externas (ver `requirements.txt`).

## Limitações e riscos

Para já só existe o esqueleto do código, com dados de exemplo.

Riscos que prevemos com o scraping:
- os sites podem mudar a estrutura das páginas;
- os sites podem bloquear pedidos seguidos (vamos usar pausas entre pedidos);
- alguns anúncios podem vir com dados em falta;
- cada site mostra os dados de forma diferente, por isso temos de os converter para o mesmo formato.
