# TASK 1: Create variables for a student profile
# Create: name (string), student_id (integer), gpa (float), 
# is_enrolled (boolean), courses (list)
# Then print each variable and its type

name = 'Dima'
student_id = 4217
gpa = 3.8
is_enrolled = True
courses_list = ['Sport', 'Art', 'Math']
print(name, type(name))


# TASK 2: Work with a tuple and list
# Create a tuple with 3 coordinates (x, y, z)
# Create a list with the same values
# Try to modify the tuple (it should fail)
# Modify the list successfully

# coordinates = (x, y, z)
my_list = ['123', '456', '789']
my_list[1] = '7777'
my_list.append('32')
print(my_list)


# TASK 3: Create a dictionary for a product
# Keys: name, price, in_stock, quantity, tags (set)
# Print all values and their types

products = {'name': 'Laptop', 'price': 999.99, 'in_stock': True, 'quantity': 50, 'tags': {'electronics', 'computer'}}
print(products, type(products))


# TASK 4: Type conversion
# Convert string "123" to integer
# Convert integer 42 to string
# Convert string "3.14" to float
# Convert integer 1 to boolean

my_str = '123'
my_str = 124
print(my_str, type(my_str))

num = 77
num = str(num)
print(num, type(num))

num2 = 555
num2 = bool(num2)
print(num2, type(num2))


# TASK 5: Create a user profile with all variable types
# Combine all types into one dictionary representing a user
# Print the profile nicely

user_name = 'Dima'
user_id = 4217
user_gpa = 3.8
user_is_enrolled = True
user_courses = ['Sport', 'Art', 'Math']

user_profile = {
    'name': user_name,
    'student_id': user_id,
    'gpa': user_gpa,
    'is_enrolled': user_is_enrolled,
    'courses': user_courses
}

print(f"User Profile: {user_profile}")