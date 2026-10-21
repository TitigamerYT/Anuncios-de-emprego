# Agregador de Anúncios de Emprego

Projeto de Linguagens de Programação 2026/2027 — Grupo 22

| Nome | Número |
|---|---|
| Tiago Marcos | 25252 |
| Luís Belo | 25793 |

## O problema

As ofertas de emprego estão espalhadas por várias plataformas. Procurar em todas é lento
e repetitivo, e é difícil comparar ofertas entre si.

## A solução

Uma aplicação em Python que junta, num só sítio, anúncios de emprego recolhidos
automaticamente de vários sites (scraping). O utilizador pode:

- **Pesquisar** ofertas pelo cargo pretendido;
- **Filtrar** por localização e por área profissional;
- **Consultar** os detalhes, os requisitos e a fonte de cada oferta.

## Interface

Interface gráfica para PC, feita com Tkinter. Os ecrãs foram desenhados primeiro no Figma.

| Ecrã de pesquisa | Detalhe da vaga |
|---|---|
| ![Ecrã de pesquisa](docs/ecra_pesquisa.png) | ![Detalhe da vaga](docs/ecra_detalhe.png) |

## Representação dos dados

Cada oferta é um **tuplo**, porque os dados não mudam depois de recolhidos e a ordem dos
campos é sempre a mesma:

```python
(cargo, localizacao, area, empresa, requisitos, fonte)
```

Os requisitos são também um tuplo, porque uma vaga pode ter vários.
Todas as ofertas ficam numa **lista**, que é percorrida com ciclos `for` e filtrada com `if`.

```python
ofertas = [
    ("Programador Python júnior", "Beja", "Informática", "TechSul",
     ("Python", "SQL", "Git"), "Site de empregos A"),
    ...
]
```

## Organização do código

| Ficheiro | Função |
|---|---|
| `main.py` | Arranca a aplicação e trata da interface |
| `dados.py` | Ofertas de exemplo (mais tarde, leitura e escrita em ficheiro) |
| `pesquisa.py` | Pesquisa por cargo e filtros por localização e área |

## Como executar

Requisitos: Python 3 (o Tkinter já vem incluído).

```bash
git clone https://github.com/TitigamerYT/Anuncios-de-emprego.git
cd Anuncios-de-emprego
python main.py
```

Nesta fase não há dependências externas. As bibliotecas usadas no scraping
serão adicionadas ao `requirements.txt`.

## Riscos previstos

| Risco | Como vamos lidar |
|---|---|
| Limites e bloqueios dos sites | Pausas entre pedidos e respeito pelo `robots.txt` |
| Mudanças na estrutura HTML | Tratamento de exceções (`try/except`) |
| Anúncios com dados em falta | Valor por omissão: "Não indicado" |
| Falhas de internet | Cópia dos dados guardada em ficheiro local |

## Estado atual

Entrega 1: proposta, desenho dos ecrãs, estrutura dos dados e esqueleto do código.
As funções ainda não estão implementadas.
