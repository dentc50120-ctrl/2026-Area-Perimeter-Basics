# ask user for width and loop until they
# enter a number that is more than zero
from Tools.scripts.generate_global_objects import Printer

def num_check(question):

    error = "Please enter a number that is more than zero\n"
    while True:

        try:
            # ask the user for a number
            response = float(input(question))

            # check that the number is more than zero
            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

# Main Routine starts here...

keep_going = ""
while keep_going == "":
    # Get width and height
    width = num_check("width: ")
    height = num_check("height: ")
    cost = num_check("cost: ")

    # Calculate perimeter and price for the fence
    perimeter = 2 * (width + height)
    price = (perimeter * cost)


    # Display output
    print()
    print(f"perimeter: {perimeter} units")
    print(f"price: ${price:.2f}")

    # Ask user if they want to keep going
    keep_going = input("Press enter to keep going or any key to quit. ")
    print()

print("Thank you for using the fence cost calculator")