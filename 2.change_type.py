#1. Преобразуй строку "1234" в число и прибавь 10.
num = "1234"
num_int = int(num)
result = num_int + 10
print(result)

result_2 = int('1234') + 10
print(result_2)

#2. Дана строка "3.14". Преобразуй её в float и умножь на 2.

str_1 = "3.14"
result_float = float(str_1) * 2
print(result_float)

#3. Преобразуй число 7 в строку, добавь к нему " apples" и выведи результат.
result_apples = str(7) + " apples"
print(result_apples)

#4. Преобразуй список [1, 2, 3] в кортеж.
my_list = [1,2,3] 
my_typle = tuple(my_list)
print(my_typle)

result = tuple([3,2,1])
print(result)