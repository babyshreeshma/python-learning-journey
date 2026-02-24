#exception

try:
    x=int(input("Enter a number:"))
    print(x)
except:
    print("Invalid input")

#multiple exception

try:
        a=int(input("A: "))
        b=int(input("B: "))
        print(a/b)
except ValueError:
     print("Invalid input")
except ZeroDivisionError:
     print("Can not divide by zero error")