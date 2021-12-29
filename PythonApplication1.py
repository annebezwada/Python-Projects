print("******************************************************************************")
print("Welcome to my program!")
name = input("Please write your name here: ")
print("Welcome, " + name + "!")

numa = float(input("Please enter a number: "))
numb = float(input("Please enter a second number: "))
operation = input("Do you want to add, subtract, multiply or divide? Use 'a', 's', 'm', 'd' to select: ")
print("You chose: " + operation + ".")
if (operation == 'a'):
    sum = numa + numb
    print("This equals to:", sum, ".")
elif (operation == 's'):
    difference = numa - numb
    print("This equals to:", difference, ".")
elif (operation == 'm'):
    product = numa * numb
    print("This equals to:", product, ".")
elif (operation == 'd'):
    divend = numa / numb
    print("This equals to:", divend, ".") 
elif(operation != 'a', 's', 'm', 'd'):
    print("That is not an option. Goodbye!")


print("******************************************************************************")


print("Thank you for using my calculator program!")
print("Created by: Anne B.")


