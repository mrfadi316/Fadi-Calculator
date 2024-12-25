
from colorama import init, Fore, Style

# Initialize colorama
init()

# Calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Physics functions
def calculate_force(mass, acceleration):
    # Formula: F = ma
    force = mass * acceleration
    print(Fore.YELLOW + f"Using the formula: F = m * a\nWhere: m = {mass} kg, a = {acceleration} m/s²")
    return force

def calculate_velocity(initial_velocity, acceleration, time):
    # Formula: v = u + at
    velocity = initial_velocity + (acceleration * time)
    print(Fore.YELLOW + f"Using the formula: v = u + at\nWhere: u = {initial_velocity} m/s, a = {acceleration} m/s², t = {time} s")
    return velocity

def calculate_kinetic_energy(mass, velocity):
    # Formula: KE = 0.5 * m * v²
    kinetic_energy = 0.5 * mass * velocity**2
    print(Fore.YELLOW + f"Using the formula: KE = 0.5 * m * v²\nWhere: m = {mass} kg, v = {velocity} m/s")
    return kinetic_energy

def calculate_gravitational_force(mass1, mass2, distance):
    # Formula: F = G * (m1 * m2) / r²
    G = 6.67430 * 10**-11  # Universal Gravitational Constant
    force = G * (mass1 * mass2) / distance**2
    print(Fore.YELLOW + f"Using the formula: F = G * (m1 * m2) / r²\nWhere: m1 = {mass1} kg, m2 = {mass2} kg, r = {distance} m")
    return force

# Function to print the ASCII art header with "FADI"
def print_header():
    print(Fore.CYAN + """
  █████▒▄▄▄      ▓█████▄  ██▓
▓██   ▒▒████▄    ▒██▀ ██▌▓██▒
▒████ ░▒██  ▀█▄  ░██   █▌▒██▒
░▓█▒  ░░██▄▄▄▄██ ░▓█▄   ▌░██░
░▒█░    ▓█   ▓██▒░▒████▓ ░██░
 ▒ ░    ▒▒   ▓▒█░ ▒▒▓  ▒ ░▓  
 ░       ▒   ▒▒ ░ ░ ▒  ▒  ▒ ░
 ░ ░     ░   ▒    ░ ░  ░  ▒ ░
             ░  ░   ░     ░  
                  ░           
    """ + Style.RESET_ALL)

# Function to print the welcome message
def print_welcome_message():
    print(Fore.GREEN + "=" * 40)
    print("         Welcome to FADI CALCULATOR")
    print("=" * 40)
    print("Select an operation to perform:")

# Function to print footer with a thank you note
def print_footer():
    print(Fore.GREEN + "=" * 40)
    print("   Thank you for using FADI CALCULATOR!")
    print("=" * 40 + Style.RESET_ALL)

# Function to display options clearly
def print_operations():
    print(Fore.YELLOW + "\n==================== Operations ====================" + Style.RESET_ALL)
    print(Fore.YELLOW + "1. Add" + Style.RESET_ALL)
    print(Fore.YELLOW + "2. Subtract" + Style.RESET_ALL)
    print(Fore.YELLOW + "3. Multiply" + Style.RESET_ALL)
    print(Fore.YELLOW + "4. Divide" + Style.RESET_ALL)
    print(Fore.YELLOW + "5. Physics Calculations" + Style.RESET_ALL)
    print(Fore.MAGENTA + "6. Exit" + Style.RESET_ALL)
    print(Fore.YELLOW + "=====================================================" + Style.RESET_ALL)

# Function to display physics options
def print_physics_operations():
    print(Fore.YELLOW + "\n==================== Physics Operations ====================" + Style.RESET_ALL)
    print(Fore.YELLOW + "1. Calculate Force (F = ma)" + Style.RESET_ALL)
    print(Fore.YELLOW + "2. Calculate Velocity (v = u + at)" + Style.RESET_ALL)
    print(Fore.YELLOW + "3. Calculate Kinetic Energy (KE = 0.5 * m * v²)" + Style.RESET_ALL)
    print(Fore.YELLOW + "4. Calculate Gravitational Force (F = G * (m1 * m2) / r²)" + Style.RESET_ALL)
    print(Fore.MAGENTA + "5. Back to Main Menu" + Style.RESET_ALL)
    print(Fore.YELLOW + "=====================================================" + Style.RESET_ALL)

