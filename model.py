import pickle as pkl
import streamlit as st

# Carregando o modelo
# with open('modelo_credito.pkl', 'rb') as file:
#     model = pkl.load(file)

def formulario():
    genero_list = ('', 'M', 'F')
    genero_option = list(range(len(genero_list)))
    genero_escolha = st.selectbox("SEXO", genero_option, format_func=lambda x: genero_list[x])

    carro_list = ('', 'Y', 'N')
    opcoes = list(range(len(carro_list)))
    escolha_carro = st.selectbox("CARRO", opcoes, format_func=lambda x: carro_list[x])

    nivel_escolar = ('','Secundário', 'Educação Superior')
    nivel = list(range(len(nivel_escolar)))
    escolha_nivel = st.selectbox("NÍVEL ESCOLAR", nivel, format_func=(lambda x: nivel_escolar[x]))

    estado_civil = ('','Casado', 'Solteiro', 'Noivo', 'Separado')
    estado = list(range(len(estado_civil)))
    escolha_estado = st.selectbox("ESTADO CIVIL", estado, format_func=(lambda x: estado_civil[x]))

    modelo_casa = ('','APARTAMENTO', 'CASA')
    casa = list(range(len(modelo_casa)))
    escolha_modelo = st.selectbox("MODELO DE RESIDÊNCIA", casa, format_func=lambda x: modelo_casa[x])

    # Renda anual do solicitante
    renda_anual = st.number_input("Renda Anual", value=0)

    # Quantidade do empréstimo solicitado
    duracao = st.number_input("Montante do Empréstimo Solicitado", value=0)

    tempo = ['',"3 Meses", "6 Meses", "9 Meses", "12 Meses", "16 Meses", "24 Meses", "48 Meses"]
    tempo_opcoes = range(len(tempo))
    tempo_selecao = st.selectbox("Duração do Empréstimo", tempo_opcoes, format_func=(lambda x: tempo[x]))

    #Botão para enviar o pedido de crédito
    if st.button("ENVIAR PEDIDO DE CRÉDITO"):
        # Verifique se todas as seleções foram feitas e se a renda anual é maior que 0
        if not all([genero_escolha, escolha_carro, escolha_nivel, escolha_estado, escolha_modelo, renda_anual > 0, duracao > 0, tempo_selecao]):
            st.error("Por favor, preencha todos os campos e assegure-se de que os valores inseridos são válidos.")
        else:
            # Calculando o limite de empréstimo (exemplo: 3 vezes a renda anual)
            limite_emprestimo = renda_anual * 3

            # Verificando se o montante solicitado não excede o limite
            if duracao > limite_emprestimo:
                st.error(f"O montante solicitado excede seu limite de empréstimo de {limite_emprestimo}.")
            else:
                # Processo de predição (ajuste conforme seu modelo)
                features = [[genero_escolha-1, escolha_carro-1, duracao, escolha_nivel-1, escolha_estado-1, escolha_modelo-1]]
                # Criar a predição
                # prediction = model.predict(features)
                
                # condição para ter o crédito
                prediction = 1 

                if prediction == 0:
                    st.error("Olá: De acordo aos cálculos, seu crédito não foi aprovado.")
                else:
                    st.success("Olá: Após análise do seu cadastro, você recebeu crédito.")
