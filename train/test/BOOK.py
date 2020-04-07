import pandas as pd


file = r"C:\test\train\HEAD.csv"
df = pd.read_csv(file, usecols=["title", "number" , "year", "univ_name", "image1", "image2", "image3"]).drop_duplicates()
df.to_csv(r'C:\test\train\BOOK.CSV', index=False)
