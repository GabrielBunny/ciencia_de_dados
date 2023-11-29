import pandas as pd
import matplotlib.pyplot as plt

# Abrindo o arquivo csv
df = pd.read_csv('expectativa_vida.csv')

# Filtrar os dados para os países de interesse
paises_interesse = ['Brazil', 'Japan', 'Switzerland', 'Australia', 'Spain', 'France']

# Filtrar os dados para os países de interesse
df_interesse = df[df['Country'].isin(paises_interesse)]

# Calcular a média mundial da expectativa de vida
media_mundial = df['Life expectancy'].mean()

# Configurar o tamanho do gráfico
plt.figure(figsize=(10, 6))

# Plotar a expectativa de vida em relação aos anos para cada país
for pais in paises_interesse:
    df_pais = df_interesse[df_interesse['Country'] == pais]
    if pais == 'Brazil':
        plt.plot(df_pais['Year'], df_pais['Life expectancy'], label=pais, color='black', linewidth=5)
    else:
        plt.plot(df_pais['Year'], df_pais['Life expectancy'], label=pais)

# Plotar a média mundial como uma linha no gráfico
plt.axhline(media_mundial, color='red', linestyle='--', label='Média Mundial')

# Adicionar rótulos e título ao gráfico
plt.xlabel('Ano')
plt.ylabel('Expectativa de Vida (Idade)')
plt.title('Comparação da Expectativa de Vida ao longo do tempo')
plt.legend()
plt.grid(True)

# Exibir o gráfico
plt.show()

import matplotlib.pyplot as plt

# Filtrar os dados para os países de interesse
paises_interesse = ['Brazil', 'India', 'Nigeria', 'Pakistan', 'Democratic Republic of the Congo', 'Angola']

# Filtrar os dados para os países de interesse
df_interesse = df[df['Country'].isin(paises_interesse)]

# Calcular a média mundial de mortes infantis
media_mundial = df['Infant deaths'].mean()

# Configurar o tamanho do gráfico
plt.figure(figsize=(10, 6))

# Plotar as mortes infantis em relação aos anos para cada país
for pais in paises_interesse:
    df_pais = df_interesse[df_interesse['Country'] == pais]
    if pais == 'Brazil':
        plt.plot(df_pais['Year'], df_pais['Infant deaths'], label=pais, color='black', linewidth=5)
    else:
        plt.plot(df_pais['Year'], df_pais['Infant deaths'], label=pais)

# Plotar a média mundial como uma linha no gráfico
plt.axhline(media_mundial, color='red', linestyle='--', label='Média Mundial')

# Adicionar rótulos e título ao gráfico
plt.xlabel('Ano')
plt.ylabel('Mortes Infantis')
plt.title('Comparação das Mortes Infantis ao longo do tempo')
plt.legend()
plt.grid(True)

# Exibir o gráfico
plt.show()

# IDH POR PAÍSES DESENVOLVIDOS E SUBDESENVOLVIDOS

# Filtrar os dados para os países de interesse
paises_interesse = ['Brazil', 'United States', 'Germany', 'China', 'Afghanistan', 'Ethiopia']

# Filtrar os dados para os países de interesse
df_interesse = df[df['Country'].isin(paises_interesse)]

# Configurar o tamanho do gráfico
plt.figure(figsize=(10, 6))

# Plotar o IDH em relação aos anos para cada país
for pais in paises_interesse:
    df_pais = df_interesse[df_interesse['Country'] == pais]
    
    if pais == 'Brazil':
        plt.plot(df_pais['Year'], df_pais['Income composition of resources'], label=pais, color='black', linewidth=5)
    else:
        plt.plot(df_pais['Year'], df_pais['Income composition of resources'], label=pais)

# Adicionar rótulos e título ao gráfico
plt.xlabel('Ano')
plt.ylabel('IDH')
plt.title('Evolução do IIDH ao longo dos anos para países desenvolvidos e subdesenvolvidos')
plt.legend()
plt.grid(True)

# Exibir o gráfico
plt.show()

# GASTOS COM SAÚDE E EXPECTATIVA DE VIDA

import pandas as pd
import matplotlib.pyplot as plt

# Filtrar os dados para o ano de 2014
df_2014 = df[df['Year'] == 2014]

# Calcular a porcentagem de gastos com saúde em relação ao PIB per capita
df_2014['expenditure percentage'] = df_2014['percentage expenditure'] / df_2014['GDP'] * 100

# Filtrar as colunas relevantes para o gráfico
df_plot = df_2014[['expenditure percentage', 'Life expectancy']]

# Plotar o gráfico
plt.figure(figsize=(10, 6))
plt.scatter(df_plot['expenditure percentage'], df_plot['Life expectancy'])
plt.xlabel('Porcentagem de gastos com saúde em relação ao PIB per capita (%)')
plt.ylabel('Expectativa de Vida')
plt.title('Gastos com saúde vs Expectativa de Vida em 2014')
plt.grid(True)
plt.show()

# PIB PER CAPITA E EXPECTATIVA DE VIDA

import pandas as pd
import matplotlib.pyplot as plt

# Filtrar as colunas relevantes para o gráfico
df_plot = df[['GDP', 'Life expectancy']]

# Plotar o gráfico
plt.figure(figsize=(10, 6))
plt.scatter(df_plot['GDP'], df_plot['Life expectancy'])
plt.xlabel('PIB per capita')
plt.ylabel('Expectativa de Vida')
plt.title('PIB per capita vs Expectativa de Vida')
plt.grid(True)
plt.show()