# Assign values for the game:
# 1 for snake, -1 for water, 0 for gun
computer = -1  # Computer chooses water

# Take user input
youstr = input("Enter your choice (s for snake, w for water, g for gun): ")

# Map user input to corresponding values
youDict = {"s": 1, "w": -1, "g": 0}

# Convert user input to game value
you = youDict.get(youstr)

# Check if user input is valid
if you is None:
    print("Invalid input! Please enter 's', 'w', or 'g'.")
else:
    # Compare computer and user choices to decide the winner

    # If both choose the same, it's a tie
    if computer == you:
        print("It's a tie!")while

    # Snake (1) beats Water (-1)
    elif computer == -1 and you == 1:
        print("You win!")  # Snake drinks water

    elif computer == 1 and you == -1:
        print("You lose!")  # Water loses to snake

    # Water (-1) beats Gun (0)
    elif computer == 0 and you == -1:
        print("You win!")  # Water rusts gun

    elif computer == -1 and you == 0:
        print("You lose!")  # Gun loses to water

    # Gun (0) beats Snake (1)
    elif computer == 1 and you == 0:
        print("You win!")  # Gun kills snake

    elif computer == 0 and you == 1:
        print("You lose!")  # Snake loses to gun

    else:
        # This else should never be reached if all cases are covered
        print("Something went wrong!")