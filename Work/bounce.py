# bounce.py
#
# Exercise 1.5

start = 100

for i in range(1, 11):
    start *= 0.6
    print(f"{i:>2} {start:>8.4f}")
