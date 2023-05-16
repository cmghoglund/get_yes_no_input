# Function to get and validate yes/no input from the user

def get_yes_no_input(prompt):
    while True:
        user_choice = input(f"{prompt} (y/n or yes/no): ").strip().lower()
        if user_choice in ['y', 'yes']:
            return True
        elif user_choice in ['n', 'no']:
            return False
        else:
            print("Please enter a valid response (y/n or yes/no).")
