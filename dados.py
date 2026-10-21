"""
dados.py

Responsável pelos dados utilizados pela aplicação.

Nesta primeira fase, as ofertas de emprego são dados de exemplo.
Cada oferta é representada por um tuplo e todas as ofertas
ficam guardadas numa lista.

Estrutura de cada oferta (tuplo):
    (cargo, localizacao, area, empresa, requisitos, descricao, fonte, data, link)

Nas fases seguintes, os dados passarão a ser recolhidos da Web
e guardados em ficheiros CSV/JSON.
"""

# Lista de ofertas de exemplo (lista de tuplos)
OFERTAS = [
    (
        "Programador Python júnior",
        "Beja",
        "Informática",
        "TechSul",
        ("Licenciatura em Engenharia Informática", "Python e SQL", "Git"),
        "Desenvolvimento de aplicações internas e automatização de processos.",
        "Site de empregos A",
        "20/10/2026",
        "https://exemplo.com/oferta/1",
    ),
    (
        "Técnico de redes",
        "Évora",
        "Informática",
        "NetAlentejo",
        ("Conhecimentos de redes", "Cisco"),
        "Instalação e manutenção de redes informáticas.",
        "Site de empregos B",
        "19/10/2026",
        "https://exemplo.com/oferta/2",
    ),
    (
        "Designer UI/UX",
        "Remoto",
        "Design",
        "Criativa Lda",
        ("Figma", "Portefólio"),
        "Desenho de interfaces para aplicações web e móveis.",
        "Site de empregos C",
        "18/10/2026",
        "https://exemplo.com/oferta/3",
    ),
    (
        "Assistente administrativo",
        "Beja",
        "Administração",
        "Alentejo Serviços",
        ("12.º ano", "Conhecimentos de informática na ótica do utilizador"),
        "Apoio administrativo e atendimento ao público.",
        "Site de empregos A",
        "17/10/2026",
        "https://exemplo.com/oferta/4",
    ),
]


def obter_ofertas():
    """Devolve a lista de ofertas disponíveis."""
    # TODO (Entrega 2): ler as ofertas de um ficheiro CSV/JSON
    pass
