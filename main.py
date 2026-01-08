import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import date

# Carregar dados
# Capturar cotações o Itau - ITUB4 - 2010 - 2025

@st.cache_data
def carregar_acoes(empresa):

    dados = yf.download(
        tickers=empresa,
        start="2015-01-01",
        end=date.today(),
        group_by="ticker"
    )

    # Devido ao multi index, é necessário a list comprehension para buscar o fechamento de cada cotação
    fechamento = pd.DataFrame({
        acao: dados[acao]["Close"] for acao in empresa
    })
    return fechamento

@st.cache_data
def buscar_ativos():
    base_ativos = pd.read_csv("IBOV.csv", sep=';')
    ativos = list(base_ativos["Código"])
    db_ativos = [item + ".SA" for item in ativos]
    return db_ativos

acoes = buscar_ativos()
dados = carregar_acoes(acoes)

st.write("""
    # Dashboard cotação de ações

         
O dashboard abaixo representa a evolução dos preços das ações ao longo dos anos
""")

# Sidebar para filtros do dashboard
st.sidebar.header("Filtros")

# Filtro de Multiselect
lista_acoes = st.sidebar.multiselect("Escolhas as ações que deseja visualizar",acoes, placeholder="Escolher ação", default=["ITUB4.SA", "PETR4.SA"])
if not lista_acoes:
    st.info("Selecione ao menos uma ação")
    st.stop()

dados = carregar_acoes(lista_acoes)

if len(lista_acoes) == 1:
        acao_unica = lista_acoes[0]
        dados = dados.rename(columns={acao_unica: "Close"})



# Filtro de datas - slider
data_inicio = dados.index.min().to_pydatetime()
data_fim = dados.index.max().to_pydatetime()
intervalo_data_cotacoes = st.sidebar.slider("Selecione o período das datas", 
                                            min_value=data_inicio, 
                                            max_value=data_fim, 
                                            value=(data_inicio, data_fim),
                                            format="DD/MM/YYYY")

st.sidebar.caption(
    f"De {data_inicio.strftime('%d/%m/%Y')} até {data_fim.strftime('%d/%m/%Y')}"
)

dados = dados.loc[intervalo_data_cotacoes[0]:intervalo_data_cotacoes[1]]

st.line_chart(dados)

performance_text = ""

if len(lista_acoes) == 0:
    lista_acoes = list(dados.columns)

elif len(lista_acoes) == 1:
    dados = dados.rename(columns={"Close": acao_unica})

for acao in lista_acoes:
    # Calculo performance: Valor final / Valor inicial - 1
    performance_ativo = float(dados[acao].iloc[-1] / dados[acao].iloc[0] - 1)

    if performance_ativo > 0:
        performance_text = performance_text + f"{acao}: :green[{performance_ativo:.2%}]  \n "
    elif performance_ativo < 0:
        performance_text = performance_text + f"{acao}: :red[{performance_ativo:.2%}]  \n "
    else:
        performance_text = performance_text + f"{acao}: {performance_ativo:.2%}  \n "

st.write(f"""
### Performance dos Ativos
- Performance de cada ativo selecionado pelo período informado  \n
{performance_text}
""")