# -*- coding: utf-8 -*-
import pandas as pd
import plotly.express as px
import streamlit as st

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Dashboard de vendas", page_icon=":bar_chart:", layout="wide")

# Função para ler dados do Excel
@st.cache_data
def carregar_excel():
    df = pd.read_excel(
        io="mercado_faker.xlsx",
        engine="openpyxl",
        sheet_name="Sheet1",
        skiprows=0,
        usecols="B:Q",  # Ajuste aqui para refletir as colunas reais disponíveis no arquivo
        nrows=1000,
    )
    print(f"Teste: \n{df.head()}")  # Adicione esta linha para imprimir as primeiras linhas do DataFrame
    # Adicione a coluna 'Hora' ao dataframe
    df["Hora"] = pd.to_datetime(df["Hora"], format="%H:%M").dt.hour  # Ajuste aqui para refletir o nome real da coluna
    return df

# Validação dos dados de entrada
def validar_dados(df_selecionado):
    if df_selecionado.empty:
        st.warning("Não há dados válidos baseados nas configurações!")
        st.stop()

# Função para esconder o estilo do STREAMLIT
def esconder_estilo_st():
    estilo_st = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
    st.markdown(estilo_st, unsafe_allow_html=True)

# ---- Barra Lateral ----
df = carregar_excel()
st.sidebar.header("Por favor filtre aqui:")
estado = st.sidebar.selectbox("Selecione a estado:", options=["Todos"] + list(df["Estado"].unique()), index=0)
tipo_cliente = st.sidebar.selectbox("Selecione o tipo de cliente:", options=["Todos"] + list(df["Tipo_Cliente"].unique()), index=0)
genero = st.sidebar.selectbox("Selecione o gênero:", options=["Todos"] + list(df["Genero"].unique()), index=0)

df_selecionado = df.copy()

# Atualize a consulta com base nas seleções do usuário
if estado != "Todos":
    df_selecionado = df_selecionado[df_selecionado["Estado"] == estado]
if tipo_cliente != "Todos":
    df_selecionado = df_selecionado[df_selecionado["Tipo_Cliente"] == tipo_cliente]
if genero != "Todos":
    df_selecionado = df_selecionado[df_selecionado["Genero"] == genero]

validar_dados(df_selecionado)

# ---- Pagina Principal ----
st.title(":bar_chart: Dashboard de Vendas")
st.markdown("##")

# Principais KPIs
total_vendas = int(df_selecionado["Total"].sum())
avaliacao_media = round(df_selecionado["Avaliacao"].mean(), 1)
media_estrela = ":star:" * int(round(avaliacao_media, 0))
media_venda_transacao = round(df_selecionado["Total"].mean(), 2)

coluna_esquerda, coluna_meio, coluna_direita = st.columns(3)
with coluna_esquerda:
    st.subheader("Total Vendas:")
    st.subheader(f"R$ {total_vendas:,}")
with coluna_meio:
    st.subheader("Avaliação Média:")
    st.subheader(f"{avaliacao_media} {media_estrela}")
with coluna_direita:
    st.subheader("Média de vendas por transações:")
    st.subheader(f"R$ {media_venda_transacao}")

st.markdown("""---""")

# [BAR CHART]
vendas_por_linha_produto = df_selecionado.groupby(by=["Linha_Produto"])[["Total"]].sum().sort_values(by="Total")
fig_vendas_produto = px.bar(
    vendas_por_linha_produto,
    x="Total",
    y=vendas_por_linha_produto.index,
    orientation="h",
    title="<b>Vendas por linha de produto</b>",
    color_discrete_sequence=["#0083B8"] * len(vendas_por_linha_produto),
    template="plotly_white",
)
fig_vendas_produto.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

# [BAR CHART]
vendas_por_hora = df_selecionado.groupby(by=["Hora"])[["Total"]].sum()
fig_hourly_sales = px.bar(
    vendas_por_hora,
    x=vendas_por_hora.index,
    y="Total",
    title="<b>Vendas por hora</b>",
    color_discrete_sequence=["#0083B8"] * len(vendas_por_hora),
    template="plotly_white",
)
fig_hourly_sales.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)

coluna_esquerda, coluna_direita = st.columns(2)
coluna_esquerda.plotly_chart(fig_hourly_sales, use_container_width=True)
coluna_direita.plotly_chart(fig_vendas_produto, use_container_width=True)

esconder_estilo_st()
