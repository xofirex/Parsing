import pandas as pd


file_book = r"C:\test\train\BOOK_AUTHORS.CSV"
file_site = r"C:\test\train\SITE_DATA.CSV"
df_book = pd.read_csv(file_book)
df_site = pd.read_csv(file_site)

df = pd.merge(df_site, df_book, on='title', how='left').drop_duplicates()

df.to_csv(r'C:\test\train\NEW_MEN.csv', index=False)
