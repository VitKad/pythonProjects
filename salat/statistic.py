import matplotlib.pyplot as plt


#words = [buf+1]*32
#text = "ааАаабббввгдетЯы!,№%эюя"



def calculateStatistic(text):
    buf=1072
    words = [0] * 32
    statistic = [0] * 32
    percents = [0] * 32
    for i in range(0, 32):
        words[i]=chr(buf)
        buf+=1

    for i in text:
        if (ord(i)>=1040 and ord(i)<=1103):
            if (ord(i)>=1040 and ord(i)<=1071):
                statistic[ord(i)-1040]+=1
            else:
                statistic[ord(i)-1072]+=1

    count = 0
    for i in range(0,32):
        count+=statistic[i]

    for i in range(0, 32):
        percents[i]=(statistic[i]/count)*100

    for i in range(31):
        for j in range(31-i):
            if statistic[j] < statistic[j+1]:
                statistic[j], statistic[j+1] = statistic[j+1], statistic[j]
                words[j], words[j+1] = words[j+1], words[j]
                percents[j], percents[j+1] = percents[j+1], percents[j]


    plt.subplot(1, 2, 1)
    plt.bar(words, statistic)
    plt.title("Частотный анализ зашифрованного текста")
    plt.xlabel("Буквы")
    plt.ylabel("Количество")
    #plt.show()

    plt.subplot(1, 2, 2)
    plt.title('Частотный анализ в процентах')
    plt.pie(percents,labels=words)
    plt.axis('equal')
    plt.show()

   # print(statistic)
   # print(words)
   # print(percents)

    return statistic, words;

with open('task.txt') as f:
    text = f.read()

statText, wordsText = calculateStatistic(text)

with open('example.txt') as f:
    example = f.read()

statExamp, wordsExamp = calculateStatistic(example)

print(statText)
print(wordsText)
print("Буквы, которые повторяются чаще всего")
print("Для зашифрованного текста:", wordsText[0], " - ", statText[0], ", ", wordsText[1], " - ", statText[1], ", ", wordsText[2], " - ", statText[2], ". ")
print("Для обычного текста:", wordsExamp[0], " - ", statExamp[0], ", ", wordsExamp[1], " - ", statExamp[1], ", ", wordsExamp[2], " - ", statExamp[2], ". ")
print("Предпологаемый ключ: ", ord(wordsText[0])-ord(wordsExamp[0]), ', ',ord(wordsText[1])-ord(wordsExamp[1]), ', ',ord(wordsText[2])-ord(wordsExamp[2]))