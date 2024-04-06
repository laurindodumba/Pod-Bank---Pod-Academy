import pickle as pkl
import streamlit as st

# Carregando o modelo
# with open('modelo_credito.pkl', 'rb') as file:
#     model = pkl.load(file)


#Criar formulário para os usários
def formulario():
    genero_list = ('', 'M', 'F')

    genero_option = list(range(len(genero_list)))
    genero_escolha = st.selectbox("SEXO", genero_option, format_func=lambda x: genero_list[x])

    # Se tem meios de transporte
    carro_list = ('', 'Y', 'N')

    opcoes = list(range(len(carro_list)))
    escolha_carro = st.selectbox("CARRO", opcoes, format_func=lambda x: carro_list[x])

    #nivel  escolar
    nivel_escolar = ('','Secundário', 'Educação Superior')

    nivel = list(range(len(nivel_escolar)))
    escolha_nivel = st.selectbox("NÍVEL ESCOLAR", nivel, format_func=(lambda x: nivel_escolar[x]))

    #Estado Civil
    estado_civil = ('','Casado', 'Solteiro', 'Noivo', 'Separado')
    estado = list(range(len(estado_civil)))
    escolha_estado = st.selectbox("ESTADO CIVIL", estado, format_func=(lambda x: estado_civil[x]))

    #Modelo de residência
    modelo_casa = ('','APARTAMENTO', "CASA", )

    # Quantidade do empréstimo
    duracao = st.number_input("AMT_ANNUITY",value=0)

    # Tempo de emprestimo
    tempo =  ['',"3 Meses", "6 Meses", "9 Meses", "12 Meses", "16 Meses", "24 Meses", "48 Meses"]
    tempo_opcoes = range(len(tempo))
    tempo_selecao = st.selectbox("Duração do Empréstimo", tempo_opcoes, format_func=(lambda x: tempo[x]))


    #Botão para enviar o pedido de crédito
    if st.button("ENVIAR PEDIDO DE CRÉDITO"):
        # Verifique se todas as seleções foram feitas
        if not all([genero_escolha, escolha_carro, escolha_nivel, escolha_estado, escolha_modelo, duracao is not None, tempo_selecao]):
            st.error("Por favor, preencha todos os campos.")
        else:
            # Processo de predição
            features = [[genero_escolha-1, escolha_carro-1, duracao, escolha_nivel-1, escolha_estado-1, escolha_modelo-1]]
            prediction = model.predict(features)

            if prediction == 0:
                st.error("Olá: De acordo aos cálculos não recebu crédito")
            else:
                st.success("Olá: Após análise do seu cadastro você recebeu crédito")

