from time import sleep

def convert_basic(n):
    """converts a number 0-9 to itself spelled out in a string"""
    if n == 0:
        return ''
    elif n == 1:
        return 'one'
    elif n == 2:
        return 'two'
    elif n == 3:
        return 'three'
    elif n == 4:
        return 'four'
    elif n == 5:
        return 'five'
    elif n == 6:
        return 'six'
    elif n == 7:
        return 'seven'
    elif n == 8:
        return 'eight'
    elif n == 9:
        return 'nine'
    elif n == 10:
        return 'ten'
    elif n == 11:
        return 'eleven'
    elif n == 12:
        return 'twelve'
    elif n == 13:
        return 'thirteen'
    elif n == 14:
        return 'fourteen'
    elif n == 15:
        return 'fifteen'
    elif n == 16:
        return 'sixteen'
    elif n == 17:
        return 'seventeen'
    elif n == 18:
        return 'eighteen'
    elif n == 19:
        return 'nineteen'

def convert_tens(n):
    """converts a number 0-9 to itself spelled out in a string"""
    if n == 2:
        return 'twenty'
    elif n == 3:
        return 'thirty'
    elif n == 4:
        return 'fourty'
    elif n == 5:
        return 'fifty'
    elif n == 6:
        return 'sixty'
    elif n == 7:
        return 'seventy'
    elif n == 8:
        return 'eighty'
    elif n == 9:
        return 'ninety'

high_numbers = ("thousand", "million", "billion", "trillion", "quadrillion", "quintillion")
def calc(n) -> str:
    if n < 0:
        return "negative " + calc(n * -1)
    elif n < 20:
        return convert_basic(n)
    elif n < 100:
        return convert_tens(n // 10) + "-" + convert_basic(n % 10)
    elif n < 1000:
        return convert_basic(n // 100) + " hundred " + calc(n % 100)
    compare = 1000
    for word in high_numbers:
        new_compare = compare * 1000
        if n < new_compare:
            return calc(n // compare) + " " + word + " " + calc(n % compare)
        else:
            compare = new_compare
    return "too high"


def magic():
    print("Welcome to the riddle! As you will soon see, 4 is the magic number. If you think you've figured out why 4 is magic, input 'Answer' to see if you're right. If you need a hint, input 'Hint' for a hint on your next guesses (or the same to turn off the hints). You can also input 'Exit' once you're done. Hope you enjoy!")
    hint = False

    while True:
        text = input("Please input any number: ")
        if text.strip().lower() == "answer":
            print("Everything is based on the number of letters in the spelled out number. 4 is magic, because there are exactly 4 letters in it. 3 is 5 because 'three' has 5 letters in it, etc. If you got it right, congrats!")
            continue
        if text.strip().lower() == "hint":
            if not hint:
                print("Hint applied!")
            else:
                print("Hint removed!")
            hint = not hint
            continue
        if text.strip().lower() == "exit":
            print("See you next time!")
            return
        try:
            num = int(text)
        except:
            print("Please only input integers for the riddle, e.g. '4'.")
            continue
        while num != 4:
            if num == 0:
                num_text = 'zero'
            else:
                num_text = calc(num)  
                if num_text == "too high":
                    print("Sorry, this program only calculates into the quintillions, please choose a lower number.")
                    break
                new_num = len(num_text.replace(" ", ""))
            if hint:
                print(f"{num_text} is {new_num}")
            else:
                print(f"{num} is {new_num}")
            num = new_num
            sleep(0.5)

        if num == 4:
            print(f"{'four' if hint else 4} is 4, and 4 is the magic number!")

magic()
        