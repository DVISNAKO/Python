numbers = [3, 7, 1, 9, 4]
## delete 1 
## add 10

numbers.remove(1)
print(numbers)

numbers.append(10)
print(numbers)

## ✔ Сделай все буквы заглавными
## ✔ Раздели строку по пробелам в список
## ✔ Выведи длину строки

text = "Python is awesome" 

text.upper()
print(text)

words = text.split()
print(words)


text_length = len(text)
print(text_length)

#✔ Добавь ключ "job" со значением "QA"
#✔ Увеличь возраст на 1
#✔ Удали ключ "city"

user = {
    "name": "Bob",
    "age": 25,
    "city": "Riga"
}

user['job'] = "QA"
user["age"] += 1
del user["city"]

print(user)

print(abs(3.5 - 10))
