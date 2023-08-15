import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

dataFrame = pd.read_excel("C:\\Users\\lff\\OneDrive - Elera\\Desktop\\Temp Enr.xlsx")

nameColumns = ['Data']

# Cria uma array com os novos nomes das colunas
for usina in range(1, 21):
    for ts in range(1, 8):
        nameColumns.append(f"Jana {usina} - TS {ts}")

# Muda o nome das colunas, substitution com os nomes da array nameColumns
dataFrame.columns = nameColumns

# Transforma a coluna Data em Date
dataFrame['Data'] = pd.to_datetime(dataFrame['Data']).dt.strftime('%Y-%m-%d %H:%M')

# Substitui os valores [-11059] No Good Data For Calculation para 0
dataFrame = dataFrame.replace('[-11059] No Good Data For Calculation', 0)

# Filtro usando indexação booleana
df_filtered = dataFrame[dataFrame['Data'] < '2023-08-02 00:00'][['Data', 'Jana 1 - TS 1']]

# Defina o tamanho da matriz (número de linhas e colunas)
matrix = np.zeros((len(df_filtered), len(df_filtered)))

for i, row in df_filtered.iterrows():
    for j, col in df_filtered.iterrows():
        matrix[i][j] = round(row['Jana 1 - TS 1'] / col['Jana 1 - TS 1'], 2)

# Converter a matriz para um dataframe para que as datas sejam os rótulos das linhas e colunas
matrix_df = pd.DataFrame(matrix, columns=df_filtered['Data'], index=df_filtered['Data'])

# Imprima a matriz (opcional)
print(matrix_df)

# Plotar a matriz usando o seaborn heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(matrix_df, annot=True, cmap='YlGnBu', fmt='.2f')


# Definir a rotação dos rótulos para que fiquem legíveis
plt.xticks(rotation=45)
plt.yticks(rotation=0)

plt.title(f'Matriz com Datas Refletidas Jana 1 - TS 1')
plt.xlabel('Data')
plt.ylabel('Data')
plt.tight_layout()
plt.show()
