def check_prime(x):
    prime=True
    for i in range(2,x):
        if x%i==0:
            prime=False
    if prime:
        print("it is a prime number")
    else:
        print("it is not a prime number")
number=int(input("enter number to check prime"))
check_prime(number)
