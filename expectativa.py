import pandas as pd
import matplotlib.pyplot as plt

# eXPECTATIVA DE VIDA DO BRASIL, OS 5 MELHORES E A MÉDIA

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
        plt.plot(df_pais['Year'], df_pais['Life expectancy'], label=pais, color='black')
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

# GASTOS COM SAÚDE E E. V.

# Filtrar os dados para os anos de 2012, 2013 e 2014
df_2012 = df[df['Year'] == 2012]
df_2013 = df[df['Year'] == 2013]
df_2014 = df[df['Year'] == 2014]

# Calcular a porcentagem de gastos com saúde em relação ao PIB per capita em cada ano
df_2012['expenditure percentage'] = df_2012['percentage expenditure'] / df_2012['GDP'] * 100
df_2013['expenditure percentage'] = df_2013['percentage expenditure'] / df_2013['GDP'] * 100
df_2014['expenditure percentage'] = df_2014['percentage expenditure'] / df_2014['GDP'] * 100

# Filtrar as colunas relevantes para o gráfico para ambos os anos
df_plot_2012 = df_2012[['expenditure percentage', 'Life expectancy']]
df_plot_2013 = df_2013[['expenditure percentage', 'Life expectancy']]
df_plot_2014 = df_2014[['expenditure percentage', 'Life expectancy']]

# Plotar os gráficos para os anos selecionados
plt.figure(figsize=(10, 6))
plt.scatter(df_plot_2012['expenditure percentage'], df_plot_2012['Life expectancy'], label='2012')
plt.scatter(df_plot_2013['expenditure percentage'], df_plot_2013['Life expectancy'], label='2013')
plt.scatter(df_plot_2014['expenditure percentage'], df_plot_2014['Life expectancy'], label='2014')
plt.xlabel('Porcentagem de gastos com saúde em relação ao PIB per capita (%)')
plt.ylabel('Expectativa de Vida')
plt.title('Comparação dos Gastos com Saúde e Expectativa de Vida em 2012, 2013 e 2014')
plt.grid(True)
plt.legend()
plt.show()