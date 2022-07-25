def prime_checker(number):
        for i in range(2, number//2):
            if (number % i) == 0:
                print("It's not a prime number.")
                break
            else:
                print("It's a prime number.")
                break
n = int(input("Check this number: "))
prime_checker(number=n)
