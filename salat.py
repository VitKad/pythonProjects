newNumber = 0
result = ""
print("Введите ключ")

while True:
    key = input()  # Ввод числа
    if (key.isdigit()) : break

#key = int(input())
key = int(key)
print("Введите строку")
text = input()
print("Введите функцию: 1-кодировать, 2-раскодировать")
while True:
    operation = input()  # Ввод числа
    if ((operation.isdigit()) and ((operation == "1") or (operation == "2") )) : break
operation= int(operation)

if (ord(text[0])>=1040 and ord(text[0])<=1103):
    while (key>32):
        key-=32

if (ord(text[0])>=65 and ord(text[0])<=122):
    while (key>26):
        key-=26


if (ord(text[0])>=1040 and ord(text[0])<=1071):
    for i in text:
        if (operation == 1) :
            newNumber = ord(i)+key
            if (newNumber>1071): newNumber-=32
        if (operation == 2):
            newNumber = ord(i) - key
            if (newNumber < 1040): newNumber += 32
        if (32<=ord(i)<=48): newNumber = ord(i)
        result=result+chr(newNumber)


if (ord(text[0])>=1072 and ord(text[0])<=1103):
    for i in text:
        if (operation == 1):
            newNumber = ord(i)+key
            if (newNumber>1103): newNumber-=32
        if (operation == 2):
            newNumber = ord(i) - key
            if (newNumber < 1072): newNumber += 32
        if (32 <= ord(i) <= 48): newNumber = ord(i)
        result=result+chr(newNumber)

if (ord(text[0])>=65 and ord(text[0])<=90):
    for i in text:
        if (operation == 1):
            newNumber = ord(i)+key
            if (newNumber>90): newNumber-=26
        if (operation == 2):
            newNumber = ord(i) - key
            if (newNumber < 65): newNumber += 26
        if (32 <= ord(i) <= 48): newNumber = ord(i)
        result=result+chr(newNumber)


if (ord(text[0])>=97 and ord(text[0])<=122):
    for i in text:
        if (operation == 1):
            newNumber = ord(i)+key
            if (newNumber>122): newNumber-=26
        if (operation == 2):
            newNumber = ord(i) - key
            if (newNumber < 97): newNumber += 26
        if (32<=ord(i)<=48): newNumber = ord(i)
        result=result+chr(newNumber)

if (result == ""): print("Введены неверные данные")
else:
    print("Начальная строка: ", text)
    print("Полученный результат при ключе равном ", key, " :", result)