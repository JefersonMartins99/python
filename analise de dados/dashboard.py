import streamlit as st 
import pandas as pd 
import plotly_express as px 


df=pd.read_csv("C:/Users/evely/Downloads/base_de_vendas.csv")

st.title("Dashbord de Vendas")

cidades=st.multiselect("Selecione as Cidades",df["Cidade"].unique())

if cidades :
    
    df=df[df["Cidade"].isin(cidades)]

st.metric("Faturamento Total",f"R${df["Valor_Venda"].sum()}")

st.metric("Media de Vendas",f"R${df["Valor_Venda"].mean()}")


st.bar_chart(df.groupby("Cidade")["Valor_Venda"].sum())

st.bar_chart(df.groupby("Produto")["Valor_Venda"].sum())
