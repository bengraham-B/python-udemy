def is_prime(num):
    # If the number is negative, zero or one it will return false
    if num <= 1:
        return False
    
    # This will check the range from 2 onwards to half the number provided by the user
    for n in range(2, int(num/2) + 1):
        if num % n == 0: # If the remainder is zero it means that there is another which the user num can be divided by- menaing it is not a prime number.
            return False
        
        
    else: # If the user's inputed number cannot be divided by a number in the for loop, meaning it is prime, it will return True.
        return True