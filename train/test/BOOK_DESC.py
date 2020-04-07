import pandas as pd


file_book = r"C:\test\train\BOOK.CSV"
file_site = r"C:\test\train\SITE_DATA.CSV"
df_book = pd.read_csv(file_book)
df_site = pd.read_csv(file_site)

df = pd.merge(df_book, df_site, on='title', how='left')

df.to_csv(r'C:\test\train\BOOKDES.csv', index=False)

df_desc = pd.read_csv(r'C:\test\train\BOOKDES.csv', usecols=["title", "description", "number"])

df_desc.to_csv(r'C:\test\train\BOOK_DESCRIPTION.CSV', index=False)