import pandas as pd


file_book = r"C:\test\train\MENTIONED.csv"
file_site = r"C:\test\train\SITE_DATA.CSV"
df_book = pd.read_csv(file_book)
df_site = pd.read_csv(file_site)

df = pd.merge(df_book, df_site, on='description')

df.to_csv(r'C:\test\train\mentioned_authors_title.csv', index=False)

file_mentioned = r'C:\test\train\mentioned_authors_title.csv'
df_mentioned = pd.read_csv(file_mentioned, usecols=["author_name", "meaningful_sentences","url"]).drop_duplicates()
df_mentioned.to_csv(r'C:\test\train\MENTIONED_AUTHORS.CSV', index=False)

