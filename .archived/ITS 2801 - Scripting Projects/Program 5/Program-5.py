import math

def int_to_text(val: int):
    digit_names_to_twenty = [
        "Zero",
        "One",
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
        "Ten",
        "Eleven",
        "Twelve",
        "Thirteen",
        "Fourteen",
        "Fifteen",
        "Sixteen",
        "Seventeen",
        "Eighteen",
        "Nineteen",
    ]
    
    tens_place = [
        "",
        "",
        "Twenty",
        "Thirty",
        "Forty",
        "Fifty",
        "Sixty",
        "Seventy",
        "Eighty",
        "Ninety"
]
    
    ## If Python weren't made by a disorganized psychopath, the following would be a lot prettier
    ## Chain of if/else because Python is afraid of switch blocks
    if(val > 99):
        return "A lot of"
    ## These two cases could actually be combined with some more clever ternary-ing
    elif(val >= len(digit_names_to_twenty)):
        ## A super long line because Python has the ugliest ternary operators
        ## God I miss being able to newline + tab to make things readable
        return tens_place[math.floor(val / 10)] + ((" " + digit_names_to_twenty[val % 10]) if (val % 10 > 0) else "")
    elif((val < len(digit_names_to_twenty)) & (val >= 0)):
        return digit_names_to_twenty[val]
    else:
        return "A physics-redefining amount" 

while True:
    print("Please enter the quantity of beers to attach to walls")
    user_input = input()

    ## int(value) throws an error instead of returning null or false when param is bad
    ## So I just did a try/catch block like I would for a fetch request in JS
    ## I did have to look up what word Python uses instead of catch
    try:
        for i in reversed(range(int(user_input) + 1)):
            if(i > 0):
                print(f"{int_to_text(i)} bottles of beer on the wall")
                print(f"{int_to_text(i)} bottles of beer")
                print("Take one down, pass it around")
                print(f"{int_to_text(i - 1)} bottles of beer on the wall \n")
            else:
                print(f"{int_to_text(0)} bottle of beer on the wall")
                print(f"{int_to_text(0)} bottle of beer")
                print("We've taken them down and passed them around")
                print("Now we're drunk and passed out \n")
    except ValueError:
        print("It is unsafe to consume non-quantifiable amounts of bottles of beer, or probably any liquid")
        
            
            

