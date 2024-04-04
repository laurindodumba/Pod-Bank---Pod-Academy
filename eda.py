import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import seaborn as sns

#Subir  a base de de dados

def upload_file():
    global df
    uploaded_file = st.file_uploader("Escolha a base de dados")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df)

    
        analise_total = df["AMT_INCOME_TOTAL"].sum()
        moda_credito = df["AMT_CREDIT"].mode()[0]  # Acessa o primeiro valor da moda
        mean_credito = df["AMT_CREDIT"].mean()
        med_credito = df["AMT_CREDIT"].median()  # Corrigido para a coluna correta

        total1, total2, total3, total4 = st.columns(4, gap='large')

        with total1:
            st.info("SOMA", icon="🪙")
            st.metric(label="SOMA", value=f"{analise_total:,.0f}")

        with total2:
            st.info("MODA", icon="🪙")  # Ajustado para mostrar a informação correta
            st.metric(label="MODA", value=f"{moda_credito:,.0f}")

        with total3:  # Corrigido para usar total3
            st.info("MÉDIA", icon="🪙")  # Ajustado para mostrar a informação correta
            st.metric(label="MÉDIA", value=f"{mean_credito:,.0f}")

        with total4:
            st.info("MEDIANA", icon="🪙")  # Ajustado para mostrar a informação correta
            st.metric(label="MEDIANA", value=f"{med_credito:,.0f}")



        # Histograma da Renda Total
        fig, ax = plt.subplots()
        df['AMT_INCOME_TOTAL'].hist(bins=30, color='skyblue', edgecolor='black', ax=ax)
        ax.set_title('Distribuição da Renda Total')
        ax.set_xlabel('Renda Total')
        ax.set_ylabel('Frequência')

        st.pyplot(fig)


        # Gráfico de Distribuição do Crédito
        fig, ax = plt.subplots()
        sns.histplot(df['AMT_CREDIT'], kde=True, color="blue", ax=ax)
        ax.set_title('Distribuição do Crédito')
        ax.set_xlabel('Crédito')
        ax.set_ylabel('Densidade')

        st.pyplot(fig)


        fig, ax = plt.subplots()
        ax.scatter(df['CODE_GENDER'], df['NAME_CONTRACT_TYPE'], alpha=0.5)
        ax.set_title('Renda Total vs. Crédito')
        ax.set_xlabel('Renda Total')
        ax.set_ylabel('Crédito')

        st.pyplot(fig)


        fig, ax = plt.subplots()
        ax.scatter(df['NAME_EDUCATION_TYPE'], df['NAME_FAMILY_STATUS'], alpha=0.5)
        ax.set_title('Renda Total vs. Crédito')
        ax.set_xlabel('Renda Total')
        ax.set_ylabel('Crédito')

        st.pyplot(fig)


    

