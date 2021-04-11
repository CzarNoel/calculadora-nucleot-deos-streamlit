import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

#page title

image = Image.open('dna-logo.png')

st.image(image, use_column_width=True)

st.write("""
# Contador de DNA Nucleotídeos Web App

Este aplicativo faz a contagem da composição de nucleotídeos de um DNA

***
""")

#input text box

#st.sidebar.header('Enter DNA squence)
st.header('Sequência de DNA')

sequence_input = ">Sequêncis de DNA (pressionar 'enter' para cada sequência) \nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

#sequence = st.sidebar.text_area("Sequence input", sequence_input,)
sequence = st.text_area("Sequência", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:] #skip the sequence name (first line)
sequence = ''.join(sequence) #concatenates list to string

st.write("""
***
""")

#prints the input DNA sequence
st.header('INPUT (Sequência DNA)')
sequence

#DNA nucleotides count
st.header('OUTPUT (Contagem de Nucleotídeos do DNA)')

#1. print dictionary
st.subheader('1. Dicionário')
def DNA_nucleotide_count(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C'))
    ])
    return d

X = DNA_nucleotide_count(sequence)

X_label = list(X)
X_values = list(X.values())

X

#2. print text
st.subheader('2. Portanto,')
st.write('Temos ' + str(X['A']) + ' adeninas (A)')
st.write('Temos ' + str(X['T']) + ' timinas (T)')
st.write('Temos ' + str(X['G']) + ' guaninas (G)')
st.write('Temos ' + str(X['C']) + ' citocinas (G)')

#3. display dataframe
st.subheader('3. Dataset')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'contagem'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'nucleotídeos'})
st.write(df)

#4. display bar chart using altair 
st.subheader('3. Gráfico de barras')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotídeos',
    y='contagem'
)
p = p.properties(
    width=alt.Step(80) #constrols width of bar 
)
st.write(p)
