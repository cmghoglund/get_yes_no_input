# Function to get and validate yes/no input from the user

def get_yes_no_input(prompt):
    while True:
        user_choice = input(prompt + " (yes/no): ").lower()
        if user_choice == "yes" or user_choice == "y":
            return True
        elif user_choice == "no" or user_choice == "n":
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
