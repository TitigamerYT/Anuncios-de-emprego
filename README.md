# Agregador de Anúncios de Emprego

## Projeto de Avaliação — Linguagens de Programação

**Grupo:** 22

**Elementos do grupo:**
- Tiago Marcos 25252
- Luis Belo 25793

---

## 1. Descrição do projeto

O projeto consiste no desenvolvimento de uma aplicação em Python para **agregar anúncios de emprego provenientes de diferentes fontes**.

O objetivo é facilitar a pesquisa de oportunidades de emprego, permitindo ao utilizador consultar e filtrar ofertas através de diferentes critérios.

A aplicação será desenvolvida de forma modular e, numa fase posterior, deverá integrar a recolha e processamento automático de informação publicada na Web.

---

## 2. Problema

Atualmente, os anúncios de emprego encontram-se distribuídos por diferentes plataformas e fontes.

Esta situação pode tornar a pesquisa de oportunidades de emprego mais demorada, uma vez que o utilizador precisa de consultar diferentes locais para encontrar ofertas adequadas.

A nossa solução pretende centralizar essa informação numa única aplicação.

---

## 3. Objetivos

Os principais objetivos do projeto são:

- Centralizar anúncios de emprego provenientes de diferentes fontes;
- Facilitar a pesquisa de ofertas;
- Permitir a filtragem dos anúncios;
- Apresentar os detalhes e requisitos de cada oferta;
- Organizar a informação de forma simples e intuitiva;
- Numa fase posterior, recolher automaticamente informação de fontes Web.

---

## 4. Funcionalidades previstas

A aplicação deverá permitir:

- Pesquisar ofertas por cargo;
- Filtrar ofertas por localização;
- Filtrar ofertas por área profissional;
- Consultar os detalhes de uma oferta;
- Consultar os requisitos de uma vaga;
- Visualizar os anúncios disponíveis.

Estas funcionalidades correspondem às funcionalidades essenciais previstas para o tema do Grupo 22.

---

## 5. Estrutura dos dados

Nesta primeira fase, os anúncios de emprego serão representados através de uma **lista de ofertas**.

Cada oferta poderá ser inicialmente representada através de um **tuplo**, contendo informações como:

```text
(
    cargo,
    localização,
    área profissional,
    empresa,
    requisitos
)
```

Exemplo:

```text
(
    "Programador Python",
    "Beja",
    "Informática",
    "Empresa Tech",
    "Conhecimentos de Python e SQL"
)
```

A estrutura dos dados poderá ser alterada ou melhorada nas fases seguintes do projeto, de acordo com a evolução da aplicação.

---

## 6. Organização da solução

A solução será organizada em diferentes componentes, de forma a separar responsabilidades.

Estrutura prevista:

```text
agregador_empregos/
│
├── main.py
├── empregos.py
├── dados.py
├── pesquisa.py
├── README.md
└── requirements.txt
```

### `main.py`

Responsável pelo menu principal e pela interação com o utilizador.

### `empregos.py`

Responsável pelas operações relacionadas com as ofertas de emprego, como a listagem e consulta dos detalhes.

### `dados.py`

Responsável pelos dados utilizados pela aplicação.

### `pesquisa.py`

Responsável pelas funcionalidades de pesquisa e filtragem das ofertas.

### `README.md`

Contém a documentação do projeto.

### `requirements.txt`

Contém a indicação das dependências externas utilizadas pelo projeto.

---

## 7. Fluxo previsto da aplicação

O funcionamento geral previsto é:

```text
Fontes de anúncios
        ↓
Recolha de informação
        ↓
Tratamento e organização
        ↓
Pesquisa / filtragem
        ↓
Apresentação dos resultados
        ↓
Consulta dos detalhes da oferta
```

---

## 8. Tecnologias

A aplicação será desenvolvida utilizando:

- **Python 3**
- **Git**

Serão utilizadas bibliotecas da biblioteca padrão do Python sempre que possível.

Caso sejam utilizadas bibliotecas externas, estas serão identificadas e justificadas no projeto.

---

## 9. Instalação e execução

### Requisitos

É necessário ter o **Python 3** instalado no computador.

### Execução

Depois de obter o projeto, executar:

```bash
python main.py
```

---

## 10. Exemplo de utilização

Ao iniciar a aplicação, será apresentado um menu semelhante a:

```text
======================================
     AGREGADOR DE ANÚNCIOS DE EMPREGO
======================================

1 - Listar ofertas de emprego
2 - Pesquisar por cargo
3 - Pesquisar por localização
4 - Pesquisar por área profissional
5 - Ver detalhes de uma oferta
0 - Sair
```

O utilizador poderá escolher uma das opções e consultar ou pesquisar as ofertas disponíveis.

---

## 11. Limitações atuais

Nesta fase inicial do projeto:

- Os dados utilizados poderão ser dados de exemplo;
- A recolha automática da Web ainda não está implementada;
- A persistência dos dados será desenvolvida numa fase posterior;
- Os mecanismos de validação, exceções e testes serão aprofundados nas fases seguintes.

Estas funcionalidades serão desenvolvidas e integradas durante a evolução do projeto.

---

## 12. Evolução prevista

### Entrega Intermédia 1

- Definição do problema;
- Definição das funcionalidades;
- Desenho da solução;
- Escolha das estruturas de dados;
- Desenvolvimento da estrutura inicial do projeto.

### Entrega Intermédia 2

Prevê-se a implementação de:

- Maior modularização;
- Estruturas de dados mais completas;
- Leitura e escrita de ficheiros CSV/JSON;
- Validação dos dados introduzidos;
- Tratamento de exceções;
- Testes básicos;
- Integração dos diferentes módulos.

### Entrega Final

Prevê-se a conclusão da aplicação, documentação, organização final do repositório e demonstração do funcionamento integral da solução.

---

## 13. Fontes e utilização de informação externa

Caso sejam utilizadas fontes externas, bibliotecas ou dados provenientes da Web, estas serão identificadas e documentadas no projeto.

Na recolha automática de informação serão respeitadas as regras definidas no enunciado, incluindo as limitações de acesso e as condições aplicáveis às fontes utilizadas.

---

## 14. Estado atual do projeto

**Fase:** Entrega Intermédia 1 — Proposta e desenho da solução

**Estado:** Em desenvolvimento
