import pandas as pd



file_site = r"C:\test\train\SITE_DATA.CSV"
file_book = r"C:\test\train\MENTIONED_AUTHORS.CSV"
df_site = pd.read_csv(file_site, usecols=["title", "url"])
df_book = pd.read_csv(file_book, usecols=["author_name", "url"])


df = pd.merge(df_site, df_book, on='url', how='left').drop_duplicates()

df = df[df['author_name'].isnull()]
df.to_csv(r'C:\test\train\MISSING_BOOKS.csv', index=False)