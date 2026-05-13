
# 1. Generator
# def generator(a):
#     y = a
#     y += 2
#     yield y

#     y *= 5
#     yield y

#     y /= 2
#     yield int(y)

# natija = generator(10)
# print(next(natija))
# print(next(natija))
# print(next(natija))


# 2.Iterator 

# l = [1, "salom", "Xayr"]
# l2 = iter(l)

# print(type(l))
# print(type(l2))
# print(l2)
# print(next(l2))
# print(next(l2))


# 3.Generator va for sikli:

# def generator_sikl(a,b):
#     for i in range(a,b):
#         yield i*2

# natija2 = generator_sikl(5,10)
# item = list(it for it in natija2)
# print(item)

# 4. Anonim generator

# mening_generatorim = (q for q in range(1,10))
# print(mening_generatorim)
# last_answer = list(i for i in mening_generatorim)
# print(last_answer)


# 5. Just For Information

# def prime_generator():
#     def is_prime(number):
#         if number < 2:
#             return False
#         for i in range(2, int(number**0.5) + 1):
#             if number % i == 0:
#                 return False
#         return True

#     number = 2
#     while True:
#         if is_prime(number):
#             yield number
#         number += 1

# primes = prime_generator()
# for _ in range(10):
#     print(next(primes))


# 6. Just For Information

# import itertools

# def password_generator(input_string):
#     for pwd in itertools.permutations(input_string):
#         yield '-'.join(pwd)

# input_string = "asb"
# passwords = password_generator(input_string)
# for _ in range(6):
#     print(next(passwords))

# 7. Juft sonlarni topish.

# def juft_sonlar_fabrikasi():
#     son = 2
#     while True:
#         yield son 
#         son += 2  


# generator_obj = juft_sonlar_fabrikasi()


# sanoq = 0 

# for j in generator_obj:
#     print(j) 
#     sanoq += 1 
    
    
#     if sanoq == 10:
#         break


# 8.Fibanachi sonlar

# def fibonacci_generator():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b

# fibonacci = fibonacci_generator()
# for _ in range(10):
#     print(next(fibonacci))