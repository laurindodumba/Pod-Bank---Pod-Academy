import streamlit as st
from eda import upload_file
# from eda import visualize

# Injeta o CSS do Bootstrap ou estilos personalizados
def inject_bootstrap():
    bootstrap_link = """
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    """
    st.markdown(bootstrap_link, unsafe_allow_html=True)

def create_footer():
    footer_html = """
        <div class="footer">
        <hr style="border-top: 1px solid #bbb;">
        <p style="text-align: center; font-size: 14px;">© 2024 PoD Bank - Laurindo</p>
        </div>
        """
    st.markdown(footer_html, unsafe_allow_html=True)

# Configurações da página
st.set_page_config(page_title=" POD BANK - APPLICATION ", layout="wide")

# Injeta Bootstrap CSS
inject_bootstrap()

# Seleção de páginas
page = st.sidebar.selectbox("Navegação", ["HOME", "SERVIÇOS", "INSIGHTS", "SOBRE NÓS"])

import streamlit as st
import base64

# Função para converter imagem em base64
def get_image_base64(path):
    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()


if page == "HOME":
    st.markdown("<h1 style='text-align: center;'>APLICAÇÃO WEB - POD BANK</h1>", unsafe_allow_html=True)
    
    # Caminho da imagem
    image_path = r"C:\Users\Eduardo\Documents\Pod Academy\pod bank\Capturar.PNG"
    
    # Obter a imagem codificada em base64
    image_base64 = get_image_base64(image_path)
    
    # HTML/CSS para exibir a imagem com bordas arredondadas
    image_html = f"""
    <style>
    img {{
        border-radius: 15px;  /* Arredonda as bordas da imagem */
    }}
    </style>
    <img src="data:image/png;base64,{image_base64}" width="1000">
    """
    
    # Usar markdown para exibir a imagem com CSS personalizado
    st.markdown(image_html, unsafe_allow_html=True)

elif page == "SERVIÇOS":
    st.title("SERVIÇOS")
    # Conteúdo da página secundária 1
    st.write("Conteúdo da Página Secundária 1.")
    create_footer()

elif page == "INSIGHTS":
    st.title("ANÁLISE ESTATÍSTICA")
    # Conteúdo da página secundária 2

    df = upload_file()


    create_footer()

elif page == "SOBRE NÓS":
    st.title("NÓS")
    st.write("parametros de configuração da API")
    create_footer()