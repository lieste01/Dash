import datetime

import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st


def matrixCalor(dataframe, data, jana, titulo):
    dataFrame = pd.read_excel(f"{dataframe}.xlsx")

    nameColumns = ['Data']

    # Cria uma array com os novos nomes das colunas
    for usina in range(1, 21):
        for ts in range(1, 8):
            nameColumns.append(f"Jana {usina} - TS {ts}")

    # Muda o nome das colunas, substitution com os nomes da array nameColumns
    dataFrame.columns = nameColumns

    # Transforma a coluna Data em Date
    dataFrame['Data'] = pd.to_datetime(dataFrame['Data']).dt.strftime('%Y-%m-%d')

    # Substitui os valores [-11059] No Good Data For Calculation para 0
    dataFrame = dataFrame.replace('[-11059] No Good Data For Calculation', 0)
    dataFrame = dataFrame.replace('[-11057] Not Enough Values For Calculation', 0)
    # Filtro usando indexação booleana
    df_filtered = dataFrame[(dataFrame['Data'] == f"{data}")][
        ['Data', f'{jana} - TS 1', f'{jana} - TS 2', f'{jana} - TS 3',
         f'{jana} - TS 4', f'{jana} - TS 5', f'{jana} - TS 6',
         f'{jana} - TS 7']]
    colunas = [f'{jana} - TS 1', f'{jana} - TS 2', f'{jana} - TS 3',
               f'{jana} - TS 4', f'{jana} - TS 5', f'{jana} - TS 6',
               f'{jana} - TS 7']

    # Defina o tamanho da matriz (número de linhas e colunas)
    matrix = np.zeros((len(df_filtered.columns), len(df_filtered.columns)))

    for row, col in df_filtered.iterrows():
        for num in range(1, len(df_filtered.columns)):
            for num2 in range(1, len(df_filtered.columns)):
                if col[num] == 0:
                    print("IF")
                    matrix[num][num2] = 0
                elif col[num2] == 0:
                    print("ELIF")
                    matrix[num][num2] = 0
                else:
                    matrix[num][num2] = round((float(col[num]) / float(col[num2])) - 1, 2)

    matrix = [linha[1:] for linha in matrix[1:]]

    # Converter a matriz para um dataframe para que as datas sejam os rótulos das linhas e colunas
    matrix_df = pd.DataFrame(matrix, columns=colunas, index=colunas)

    fig_corr = px.imshow(matrix_df, text_auto=True)

    fig_corr.update_layout(height=500,
                           width=700,
                           margin={'l': 50, 'r': 50, 't': 50, 'b': 50},
                           title_text=f"{titulo}",
                           title_x=0.1
                           )

    st.plotly_chart(fig_corr, theme=None, use_container_width=True)


def horaTemp(dataframe, data, jana, titulo):
    dataFrame = pd.read_excel(f"{dataframe}.xlsx")

    nameColumns = ['Data']

    # Cria uma array com os novos nomes das colunas
    for usina in range(1, 21):
        for ts in range(1, 8):
            nameColumns.append(f"Jana {usina} - TS {ts}")

    # Muda o nome das colunas, substitution com os nomes da array nameColumns
    dataFrame.columns = nameColumns

    # Transforma a coluna Data em Date
    dataFrame['Data'] = dataFrame['Data'].dt.strftime("%Y-%m-%d %H:%M:%S")
    dataFrame.index = pd.to_datetime(dataFrame['Data'])

    # Substitui os valores [-11059] No Good Data For Calculation para 0
    dataFrame = dataFrame.replace('[-11059] No Good Data For Calculation', 0)
    dataFrame = dataFrame.replace('[-11057] Not Enough Values For Calculation', 0)

    # Filtro usando indexação booleana
    dataInc = pd.to_datetime(data)
    dataFin = dataInc + datetime.timedelta(hours=23, minutes=59)

    df_filtered = dataFrame[dataFrame.index >= dataInc][[f'{jana} - TS 1']]

    df_filtered = df_filtered[df_filtered.index <= dataFin]

    fig = px.line(df_filtered, title=titulo)
    st.plotly_chart(fig)
