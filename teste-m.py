import streamlit as st
import time
from PIL import Image
import random

name = st.sidebar.text_input(label='Preencha o seu nome: ', )
if not name:
    st.sidebar.warning('Insira um Nome.')
    st.stop()
st.sidebar.success('Obrigado por preencher!')

age = st.sidebar.number_input(label='Preencha a sua idade: ', format='%d', step=1)
if age <= 0:
    st.stop()

smoke = st.sidebar.radio('Fumante?', ('Nunca', 'Ocasionalmente', 'Sempre', 'Maria Fumaça'))
drink = st.sidebar.radio('Bebe?', ('Não', 'Ocasionalmente', 'Todos os Dias', 'Cana Brava'))

with st.form(key='questionario',  clear_on_submit=True):
    st.title('Sistema de Avaliação:')
    st.header('Através das suas respostas o formulário irá mostrar qual imagem corresponde ao seu perfil. ')
    st.subheader('Escolha as opções abaixo:')
    sport = st.selectbox('Qual o seu esporte favorito?', ('', 'Futebol', 'Hipismo', 'Boliche', 'Tênis', 'Natação'))
    movie = st.selectbox('Qual o seu filme favorito?', ('', 'Jurassic Park', 'Titanic', 'Frozem', 'Rambo', 'Era do Gelo'))
    locomotion = st.selectbox('Qual destes você prefere?', ('', 'Carro', 'Moto', 'Patinete', 'Bicicleta Elétrica', 'Patins'))
    game = st.selectbox('Qual destes jogos você prefere?', ('', 'Dama', 'Baralho', 'Xadrex', 'Bolinha de Gude', 'Pião'))
    button = st.form_submit_button('Calcular Dados')

    if button:
        if sport == '':
            st.warning('Esporte deve ser preenchido!')
            st.stop()
        if movie == '':
            st.warning('Filme deve ser preenchido!')
            st.stop()
        if locomotion == '':
            st.warning('Locomoção deve ser preenchido!')
            st.stop()
        if game == '':
            st.warning('Jogo deve ser preenchido!')
            st.stop()

        my_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.05)
            my_bar.progress(percent_complete + 1)
            if percent_complete == 60:
                st.write('Calma ai, tá indo!')
        st.balloons()
        image_rd = random.choice(['deer.jpg', 'clown.jpg', 'gay.jpg', 'girl.jpg', 'jegue.jpg'])
        if image_rd == 'girl.jpg':
            st.title('Hoje você teve sorte! Não é todo dia que você parece macho.')
        if image_rd == 'jegue.jpg':
            st.title('Tiramos uma foto sua passeando.')
        if image_rd == "clown.jpg":
            st.title('Sua cara preenchendo esse formulário.')
        if image_rd == "deer.jpg":
            st.title('Sua cara de manhã olhando no espelho')
        if image_rd == 'gay.jpg':
            st.title('Sua bandeira preferida. Ui!')
        image = Image.open(image_rd)
        st.image(image)
