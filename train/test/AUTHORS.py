import pandas as pd


file = r"C:\test\train\HEAD.csv"
df = pd.read_csv(file, usecols=["author_name"]).drop_duplicates()
df.to_csv(r'C:\test\train\AUTHORS.CSV', index=False)