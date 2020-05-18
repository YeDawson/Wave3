#Exercise 92:Is a Number Prime?
n = int(input("Please input an integer larger than 1: "))
print("This number is a Prime?")
if n <= 1:
    print("Error, please insert valid value")
else:
    for i in range(2, n):
        if (n % i) == 0:
            print("False")
            break
    else:
            print("True")