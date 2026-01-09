# 📈 Dashboard de Cotações de Ações (IBOV)

Este projeto é um **dashboard interativo desenvolvido com Python e Streamlit** para visualização da evolução histórica de ações listadas no **Ibovespa (B3)**.

O objetivo é permitir que o usuário selecione diferentes ativos, filtre períodos de tempo e visualize tanto o **gráfico de preços** quanto a **performance percentual** de cada ação no período escolhido.

---

## 🚀 Funcionalidades

- 📊 Visualização gráfica das cotações (preço de fechamento)
- 🧮 Cálculo automático da performance percentual por ativo
- 🗂️ Seleção múltipla de ações (multiselect)
- 📆 Filtro de período por slider de datas
- ⚡ Cache de dados para melhor performance
- 📁 Base de ativos carregada via CSV (IBOV)

---

## 🛠️ Tecnologias Utilizadas

- **Python**
- **Streamlit** – interface e dashboard
- **Pandas** – manipulação de dados
- **yFinance** – coleta de dados financeiros
- **CSV** – base de ativos do Ibovespa

---

## 📂 Estrutura do Projeto

```text
dashboard_cotacao_acoes/
│
├── main.py # Código principal do dashboard
├── requirements.txt # Dependências do projeto
├── IBOV.csv # Base de ativos do Ibovespa
└── README.md
```

## 📦 Instalação e Execução Local

### Rode o projeto 
```bash
git clone https://github.com/seu-usuario/dashboard-cotacao-acoes.git
cd dashboard-cotacao-acoes

pip install -r requirements.txt

streamlit run main.py
```


🌐 Deploy

O projeto é compatível com Streamlit Cloud.
Basta garantir que o arquivo requirements.txt esteja presente na raiz do repositório.

📊 Fonte dos Dados

Os dados de mercado são obtidos através da biblioteca yFinance, que utiliza informações públicas do Yahoo Finance.

⚠️ Os dados podem sofrer atrasos ou indisponibilidade momentânea.

🎯 Objetivo do Projeto

Este projeto faz parte do meu aprendizado e portfólio na área de desenvolvimento Python e análise de dados, com foco em:

Dashboards interativos

Visualização de dados financeiros

Boas práticas de organização e performance

⭐ Se você gostou do projeto, deixe uma estrela no repositório!
