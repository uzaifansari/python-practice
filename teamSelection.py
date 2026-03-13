"""
TEAM SELECTION
TCS NQT Question

Problem Statement:
A company has N employees
The manager needs to form a team of R employees to work on a special project
The order of selection does not matter, only the combination of employees matter.
Find the number of different teams that can be formed.

INPUT:
Two Numbers
N R

OUTPUT:
Print the total number of possible teams

EXAMPLE:

INPUT:
5 2

OUTPUT:
10

EXPLANATION:
Possible Teams:
(1, 2)(1, 3)(1, 4)(1, 5)
(2, 3)(2, 4)(2, 5)
(3, 4)(3, 5)
(4, 5)

"""
n=5
r=2

def get_factorial(N):
    fact=1
    for i in range(0,N):
        fact = fact*(i+1)
    return fact

factorial_n = get_factorial(n)
factorial_r = get_factorial(r)
factorial_nr = get_factorial(n-r)


print(factorial_n // (factorial_r*factorial_nr))