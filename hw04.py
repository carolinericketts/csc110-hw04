# ------------------------------------------------------
#        Name: Caroline Ricketts
#       Peers: N/A
#  References: Lecture 11, Lecture 12, Lecture 13
# ------------------------------------------------------
import sys

secret_word = "food"

# Task 1
def check_text():
    """ prints if user input contains the secret word, "dog," or "Dog"

Takes in a string input from the user as user_input.
If the user input contains the secret word,
prints "You used the secret word!", and exits loop.
If the user input contains "dog" or "Dog",
prints "You used the word "dog" or the word "Dog"!", and exits loop.
If user input does not contain either,
prints "Try again" and repeats loop.
"""
    while True:
        user_input = input("Give me a sentence: ")
        #contains secret word: print message then break
        if secret_word in user_input:
            print("You used the secret word!")
            break
        #contains "dog": print message then break
        elif "dog" in user_input:
            print('You used the word "dog" or the word "Dog"!')
            break
        #contains "Dog": print message then break
        elif "Dog" in user_input:
            print('You used the word "dog" or the word "Dog"!')
            break
        else:
            print("Try again")


# Task 2
def check_greater():
    """takes in two integers from user, prints a comparison of their values

Takes in two integers from the user as user_input_1 and user_input_2.
If the first is greater, 
prints "First is greater" and leaves the loop.
If the second is greater,
prints "Second is greater" and leaves the loop.
If the numbers are equal,
prints "Try again" and repeats loop.
"""
    while True:
        #get input
        first_integer = int(input("Give me a first integer: "))
        second_integer = int(input("Give me a second integer: "))
        #evaluate inputs and print
        if (first_integer > second_integer):
            print("First is Greater")
            break
        elif (second_integer > first_integer):
            print("Second is Greater")
            break
        elif (first_integer == second_integer):
            print("Try again")
        else:
            break
        


# Task 3
def get_special_numbers():
    """ prints numbers that are odd, multiples of 3, and not multiples of 5 in [1,40]
For all numbers in the range [1,40]:
if even, discards,
if not multiple of 3, discards,
and if multiple of 5, discards.
Prints remaining numbers on their own lines.
"""
    #sort and print numbers
    for num in range (1,41):
        if num%2==1 and num%3==0 and num%5!=0:
            print(num)


# Task 4.a
def my_for_loop():
    """ prints each letter from user input as a vowel or consonant

Assigns " " to the variable space.
Takes a string from the user as user_string.
If the string contains spaces,
or is not within the lenth range [2,5], prints "bad word."
If the string has no spaces,
and is within the length range [2,5],
then each in the string letter is printed in the format:
"letter <let> is a vowel" if the letter is a vowel,
or "letter <let> is a consonant" if the letter let is a consonant.
"""
    space = " "
    user_string = input("Give me a string: ")
    if space in user_string or not 2<=len(user_string)<=5:
        print("bad word")
    #go through letters, print if vowel or consonant
    else:
        for let in user_string:
            if (let == "A" or let == "a" or let == "E" or let == "e" or let == "I" or let == "i" or let == "O" or let == "o" or let == "U" or let == "u"):
                print(f"letter {let} is a vowel")
            else:
                print(f"letter {let} is a consonant")
    

# Task 4.b
def my_while_loop():
    """ takes in a string from the user until the loop breaks or exits program

Takes a string from the user as user_input.
If the user input "a", continues the loop.
If the user input "b", prints "Goodbye" and breaks the loop.
If the user input "c", exits the program.
If the user input anything else,
prints "try again" and repeats the loop.
"""
    while True:
        user_input = input("Choose one option: a, b, or c: ")
        if user_input=="b":
            print("Goodbye")
            break
        elif user_input=="a":
            continue
        elif user_input=="c":
            sys.exit()
        else:
            print("try again")
        

# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

def main():

    # Task 1 calls
    check_text()

    # Task 2 calls
    check_greater()

    # Task 3 calls
    get_special_numbers()

    # Task 4 calls
    my_for_loop()
    my_while_loop()

if __name__ == "__main__":
    main()
    print("The End")
