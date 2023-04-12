import pandas as pd
table = pd.read_html("index.html")
print(table[0])
table[0].to_csv("key.csv")