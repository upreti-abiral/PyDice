import random

def roll_die(sides=6):
    """Roll a single die with a given number of sides."""
    return random.randint(1, sides)

def roll_multiple_dice(num_dice, sides=6):
    """Roll multiple dice and return the results as a list."""
    return [roll_die(sides) for _ in range(num_dice)]

def main():
    print("🎲 Welcome to Python Dice Roller!")
    print("You can roll dice with any number of sides, as many times as you like.\n")
    
    while True:
        sides_input = input("Enter number of sides per die (or 'q' to quit): ")
        if sides_input.lower() == 'q':
            print("👋 Thanks for rolling! Goodbye!")
            break
        if not sides_input.isdigit() or int(sides_input) < 2:
            print("⚠️ Please enter a valid number (2 or higher).")
            continue
        sides = int(sides_input)
        
        num_input = input("Enter number of dice to roll: ")
        if not num_input.isdigit() or int(num_input) < 1:
            print("⚠️ Please enter a valid number (1 or higher).")
            continue
        num_dice = int(num_input)
        
        results = roll_multiple_dice(num_dice, sides)
        print(f"🎯 Results: {results}")
        print(f"Total: {sum(results)}\n")
        
if __name__ == "__main__":
    main()
