
import random

N = int(input("Anna pisteiden kokonaismäärä: "))
pisteet = 0
n = 0
while pisteet <= N:
    pisteet = pisteet + 1
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    if x**2+y**2<1:
         n = n + 1

Pi = 4*n/N
print(f"Piin likiarvo on : {Pi}")
