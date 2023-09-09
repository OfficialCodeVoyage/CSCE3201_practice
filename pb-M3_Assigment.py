import random 

while True:

    while True: 
        try:
            range_select_lower = int(input("Enter Lower Bound: "))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
            
    while True: 
        try:
            range_select_upper = int(input("Enter Upper Bound: "))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
    
    if range_select_lower > range_select_upper: 
        print("OOPss. Your Lower Bound can't be hiegher than Upper Bound!\nTry Again!")
        continue
    else: break        
        
             
while True: 
    try:
        remaining_guesses = int(input("Enter Maximum Number of Guesses:"))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")


number_to_guess = random.randint(range_select_lower,range_select_upper) # Number to guess
count_of_attemts = 0 # using for promt messages only
print(f"You only have {remaining_guesses} chances to guess the integer between {range_select_lower} and {range_select_upper}!\nGood luck!")


while True:
    
    if remaining_guesses > 0:   
        try:  
            user_input_to_guees_number = int(input("Guess the number: "))
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
            
        if user_input_to_guees_number == number_to_guess:
            count_of_attemts+=1
            print(f"Congratulation, You did in {count_of_attemts} tries!")
            break
        elif user_input_to_guees_number > number_to_guess:
            count_of_attemts+=1
            remaining_guesses -=1
            print(f'You guessed too high!  Attempts left : {remaining_guesses}')
        elif user_input_to_guees_number < number_to_guess:
            count_of_attemts+=1
            remaining_guesses -=1
            print(f'You guessed to small. Attempts left : {remaining_guesses}')
    elif remaining_guesses == 0: 
        print(f"You were not able to guess the number!\nNumber to guees was - {number_to_guess}!\nGood luck next time!")
        break
    

    
