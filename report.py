import pandas as pd
table = pd.read_html("rowdata.html")
table[-1].to_csv("round6.csv")