# python function can return multiple values together.
# other language like C,C++ or Java needs  a class or structure for the same reason.

def add_multiply(a, b):
    sum = a+b;
    product = a*b
    return sum, product

m, n = add_multiply(10, 20)
print("m: "  +str(m) + " n: " + str(n))
