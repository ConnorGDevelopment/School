# Input

units = [
    ["fahrenheit","f"],
    ["celsius", "c"],
    ["kelvin", "k"], 
    # https://en.wikipedia.org/wiki/Delisle_scale
    ["delisle", "d"]
]

def prompt_unit_input(unit_choices=units): 

    print('Select a unit by typing the full name or the letter abbreviation in parenthesis')

    # On starting unit selection, we use the raw units const
    # On ending unit selection, we pass in only the units that have defined conversion 
    for unit in unit_choices:
        print(f"- {unit[0].capitalize()} ({unit[1].capitalize()})")
        
    unit_input = input()
    
    for unit in unit_choices:
        if(unit_input.lower() == unit[0] or unit_input.lower() == unit[1]):
            return unit
    
    # This only runs if a value is not returned above
    print("Invalid Input")
    return []

## 1. Fahrenheit > Float
## 2. Celsius > Float
## 3. Kelvin > Float
def prompt_value_input():
    print('Enter a numerical value')
    
    value_input = input()
    
    # Screech if can't convert
    try:
        return float(value_input)
    except ValueError:
        print("Invalid Input")
            
# Convert
## 1. Fahrenheit > Celsius
## ( Temperature in Fahrenheit - 32 ) x 5 / 9 = Temperature in Celsius
def f_to_c(val):
    return (val - 32) * (5/9)

## 2. Celsius > Fahrenheit
## Temperature in Celsius x 9 / 5 + 32 = Temperature in Fahrenheit
def c_to_f(val):
    return val * (9/5) + 32

## 3. Fahrenheit > Kelvin
## ( Temperature in Fahrenheit - 32 ) x 5 / 9 + 273.15 = Temperature in Kelvin
def f_to_k(val):
    return (val - 32) * (5/9) + 273.15

## 4. Kelvin > Fahrenheit
## ( Temperature in Kelvin - 273.15 ) x 9 / 5 + 32 = Temperature in Fahrenheit
def k_to_f(val):
    return (val - 273.15) * (9/5) + 32

## 5. Celsius > Kelvin
## Temperature in Celsius + 273.15 = Temperature in Kelvin
def c_to_k(val):
    return val + 273.15

## 6. Kelvin > Celsius
## Temperature in Kelvin - 273.15 = Temperature in Celsius
def k_to_c(val):
    return val - 273.15

## Extras
def f_to_d(val):
    return (212 - val) * (6/5)

def c_to_d(val):
    return (100 - val) * (2/3)

def d_to_c(val):
    return (100 - val) * (3/2)    
    
def d_to_f(val):
    return(212 - val) * (5/6)

# [ starting_unit, List<[ending_unit, conversion_function] ]
conversion_tree = [
    # Fahrenheit
    [units[0], [
        [units[1], f_to_c],
        [units[2], f_to_k],
        [units[3], f_to_d]
    ]],
    # Celsius
    [units[1],[
        [units[0], c_to_f],
        [units[2], c_to_k],
        [units[3], c_to_d]
    ]],
    # Kelvin
    [units[2],[
        [units[0], k_to_f],
        [units[1], k_to_c]
    ]],
    # Delisle
    [units[3], [
        [units[0], d_to_f],
        [units[1], d_to_c]
    ]]
]    

# Print Before and After Values
while True:    
    print("Select Starting Unit:")
    print("")
    
    # The general pattern here is:
    #   1. Init a selection var as None
    #   2. While that var is None, run a prompt which will update that value, breaking the loop
    #   3. Give a display of inputted info
    #   4. Repeat until all selections are made
    starting_unit_selected = None
    
    while starting_unit_selected == None:
        starting_unit_selected = prompt_unit_input()
    
    if(starting_unit_selected):
        print(f"Starting Unit: {starting_unit_selected[0].capitalize()}")
        print("")

        starting_value_selected = None
        
        while starting_value_selected == None:
            print("")
            print("Enter Starting Value:")
            print("")
            starting_value_selected = prompt_value_input()
            
        
        if(starting_value_selected):
            print("")
            print(f"Starting Unit: {starting_unit_selected[0].capitalize()}")
            print(f"Starting Value: {starting_value_selected}")
            print("")
            
            ending_unit_selected = None
            
            # In JS, I would normally do:
            # matched_conversion_tree = conversion_tree.find(unit => unit === starting_unit_selected)
            # And then to find the conversion function after ending_unit_selected is chosen:
            # ending_unit_selected = matched_conversion_tree.find(branch => branch[0] === ending_unit_selected)[1]
            # But can't chain in Python, or at least I don't know how
            
            matched_conversion_tree = conversion_tree[units.index(starting_unit_selected)][1]
            
            valid_unit_choices = []
            for branch in matched_conversion_tree:
                valid_unit_choices.append(branch[0])
                
            while ending_unit_selected == None:
                ending_unit_selected = prompt_unit_input(valid_unit_choices)
                
            if(ending_unit_selected):        
                matched_conversion = None
                for branch in matched_conversion_tree:
                    if(branch[0] == ending_unit_selected):
                        matched_conversion = branch[1]
                
                print("")
                print(f"Starting Unit: {starting_unit_selected[0].capitalize()}")
                print(f"Starting Value: {starting_value_selected}")
                print(f"Ending Unit: {ending_unit_selected[0].capitalize()}")
                print(f"Ending Value: {matched_conversion(starting_value_selected)}")
                print("")
                
                starting_unit_selected = None
                starting_value_selected = None
                ending_unit_selected = None
                
                
                