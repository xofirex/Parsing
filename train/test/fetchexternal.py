import pandas as pd

#


file = r"https://raw.githubusercontent.com/bigsnarfdude/guide-to-data-mining/master/BX-Dump/BX-Books.csv"
df = pd.read_csv(file, sep='";"', engine="python")
df.to_csv (r'C:\test\train\train.csv', index = False)
