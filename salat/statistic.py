import matplotlib.pyplot as plt

def calculateStatistic(text, c):    #функция расчета частотного анализа
    buf=1072
    words = [0] * 32       #сооздание пустых массивов
    statistic = [0] * 32
    percents = [0] * 32
    for i in range(0, 32):   #цикл заполнения массива алфавита
        words[i]=chr(buf)
        buf+=1

    for i in text:       #цикл подсчета букв в тексте
        if (ord(i)>=1040 and ord(i)<=1103):
            if (ord(i)>=1040 and ord(i)<=1071):
                statistic[ord(i)-1040]+=1
            else:
                statistic[ord(i)-1072]+=1

    count = 0
    for i in range(0,32):    #подсчет количества букв в целом
        count+=statistic[i]

    for i in range(0, 32):     #заполнение массива с процентами
        percents[i]=(statistic[i]/count)*100

    for i in range(31):    #сортировка всех массивов
        for j in range(31-i):
            if statistic[j] < statistic[j+1]:
                statistic[j], statistic[j+1] = statistic[j+1], statistic[j]
                words[j], words[j+1] = words[j+1], words[j]
                percents[j], percents[j+1] = percents[j+1], percents[j]

    plt.figure(num='Частотный анализ', figsize=(16, 8))
    plt.subplot(1, 2, 1)  #столбики
    plt.bar(words, statistic)
    if (c==1):
        plt.title("Частотный анализ зашифрованного текста")
    if (c==2):
        plt.title("Частотный анализ текста из интернета")
    plt.xlabel("Буквы")
    plt.ylabel("Количество")

    plt.subplot(1, 2, 2)  #круговая
    plt.title('Частотный анализ в процентах')
    plt.pie(percents,labels=words, autopct='%1.0f%%', pctdistance=1.1, labeldistance=1.2)
    plt.axis('equal')


    plt.show()

    return statistic, words, percents;

with open('task.txt') as f:
    text = f.read()

statText, wordsText, percentText = calculateStatistic(text, 1)

with open('example.txt') as f:
    example = f.read()

statExamp, wordsExamp, percentExamp = calculateStatistic(example, 2)


print("Количество букв, которые повторяются чаще всего")
print("Для зашифрованного текста:", wordsText[0], " - ", statText[0], "(", float('{:.3f}'.format(percentText[0])), "% ) ",
      ", ", wordsText[1], " - ", statText[1],"(", float('{:.3f}'.format(percentText[1])), "% ) ",
      ", ", wordsText[2], " - ", statText[2],"(", float('{:.3f}'.format(percentText[2])), "% ) ", ". ")
print("Для обычного текста:", wordsExamp[0], " - ", statExamp[0],"(", float('{:.3f}'.format(percentExamp[0])), "% ) ",
      ", ", wordsExamp[1], " - ", statExamp[1], "(", float('{:.3f}'.format(percentExamp[1])), "% ) ",
      ", ", wordsExamp[2], " - ", statExamp[2], "(", float('{:.3f}'.format(percentExamp[2])), "% ) ",". ")
print("Предпологаемые ключи: ", ord(wordsText[0])-ord(wordsExamp[0]), ', ',ord(wordsText[1])-ord(wordsExamp[1]), ', ',ord(wordsText[2])-ord(wordsExamp[2]))