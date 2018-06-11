easy_paragraph = '''A basic website is made with ___1___ and ___2___, that styles the website.
                    Every variable holds a ___3___, which is the information associated
                    with the variable.  ___4___ are not allowed in variable names, but
                    underscores can be used to separate words.'''
                    
medium_paragraph = '''A ___1___ is a collection of items in a particular order.  You can 
                      access any ___2___ of a list by telling Python the position,
                      or ___3___, of the item desired.  Index positions start 
                      with ___4___'''
                      
hard_paragraph = '''Add an element to the end of a list by using ___1___ .  If you know 
                    the position of the item you want to remove from a list, use
                    the ___2___ statement.  The ___3___ method removes the last item 
                    in the list.  Find the length of a list by using the 
                    ___4___ function.'''
                    
easy_answers = ["html", "css", "value", "spaces"]
medium_answers = ["list", "element", "index", "0"]
hard_answers = ["append", "del", "pop", "len"]

def get_name():
    player_name = input("What is your name?    ")
    print("Welcome, " + player_name + " .  Fill in the blanks.")
    choose_level()

def choose_level():
    level_name = input("Select level:  easy, medium, hard.   ")
    if level_name == "easy":
        print(get_level(level_name))
    elif level_name == "medium":
        get_level(level_name)
    elif level_name == "hard":
        get_level(level_name)
    else:
        print("Not a choice, try again")
        return choose_level()
        
def get_level(level_name):
    if level_name == "easy":
        print(easy_paragraph)
        level_answers = easy_answers
        return level_first_blank(easy_paragraph, level_answers)
    elif level_name == "medium":
        print(medium_paragraph)
        level_answers = medium_answers
        return level_first_blank(medium_paragraph, level_answers)
    else:
        print(hard_paragraph)
        level_answers = hard_answers
        return level_first_blank(hard_paragraph, level_answers)
        
        
def level_first_blank(level_string, level_answers):
    user_input= input("What is your answer for blank 1?   ")
    
    if user_input == level_answers[0]:
        print("That's correct!")
        first_blank_correct_string = level_string.replace('___1___', user_input)
        return level_second_blank(first_blank_correct_string,level_answers)
    else:
        guess_counter = 3
        while guess_counter > 0:
            print("Try again")
            return level_first_blank(level_string, level_answers)
            guess_counter = guess_counter - 1
        else:
            print("You lose")
            
            
            
            
            
def level_second_blank(first_blank_correct_string,level_answers):
    print(first_blank_correct_string)
    user_input = input("What's your answer for blank 2?   ")
    if user_input == level_answers[1]:
        print("That's correct")
        second_blank_correct_string = first_blank_correct_string.replace('__2__', user_input)
        return level_third_blank(second_blank_correct_string,level_answers)
    else:
        print("Sorry that's not correct")
        
        

def level_third_blank(second_blank_correct_string,level_answers):
    print(second_blank_correct_string)
    user_input = input("What's your answer for blank 3?   ")    
    if user_input == level_answers[2]:
        print("That's correct")
        third_blank_correct_string = second_blank_correct_string.replace('__3__', user_input)
        return level_fourth_blank(third_blank_correct_string,level_answers)
    else:
       print("Sorry not correct")
           
       
        
        
        
def level_fourth_blank(third_blank_correct_string, level_answers):
    print(third_blank_correct_string)
    user_input = input("What is your answer to blank 4?   ")
    if user_input == level_answers[3]:
        print("That's correct")
        fourth_blank_correct_string = third_blank_correct_string.replace('___4___', user_input)
        print(fourth_blank_correct_string)
        print("You Win!")
        
        answer = input("\nWould you like to play again?  Y/N   ")
        if answer == "N":
            print("Thanks for playing")
        else:
            return choose_level()
    else:
        print("Sorry, that's not correct")

    
    
    
get_name()
        
        


#I researched Git Hub, Stackoverflow, pythonexample, repl.it, google, udacity, Python crash course, Stack exchange









