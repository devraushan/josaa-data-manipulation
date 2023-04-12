from math import nan
import sys
import pandas as pd
df1 = pd.read_csv("anskey.csv")
df1.dropna(inplace = True)

testerdf = df1.iloc[:,[2,3]]
df2 = pd.read_csv('answers.csv')
testeedf = df2.iloc[:,[0,1]]
trueCounter = 0
falseCounter = 0
for a in range(0,89):
    for b in range(0,89):
        if testeedf.iloc[a,0]==testerdf.iloc[b,0]:
            if(testeedf.iloc[a,1]==testerdf.iloc[b,1]):
                trueCounter+=1
            elif(testeedf.notnull().iloc[a,1]):
                falseCounter+=1

print("True answers count - "+str(trueCounter))
print("False answers count - "+str(falseCounter))
print("Positive Score - "+str(trueCounter*4))
print("Negative Score - "+str(falseCounter))
print("Total Scores - "+str((trueCounter*4)-falseCounter))