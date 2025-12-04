#Попроси пользователя ввести возраст.
#Если возраст 18 и больше — вывести "Доступ разрешён",
#иначе — "Доступ запрещён".

age = int(input(("Введите ваш возраст: ")))

if age >= 18:
    print("Доступ разрешён")
else: 
    print("Доступ запрещён")

#2 Есть число n.
#Если число чётное — вывести "even".
#Если нечётное — вывести "odd".

n = int(input("Введите число: "))
if n % 2 == 0:
    print("четное") 
else:
    print("нечетное")

#3 

grade = int(input("Введите ваш балл: "))

if grade == 5:
    print("Отлично")
elif grade == 4:
    print("Хорошо")
elif grade == 3:
    print("Удовлетворительно")
elif grade == 2:
    print("Неудовлетворительно")
else:
    print("Некорректный балл")

#4 

t = int(input("Введите температуру: "))
if t > 30 :
    print("Жарко")
elif t >=20 and t <=30:
    print("Тепло")
elif t >=10 and t <=20:
    print("Прохладно")
else:
    print("Холодно")

#5

login = "admin"
password = "1234"

input_login = input("Введите логин: ")
input_password = input("Введите пароль: ")

if input_login == login and input_password == password:
    print("Доступ разрешён")
else:
    print("Доступ запрещён")

#6

first_num = int(input("Введите первое число: "))
second_num = int(input("Введите второе число: "))

if first_num > second_num:
    print(first_num)
elif second_num > first_num:
    print(second_num)

#7 
str_leng = str(input("Введите строку: "))

if len(str_leng) > 10:
    print("Длинная строка")
else:
    print("Короткая строка")