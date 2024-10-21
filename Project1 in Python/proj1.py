# # # We all have played snake, water gun game in our childhood.If you haven't google the rules and
# # write the python code capable of playing by user 
# write the code for it 
import random

# Snake, Water, Gun game
def snake_water_gun():
    choices = ["s", "w", "g"]  # Snake, Water, Gun choices
    computer = random.choice(choices)  # Computer randomly selects
    youstr = input("Enter Your Choice(s for Snake, w for Water, g for Gun): ").lower()

    # Dictionary to represent outcomes
    youDict = {"s": 1, "w": -1, "g": 0}
    
    if youstr not in youDict:
        print("Invalid input! Please enter 'snake', 'water', or 'gun'.")
        return
    
    # Map input to numbers
    you = youDict[youstr]
    computer_choice = youDict[computer]

    # Determine the winner
    if you == computer_choice:
        result = "It's a draw!"
    elif (you == 1 and computer_choice == -1) or (you == -1 and computer_choice == 0) or (you == 0 and computer_choice == 1):
        result = "You win!"
    else:
        result = "You lose!"

    # Output the results
    print(f"Your choice: {youstr.upper()}, Computer's choice: {computer.upper()}")
    print(result)

# Run the game
snake_water_gun()
snake_water_gun()
