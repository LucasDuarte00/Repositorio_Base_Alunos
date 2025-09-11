import streamlit as st

#------------------------SIDEBAR
st.sidebar.image('Logo.png')
st.sidebar.title('SoundScape ')

estilos_musicas = ['Gospel' , 'Rock' , 'Reggae' , 'Pop' ]

estilo_escolhido = st.sidebar.selectbox('O que você quer ouvir hoje? ' , estilos_musicas )

#--------------------------PRINCIPAL
st.title('SoundScape - Playlists e Álbuns')
st.markdown(f'#### Você escolheu: {estilo_escolhido}')

if estilo_escolhido == 'Gospel':
    artistas = ['Arautos do Rei','Leonardo Gonçalves','Jonatas Ferreira','Prisma Brasil' ]
    artista = st.sidebar.selectbox('Escolha um artista:', artistas)

elif estilo_escolhido == 'Rock':
    artistas = ['Elvis Presley', 'Freddie Mercury','McCartney','Kurt Cobain' ]
    artista = st.sidebar.selectbox('Escolha um artista:', artistas)

elif estilo_escolhido == 'Reggae':
    artistas = ['Bob Marley','Jonh Holt', 'Omi', 'Yellowman']
    artista = st.sidebar.selectbox('Escolha um artista:', artistas)

elif estilo_escolhido == 'Pop':
    artistas = ['Justin Bieber','Michael Jackson','Beyoncé','Bruno Mars']
    artista = st.sidebar.selectbox('Escolha um artista:', artistas)

if artista == 'Arautos do Rei':
    st.markdown('#### Ótima escolha!😊')
    st.video('https://youtu.be/Fix16eQfXPg?si=wQZLZ0FqHn5o9dXu')

elif artista == 'Leonardo Gonçalves':
    st.markdown('#### Ótima escolha!')
    st.video('https://youtu.be/t9dz882vNB8?si=tfCQx5us2bVslLFD')

elif artista =='Jonatas Ferreira':
    st.markdown('#### Ótima escolha!😊')
    st.video('https://youtu.be/-ZdYKoKDBj0?si=5p64llpSkx1_EIdM')

elif artista == 'Prisma Brasil':
    st.markdown('#### Ótima escolha!😊')
    st.video('https://youtu.be/3lDFb9cq7kA?si=2wW18M9gw5EWejV0')

elif artista == 'Elvis Presley':
    st.markdown('#### Ótima escolha!😊')
    st.video('https://youtu.be/vGJTaP6anOU?si=NzZP0P5WWIqTXxY_')

elif artista == 'Freddie Mercury':
    st.markdown('#### Ótima escolha!😊')
    st.video('https://youtu.be/vbvyNnw8Qjg?si=XqeXQD3ZFp-PCYeD')

elif artista == 'McCartney':
    st.markdown('#### Ótima escolha!😊')
    st.video('https://youtu.be/-T_ZkacL9A0?si=zicv200ukxvV0oaE')

elif artista == 'Kurt Cobain':
    st.markdown('#### Ótima escolha!😊')
    st.video('https://youtu.be/hTWKbfoikeg?si=KXd6dEAFt2gD9nss')

elif artista == 'Bob Marley':
    st.markdown('#### Ótima escolha!😊')
    st.video('https://youtu.be/69RdQFDuYPI?si=jrCkU8hwKvjIxD4a')

elif artista == 'Jonh Holt':
    st.markdown('#### Ótima escolha!😊')
    st.video('https://youtu.be/uDT3tXnGFYk?si=Hml2PY85WN4gY8O9')

elif artista == 'Omi':
    st.markdown('#### Ótima escolha!😊')
    st.video('https://youtu.be/jGflUbPQfW8?si=X0PnTUbJnt__eBgJ')

elif artista == 'Yellowman':
    st.markdown('#### Ótima escolha!😊')
    st.video('https://youtu.be/HV46OGU7ksE?si=gmcCmnL2lDKPhbDf')

elif artista == 'Justin Bieber':
    st.markdown('#### Ótima escolha!😊')
    st.video('https://youtu.be/kffacxfA7G4?si=J4qLZvJN6Mchcw5q')

elif artista == 'Michael Jackson':
    st.markdown('#### Ótima escolha!😊')
    st.video('https://youtu.be/Zi_XLOBDo_Y?si=WKyzEduWlgI1800m')

elif artista == 'Beyoncé':
    st.markdown('#### Ótima escolha!😊')
    st.video('https://youtu.be/bnVUHWCynig?si=0t6sCFd66e_NB1E6')

elif artista == 'Bruno Mars':
    st.markdown('#### Ótima escolha!😊')
    st.video('https://youtu.be/fLexgOxsZu0?si=wg68z3b1ll2kxIrP')

