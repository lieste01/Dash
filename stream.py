import streamlit as st
import matrix
import datetime

potAtiva = "Pot Ativa"
tempAmb = "TempAmb"
tempEnr = "Temp Enr"
TempOleo = "Temp Oleo"

st.set_page_config(page_title="Matriz", page_icon="🔅", layout="wide",  menu_items=None)

jana = ['Jana 1', 'Jana 2', 'Jana 3', 'Jana 4', 'Jana 5', 'Jana 6', 'Jana 7', 'Jana 8', 'Jana 9', 'Jana 10',
        'Jana 11', 'Jana 12', 'Jana 13', 'Jana 14', 'Jana 15', 'Jana 16', 'Jana 17', 'Jana 18', 'Jana 19', 'Jana 20']

col1, col2 = st.columns(2, gap="large")
optionJana = col1.selectbox("Escolha uma TS:", jana)
data = col2.date_input(label="Escolha uma data:", value=datetime.datetime.today()+datetime.timedelta(-1), min_value=datetime.date(2023, 8, 2), max_value=datetime.datetime.today())

with col1:
    matrix.matrixCalor(potAtiva, data, optionJana, "Matrix de Dados de Potência Ativa dos Eletrocentros (Trafos WEG)")
    matrix.matrixCalor(tempEnr, data, optionJana, "Matrix de Dados de Temperatura dos Eletrocentros (Trafos WEG)")

with col2:
    matrix.matrixCalor(TempOleo, data, optionJana,
                       "Matrix de Dados de Temperatura do Óleo dos Eletrocentros (Trafos WEG)")
    st.line_chart(matrix.horaTemp(tempAmb, data, optionJana,
                       "Dados de Temperatura Ambiente dos Eletrocentros (Trafos WEG)"))

