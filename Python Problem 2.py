operations = ["add", "subtract", "multiply", "divide"]
results = []


def elderberries():
    while True:
        print("Please choose from the following operations:")
        for i in range(len(operations)):
            print(f"{i+1}. {operations[i]}")
        try:
            choice = int(input("Which choice would you like?: "))
            if 1 <= choice <= len(operations):
                return choice
            else:
                print("Invalid choice, please select a numer from 1 to 4")
        except ValueError:
            print("Please enter a valid number")           

def answer(choice, num1, num2):

        if choice == 1:
            result = num1 + num2
            problem = f"{num1} + {num2} = {result}"
        elif choice == 2:
            result = num1 - num2
            problem = f"{num1} - {num2} = {result}"
        elif choice == 3:
            result = num1 * num2
            problem = f"{num1} * {num2} = {result}"
        elif choice == 4:
            try:
                result = num1 / num2
                problem = f"{num1} / {num2} = {result}"
            except ZeroDivisionError:
                print("You cant divide by 0 doofus.")
                return
        print("Your number is:", result)
        results.append(problem)
        return
            




while True:
    choice = elderberries()

    print(f"And which two numbers would you like to {operations[choice - 1]} together?")

    num1 = int(input("Please input your first number: "))
    num2 = int(input("Please input your second number: "))

    answer(choice, num1, num2)

    again = input("Would you like to run the calc again?(Y/N): ").lower()
    if again in ["y", "yes"]:
        continue
    elif again in ["n", "no"]:
        print("Live Long and Prosper 🖖. BTW, Here are your calculations from today:")
        for r in results:
            print(r)
        break
    else:
        print("Hmmmm... doesnt look like a Y or N to me.")






