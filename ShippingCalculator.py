#Exercise 83:Shipping Calculator
n = int(input("Please insert number of items that are being shipped: "))
def ShipCalc(n):
    if n < 1:
        print("Are you not shipping something? You can come back when you are.")
    else:
        C = 10.95 + (n - 1) * 2.95
        print("The Cost of the Shipping is: $" + str(C))
ShipCalc(n)