def prime_checker(number):
    is_prime = True
    
    for i in range(2, number):
        if number % i  == 0:
            is_prime = False
            
    if is_prime == True:
        return print("Is a prime number")
    
    else:
        return print("Is not a prime number")

    
n = int(input("Enter a number:"))
prime_checker(number=n)