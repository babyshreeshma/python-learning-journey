try:
    x=int(input("Enter a number:"))
    print(x)
except IndentationError:
    print("unexpected indent")

except ValueError:
    print("invalid literal")