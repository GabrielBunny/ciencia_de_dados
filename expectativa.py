import pandas as pd
import matplotlib.pyplot as plt

# Abrindo o arquivo csv
df = pd.read_csv('expectativa_vida.csv')

# EXPECTATIVA DE VIDA NO BRASIL vs MUNDO

# Definindo o Brasil como o país de referência
df_brasil = df[df['Country'] == 'Brazil']

# Criando a média mundial
df_media_mundial = df.groupby('Year')['Life expectancy'].mean().reset_index()

# Configurando o tamanho do gráfico
plt.figure(figsize=(10, 6))

# Plotando o gráfico comparativo
plt.plot(df_media_mundial['Year'], df_media_mundial['Life expectancy'], label='Média Mundial', color='red', linewidth=5)
plt.plot(df_brasil['Year'], df_brasil['Life expectancy'], label='Brasil', color='green', linewidth=5)

# Adicionando rótulos e título ao gráfico
plt.xlabel('Ano')
plt.ylabel('Expectativa de Vida (%)')
plt.title('Expectativa de Vida no Brasil comparado com o mundo')
plt.legend()

# Ajustando os valores mostrados no gráfico
plt.xticks(df_brasil['Year'])
plt.yticks(range(0, 101, 5))
plt.grid(True)

# Mostrando
plt.show()

# TOP 5 PAISES COM MAIOR EXPECTATIVA DE VIDA vs BRASIL
# Agrupando os dados por país e calculando a média da expectativa de vida para cada país
df_media_paises = df.groupby('Country')['Life expectancy'].mean().reset_index()

# Ordenando o DataFrame em ordem decrescente com base na coluna 'Life expectancy'
df_media_paises = df_media_paises.sort_values('Life expectancy', ascending=False)

# Selecionando os 5 primeiros países
top_5_paises = df_media_paises.head(5)

# Filtrando o DataFrame original apenas para os países selecionados
df_top_paises = df[df['Country'].isin(top_5_paises['Country'])]

# Configurando o tamanho do gráfico
plt.figure(figsize=(10, 6))

plt.plot(df_brasil['Year'], df_brasil['Life expectancy'], label='Brasil', color='green', linewidth=5)

# Plotando um gráfico de linhas para mostrar a expectativa de vida de cada país
for pais in top_5_paises['Country']:
    df_pais = df_top_paises[df_top_paises['Country'] == pais]
    plt.plot(df_pais['Year'], df_pais['Life expectancy'], label=pais)

# Adicionando rótulos e título ao gráfico
plt.xlabel('Ano')
plt.ylabel('Expectativa de Vida')
plt.title('5 Países com Maior Expectativa de Vida')
plt.legend()
plt.yticks(range(0, 101, 5))
plt.grid(True)

# Exibindo o gráfico
plt.show()

# MORTES DE CRIANÇAS NO BRASIL E NO MUNDO

# Filtrando os dados para obter as mortes infantis do Brasil e da média mundial
df_brasil = df[df['Country'] == 'Brazil']
df_mundial_media = df.groupby('Year')['Infant deaths'].mean().reset_index()

# Configurando o tamanho do gráfico
plt.figure(figsize=(10, 6))

# Plotando as linhas das mortes infantis do Brasil e da média mundial
plt.plot(df_brasil['Year'], df_brasil['Infant deaths'], label='Brasil', linewidth=5, color='green')
plt.plot(df_mundial_media['Year'], df_mundial_media['Infant deaths'], label='Média Mundial', linewidth=5, color='red')

# Adicionando rótulos e título ao gráfico
plt.xlabel('Ano')
plt.ylabel('Mortes Infantis')
plt.title('Mortes Infantis no Brasil vs Média Mundial')
plt.legend()
plt.grid(True)

# Exibindo o gráfico
plt.show()

# 10 paises com mais mortes de crianças

# Agrupando os dados por país e calculando o total de mortes infantis para cada país
df_total_mortes_por_pais = df.groupby(['Country', 'Year'])['Infant deaths'].sum().reset_index()

# Selecionando os 5 países com mais mortes infantis
top_5_paises_mortes = df_total_mortes_por_pais.groupby('Country')['Infant deaths'].sum().nlargest(5).index

# Filtrando o DataFrame original apenas para os países selecionados
df_top_5_paises_mortes = df_total_mortes_por_pais[df_total_mortes_por_pais['Country'].isin(top_5_paises_mortes)]

# Configurando o tamanho do gráfico
plt.figure(figsize=(12, 6))

# Plotando o gráfico de linhas para cada país
for pais in top_5_paises_mortes:
    df_pais = df_top_5_paises_mortes[df_top_5_paises_mortes['Country'] == pais]
    plt.plot(df_pais['Year'], df_pais['Infant deaths'], label=pais)

# Adicionando rótulos e título ao gráfico
plt.xlabel('Ano')
plt.ylabel('Mortes Infantis')
plt.title('Evolução das Mortes Infantis dos 5 Países com Mais Mortes')

# Exibindo a legenda
plt.legend()

# Exibindo o gráfico
plt.show()