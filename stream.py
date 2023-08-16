import streamlit as st
import matrix
import datetime



jana = ['Jana 1', 'Jana 2', 'Jana 3', 'Jana 4', 'Jana 5', 'Jana 6', 'Jana 7', 'Jana 8', 'Jana 9', 'Jana 10',
        'Jana 11', 'Jana 12', 'Jana 13', 'Jana 14', 'Jana 15', 'Jana 16', 'Jana 17', 'Jana 18', 'Jana 19', 'Jana 20']

optionJana = st.selectbox("Escolha uma TS:", jana)

data = st.date_input("Escolha uma data:", datetime.date(2023, 8, 2))

matrix.matrixCalor(data, optionJana)

#image = Image.open('matrix.jpg')

#st.image(image, caption='Sunrise by the mountains')