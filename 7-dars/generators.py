import string
import random

def password_creator():
    return "".join(random.sample(string.ascii_letters + string.digits, 8))

def password_generator(num):
    for _ in range(num):
        yield password_creator()

def even_generator(num):
    for i in range(1, num):
        if i % 2 == 0:
            yield i

def odd_generator(num):
    for i in range(1, num):
        if i % 2 == 1:
            yield i
    
def prime_generator(num):
    for i in range(num):
        factors = 0
        for l in range(1, i+1):
            if i % l == 0:
                factors += 1
        if factors == 2:
            yield i

