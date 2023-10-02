import datetime as dt

import pandas as pd
import streamlit as st
import yfinance as yf

st.set_page_config(page_title='Dashboard de Finanças',layout='wide')

st.title('Dashboard de Finanças Pessoais')


end_date = dt.datetime.today()
start_date = dt.datetime(end_date.year-1,end_date.month,end_date.day)


with st.container():
    st.header('Pesquise de acordo com as opções abaixo:')

    col1, col2, col3 = st.columns(3)
    with col1:
        ativo = st.text_input('Digite o nome da Ação no formato AÇÃO.SA',value='PETR4.SA')
        
    with col2:
        data_inicial = st.date_input('Selecione a data inicial',start_date)

    with col3:
        data_final = st.date_input('Selecione a data final',end_date)





# Obtendo os dados usando o yfinance
df = yf.download(tickers=ativo, start=data_inicial, end=data_final)
df.index = df.index.date

# Metricas
ult_atualizacao = df.index.max() #data da última att
ult_cotacao = round(df.loc[df.index.max(),'Adj Close'],2) #ultima cotação encontrada
menor_cotacao = round(df['Adj Close'].min(),2) #menor cotacao encontrada
maior_cotacao = round(df['Adj Close'].max(),2) #maior cotacao encontrada
prim_cotacao = round(df.loc[df.index.min(),'Adj Close'],2) #primeira cotacao
delta = round(((ult_cotacao-prim_cotacao)/prim_cotacao)*100,2) #delta

with st.container():
    with col1:
        st.metric(f"Última Atualização - {ult_atualizacao}","{:,.2f}".format(ult_cotacao),f"{delta}%")

    with col2:
        st.metric("Menor Cotação do período","{:,.2f}".format(menor_cotacao))
            
    with col3:
        st.metric("Maior Cotação do período","{:,.2f}".format(maior_cotacao))


with st.container():
    st.area_chart(df[['Adj Close']],color=['#8A2BE2'])
