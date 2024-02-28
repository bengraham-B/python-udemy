import math

for n in range(1, 20):
    print(str(n) + " " + str(math.sqrt(n)))
    
def is_prime(num):
    if num <= 1:
        return False
    
    for n in range(2, int(math.sqrt(num + 1))):
        if num % n == 0: # If the remainder is zero it means that there is another which the user num can be divided by- menaing it is not a prime number.
            return False
        
    else: # If the user's inputed number cannot be divided by a number in the for loop, meaning it is prime, it will return True.
        return True