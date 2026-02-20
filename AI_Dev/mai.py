def show_menu():
    print("\n🐍 Python Learning Journey")
    print("1. Day 1 - Variables")
    print("2. Day 2 - Conditions")
    print("3. Exit")


def run_day1():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    print(f"Hi {name}, next year you will be {age + 1} years old")


def run_day2():
    number = int(input("Enter a number: "))

    if number > 0:
        print("Positive number")
    elif number < 0:
        print("Negative number")
    else:
        print("Zero")


while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        run_day1()
    elif choice == "2":
        run_day2()
    elif choice == "3":
        print("Goodbye 👋")
        break
    else:
        print("Invalid choice. Try again.")
