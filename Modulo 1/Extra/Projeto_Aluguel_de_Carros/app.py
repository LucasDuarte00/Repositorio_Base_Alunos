import streamlit as st

#-------------------------------------SIDEBAR
st.sidebar.image('Logo.png')
st.sidebar.title('DriveX - Aluguel de carros ')

carros = ['Celta', 'Fusca', 'Palio', 'Pegeout']

modelo = st.sidebar.selectbox('Selecione o carro alugado', carros)

#-------------------------------------PRINCIPAL

st.title('DriveX - Aluguel de carros')
st.markdown(f'## Você escolheu o modelo: {modelo}')
st.image(f'{modelo}.png')

if modelo == 'Celta':
    diaria = 110

elif modelo == 'Fusca':
    diaria = 90

elif modelo == 'Palio':
    diaria = 130

elif modelo == 'Pegeout':
    diaria = 220

dias = st.text_input(f'Por quantos dias você alugou o {modelo}? ')
km = st.text_input(f'Quantos km você rodou? ')

if st.button('Calcular'):
    dias = int(dias)
    km = float(km)

    total_dias = dias * diaria
    total_km = km * 0.15
    aluguel = total_dias + total_km

    st.warning(f' Você alogou o {modelo} por {dias} dias e rodou {km}km. O valor do aluguel será R${aluguel}.')
