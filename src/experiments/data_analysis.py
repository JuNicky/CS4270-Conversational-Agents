import pandas as pd

data = pd.read_csv('src/experiments/cocktail_data.csv', encoding='ISO-8859-1')

print(data.head())