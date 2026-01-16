def validate_str_input(val, keywords):
    for keyword in keywords:
        if(val.lower().find(keyword)):
            return True
    return False

while True:
    print("Enter your name")
    # Get name, capitalize string
    player_name = input().capitalize()
    
    print(" ")
    print("You're standing in a large ballroom")
    print("You see a man in the back")
    print("His eyes are as red as the sun")
    print(" ")
    
    man_conversation = None
    
    while man_conversation == None:
        print("Type either the number or the choice to select")
        print("     1. Yes")
        print("     2. No")
        
        man_conversation_input = input()
        
        if(validate_str_input(man_conversation_input, ["1", "y"])):
            man_conversation = True
            
            print(" ")
            print("You approach the man and try to start up a conversation but...")
            print("Then he suddenly shouts 'Everyone Attack!'")
            print("What do you do?")
            print(" ")
            
            man_fight_choice = None
            
            while man_fight_choice == None:
                print("     1. Start fighting!")
                print("     2. Stay at the back and enjoy some snacks")
                man_conversation_choice_input = input()
                
                if(validate_str_input(man_conversation_choice_input, ["1", "start", "fight"])):
                    man_fight_choice = True
                elif(validate_str_input(man_fight_choice, ["2", "stay", "back", "enjoy" "snack", "eat"])):
                    man_fight_choice = False
                else:
                    print(" ")
                    print("You're a ballroom ditz, try again")
                
                
            
            # if(man_conversation_choice.lower())
        elif(validate_str_input(man_conversation_input, ["2", "n"])):
            man_conversation = False
        else:
            print("You're a ballroom ditz")
        

        