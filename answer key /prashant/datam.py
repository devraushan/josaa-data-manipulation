from math import nan
import sys
import pandas as pd
df1 = pd.read_csv("answer key /prashant/key.csv")
df1.dropna(inplace = True)
x = df1.get("QuestionID")
print(x)