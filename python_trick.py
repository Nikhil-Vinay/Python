# 1. Swap two variables are easy
a = 20
b = 10
a, b = b, a
print("a is " + str(a) + " b is " + str(b))

# 2. min and max
l = [10, 5, 20, 50, 6]
min_num = min(l)
max_num = max(l)
print (min_num, max_num)

# 3. store even/odd of a range in a list, it can be applied in any ways
even = [x for x in range (20) if x%2 == 0]
print even
odd = [x for x in range(10, 20) if x%2 == 1]
print odd

# 4. use of map, filter and reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
           11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def square(x):
    return x*x

def even(x):
    return (x%2 == 0)

def odd(x):
    return (x%2 == 1)

squares = list(map(square, numbers))
print squares

evens = list(filter(even, numbers))
print(evens)

def multiply(a, b):
    return a * b

numbers = [1, 5, 6, 4]
product = reduce(multiply, numbers)
print(product)

# 5. use of lambda function
print ("Using Lambda")

squares = list(map(lambda x: x**2, numbers))
print(squares)

evens = list(filter(lambda x: x%2 == 0, numbers))
print(evens)

product = reduce(lambda x, y: (x*y), numbers)
print(product)

# we can define lambda function outside also
lambda_func = lambda x: x**2
squares = list(map(lambda_func, numbers))
print(squares)

