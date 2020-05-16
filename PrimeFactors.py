#Exercise 76:Prime Factors
n = int(input("Enter an integer (2 or greater) : "))
if n < 2:
    print("Error, please choose integer greater than 2")
else:
    print("The prime factors of " + str(n) , "are:")
    i = 2
    while i <= n :
        if n % i == 0:
            print(i)
            n /= i
        else:
            i += 1
            if n % i == 0:
                n /= i
                print(i)
            else:
                print(int(n))
                break