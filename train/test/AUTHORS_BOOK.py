import pandas as pd


file = r"C:\test\train\HEAD.csv"
df = pd.read_csv(file, usecols=["title", "author_name", "number"]).drop_duplicates()
df.to_csv(r'C:\test\train\BOOK_AUTHORS.CSV', index=False)