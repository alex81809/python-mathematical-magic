print("2-Digit Prime Numbers (10 to 99):")
print("-" * 30)

for num in range(10, 100):
    is_prime = True  
    
    # Check for divisors from 2 up to the number itself
    for i in range(2, num):
        if (num % i) == 0:
            is_prime = False  # Found a divisor, so it's NOT prime
            break             # No need to keep checking this number
            
    # If it survived the loop without is_prime becoming False, it's a winner!
    if is_prime:
        print(num, end=" ")
