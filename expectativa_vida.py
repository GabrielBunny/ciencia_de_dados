import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('expectativa_vida copy.csv')

plt.plot(df['Year'], df['infant deaths'], color='red')
plt.show()