# Display the header
print_header()

# Display the welcome message
print_welcome_message()

# Main loop for user input and calculation
while True:
    # Display available operations
    print_operations()

    # Prompt for the user's choice
    choice = input(Fore.CYAN + "\nEnter choice (1/2/3/4/5/6): " + Style.RESET_ALL)

    # Process the user's choice
    if choice in ['1', '2', '3', '4']:
        try:
            # Get the two numbers from the user
            num1 = float(input(Fore.CYAN + "Enter the first number: " + Style.RESET_ALL))
            num2 = float(input(Fore.CYAN + "Enter the second number: " + Style.RESET_ALL))

            # Perform the selected operation
            if choice == '1':
                result = add(num1, num2)
                operation = "Addition"
            elif choice == '2':
                result = subtract(num1, num2)
                operation = "Subtraction"
            elif choice == '3':
                result = multiply(num1, num2)
                operation = "Multiplication"
            elif choice == '4':
                result = divide(num1, num2)
                operation = "Division"

            # Display the result with a consistent format
            print(Fore.GREEN + f"\n{operation} Result: {result}\n" + Style.RESET_ALL)

        except ValueError:
            print(Fore.RED + "\nError: Please enter valid numbers.\n" + Style.RESET_ALL)

    elif choice == '5':
        # Physics calculations
        while True:
            print_physics_operations()
            physics_choice = input(Fore.CYAN + "\nEnter physics choice (1/2/3/4/5): " + Style.RESET_ALL)

            if physics_choice == '1':
                mass = float(input(Fore.CYAN + "Enter mass (kg): " + Style.RESET_ALL))
                acceleration = float(input(Fore.CYAN + "Enter acceleration (m/s²): " + Style.RESET_ALL))
                result = calculate_force(mass, acceleration)
                print(Fore.GREEN + f"\nForce (F = ma) Result: {result} N\n" + Style.RESET_ALL)

            elif physics_choice == '2':
                initial_velocity = float(input(Fore.CYAN + "Enter initial velocity (m/s): " + Style.RESET_ALL))
                acceleration = float(input(Fore.CYAN + "Enter acceleration (m/s²): " + Style.RESET_ALL))
                time = float(input(Fore.CYAN + "Enter time (s): " + Style.RESET_ALL))
                result = calculate_velocity(initial_velocity, acceleration, time)
                print(Fore.GREEN + f"\nVelocity (v = u + at) Result: {result} m/s\n" + Style.RESET_ALL)

            elif physics_choice == '3':
                mass = float(input(Fore.CYAN + "Enter mass (kg): " + Style.RESET_ALL))
                velocity = float(input(Fore.CYAN + "Enter velocity (m/s): " + Style.RESET_ALL))
                result = calculate_kinetic_energy(mass, velocity)
                print(Fore.GREEN + f"\nKinetic Energy (KE = 0.5 * m * v²) Result: {result} J\n" + Style.RESET_ALL)

            elif physics_choice == '4':
                mass1 = float(input(Fore.CYAN + "Enter mass1 (kg): " + Style.RESET_ALL))
                mass2 = float(input(Fore.CYAN + "Enter mass2 (kg): " + Style.RESET_ALL))
                distance = float(input(Fore.CYAN + "Enter distance between masses (m): " + Style.RESET_ALL))
                result = calculate_gravitational_force(mass1, mass2, distance)
                print(Fore.GREEN + f"\nGravitational Force (F = G * (m1 * m2) / r²) Result: {result} N\n" + Style.RESET_ALL)

            elif physics_choice == '5':
                break  # Back to main menu

            else:
                print(Fore.RED + "\nInvalid input! Please choose a valid option.\n" + Style.RESET_ALL)

    elif choice == '6':
        # If the user chooses to exit, print a thank you message and exit
        print(Fore.CYAN + "\nExiting FADI Calculator... Goodbye!\n" + Style.RESET_ALL)
        print_footer()  # Print footer
        break

    else:
        # Handle invalid input choice
        print(Fore.RED + "\nInvalid input! Please choose a valid option.\n" + Style.RESET_ALL)
