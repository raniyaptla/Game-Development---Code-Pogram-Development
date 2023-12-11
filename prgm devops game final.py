import random
name = input("What is your name? ")
print("Good Luck ", name,"guessing the Fruit")

wordslist = ['apple','mango','banana','papaya','grape','orange','cherry']
word = random.choice(wordslist)


print("Guess the characters")

guesses = ''
turns = 6
while turns > 0:
    failed = 0	
    for char in word:		
        if char in guesses:
            print(char, end=" ")

        else:
            print("_")			
            failed += 1
    if failed == 0:		
            print()
            print("You Win")
            print("The word is:",word)
            break	
    print()
    guess = input("Guess a character:")
    if len(guess)!=1:
        print("Enter only one character")
    else:
        guess=guess.lower()
        guesses += guess	
        if guess not in word:
            turns -= 1
            print("Wrong")		
            print("You have", + turns, 'more guesses')
            if turns == 0:
                print("You Loose")
        
        
