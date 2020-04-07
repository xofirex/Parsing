import pandas as pd

#


file = r"C:\test\train\train.csv"
df = pd.read_csv(file, names=["number", "title", "author_name", "year", "univ_name", "image1", "image2", "image3"])
df.to_csv(r'C:\test\train\HEAD.csv', index=False)
