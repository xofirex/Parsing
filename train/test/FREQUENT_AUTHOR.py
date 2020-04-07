import pandas as pd


file = r'C:\test\train\MENTIONED_AUTHORS.CSV'
df = pd.read_csv(file)
df = df.dropna(subset=['author_name'])
df = df['author_name'].value_counts()
print(df[:1])