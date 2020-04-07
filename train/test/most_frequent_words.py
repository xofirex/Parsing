import pandas as pd


file = r"C:\test\train\BOOK.CSV"
df = pd.read_csv(file)
df = pd.Series(' '.join(df['title']).lower().split())
df = df.where(df.str.len()>5).value_counts()[:10]
print(df)
