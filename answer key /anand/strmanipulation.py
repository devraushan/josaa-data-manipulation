data = []
with open('textdata.txt') as my_file:
    for line in my_file:
        data.append(line)

print(data[5])
answers = ""
for i in range(0,len(data)-1):
    # print(data[i])
    if data[i]==data[5]:
        # print(data[i+1][-11:-1]+" "+data[i+7][-2])
        questionId = data[i+1][-11:-1]
        option_no = data[i+7][-2]
        if option_no=='1'or option_no=='2' or option_no=='3'or option_no=='4':
            optionId = data[i+1+int(option_no)][-11:-1]
            answers+= questionId+","+optionId+"\n"
            # print(questionId +"," +optionId)
        else:
            answers+=questionId+"\n"
            # print(optionId)
    elif data[i]==data[300]:
        questionId = data[i+1][-11:-1]        
        if data[i-1]!=data[306]:
            ans = data[i-1]
            answers+= questionId+","+ans
        else:
            answers+=questionId+"\n"
        
file1 = open('answers.csv','w')
file1.write(answers)
file1.close()