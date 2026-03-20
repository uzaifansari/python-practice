PRIME OR NOT
import math
n = 11

prime = True
if n < 2:
    prime = False
elif n == 2:
    prime = True
elif n>2:
    for i in range(2, int(math.sqrt(n)) + 1):
        if n%i == 0:
            prime = False
            break

print(prime)
