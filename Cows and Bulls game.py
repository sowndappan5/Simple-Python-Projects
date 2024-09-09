# Import required module 
import random 

# Returns a list of digits from a number 
def extractDigits(number): 
    return [int(digit) for digit in str(number)] 
    

# Returns True if the number has 
# no duplicate digits, otherwise False	 
def hasUniqueDigits(number): 
    digit_list = extractDigits(number) 
    return len(digit_list) == len(set(digit_list))


# Generates a 4-digit number 
# with no repeated digits	 
def createUniqueNumber(): 
    while True: 
        number = random.randint(1000, 9999) 
        if hasUniqueDigits(number): 
            return number 


# Returns the count of exact matches (hits) 
# and the count of common digits in wrong positions (misses) 
def countHitsAndMisses(secret, attempt): 
    hits_misses = [0, 0] 
    secret_digits = extractDigits(secret) 
    attempt_digits = extractDigits(attempt) 
	
    for secret_digit, attempt_digit in zip(secret_digits, attempt_digits): 
		
        # Check for common digit presence 
        if attempt_digit in secret_digits: 
		
            # Check for exact match 
            if attempt_digit == secret_digit: 
                hits_misses[0] += 1
			
            # Count as a common digit match but in wrong position 
            else: 
                hits_misses[1] += 1
				
    return hits_misses 
	
	
# Secret Code 
secret_code = createUniqueNumber() 
attempts = int(input('Enter number of attempts: ')) 

# Play the game until the correct guess 
# or until no attempts are left 
while attempts > 0: 
    user_guess = int(input("Enter your guess: ")) 
	
    if not hasUniqueDigits(user_guess): 
        print("Number should not have repeated digits. Try again.") 
        continue
    if user_guess < 1000 or user_guess > 9999: 
        print("Please enter a 4-digit number only. Try again.") 
        continue
	
    hits_misses = countHitsAndMisses(secret_code, user_guess) 
    print(f"{hits_misses[0]} hits, {hits_misses[1]} misses") 
    attempts -= 1
	
    if hits_misses[0] == 4: 
        print("Congratulations! You guessed the correct number!") 
        break
else: 
    print(f"You ran out of attempts. The secret number was {secret_code}.")