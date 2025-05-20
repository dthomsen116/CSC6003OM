import random

#Print the first lines out of the loop
print("\033[0mWelcome to the Guess the Number Game!")
print("\033[0mI have selected a random number between 1 and 100. Try to guess it!")

# function to make the random num
def generate_random_number():
    return random.randint(1,100)

# function to check the guess
def check_guess(random_number, guess):
    if guess == random_number:
        return "\033[32mCorrect!"
    if guess >= random_number:
        return "\033[31mGuess a Lower Number!"
    else:
        return "\033[31mGuess a Higher Number!"
    
# function to create the extra hint
def extra_hint(random_number):
    hint = random.randint(1,3)
    if hint == 1:
        return("\033[36mThis number is even" if random_number % 2 == 0 else "This number is odd")
    if hint == 2:
        return("\033[36mThis number is a multiple of 5" if random_number % 5 == 0 else "This number is not a multiple of 5")
    if hint == 3:
        return("\033[36mThis number squared is greater than 1,000" if random_number**2 > 1000 else "This number squared is less than 1,000")
    
# Create the main function to loop the guesses and prompt the user

def main():

    # Initializing all of the variables
    random_number = generate_random_number()
    total_attempts = 0
    wrong_answers= 0
    right_ans = False

    # Create the guessing loop (loop only until the answer is correct) 
    while right_ans == False:
        
        # "try" used to catch exceptions for easy error handling
        try:
            # Guess, add an attempt to the counter, then check
            guess = int(input("\033[37mEnter a guess: "))
            total_attempts += 1
            check = check_guess(random_number, guess)

            # If Correct, exit the loop and display the victory message
            if check == "\033[32mCorrect!":
                right_ans = True
                print(f"\033[32mCorrect! You guessed the right number in {total_attempts} tries!\033[0m")
            
            # Else keep guessing, with every second guess providing an extra hint. 
            else:
                wrong_answers += 1
                if wrong_answers % 2 == 0:
                    print(check)
                    print("\033[36mExtra Hint: ", extra_hint(random_number))
                else:
                    print(check)
        # If entry was wrong, this will display this error and continue to loop
        except ValueError:
            print("\033[31mWrong Input. Please try agiain.")    

if __name__ == "__main__":
    main()