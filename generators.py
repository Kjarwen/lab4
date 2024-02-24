#ex1
def square_generator(n):
    for i in range(1, n + 1):
        yield i ** 2
n = int(input())
squares = square_generator(n)

for x in squares:
    print(x)

#ex2
def even_nums(n):
    for i in range(0, n+1):
        if i % 2 == 0:
            continue
        else:
            yield i
n = int(input())
even = even_nums(n)

for x in even:
    print(x)

#ex3 
def div_by_3_and_4(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
n = int(input())
div = div_by_3_and_4(n)

for x in div:
    print(x)

#ex4
def squares(a,b):
    for i in range(a, b+1):
        yield i*i
a = int(input())        
b = int(input())  
square = squares(a,b)
for x in square:
    print(x)

#ex5
def from_n_to_0(n):
   while n >= 0:
        yield n
        n -= 1
n = int(input())
for x in from_n_to_0(n):
    print(x)