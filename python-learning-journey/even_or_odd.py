#even or odd


number=int(input("Enter a number to check odd or even: "))
if(number%2==0):
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")
print("newly added line")

"""
multiple conditions
"""
mark=int(input("Enter mark: "))
if(mark>=90):
    print("Grade A")
elif(mark>=80 and mark<90):
    print("Grade B")
elif(mark>=70 and mark<60):
    print("Grade C")
else:
    Print("Grade P")