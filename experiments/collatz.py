import random
import time
def collatz(x):
    while x != 1:
        print(x)
        if (x % 2) == 0:
            x = x/2
            x = int(x)
        else:
            x = (3*x)+1
            x = int(x)
    else:
        print(f'End of Pattern: Loop Created (4-2-1-4) | {x} follows the Collatz Conjecture')

print("This program is to be used to validate or disprove the Collatz Conjecture.")
j = input("Generate a random number? (y/n)")
if j.lower() == 'y':
    x = random.randint(1,999999999999999999999)
    print(f"The random number chosen is {x}")
    time.sleep(2)
    collatz(x)
elif j.lower() == 'n':
    val = int(input('Enter a Number: '))
    collatz(val)
