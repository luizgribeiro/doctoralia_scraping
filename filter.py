import pandas as pd


df = pd.read_csv('info.csv', sep=';')

df.drop_duplicates()

df.to_csv('docs_info.csv', sep=';')


