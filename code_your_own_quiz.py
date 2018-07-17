easy_paragraph = '''A basic website is made with __1__ and __2__, that styles the website.
                    Every variable holds a __3__, which is the information associated
                    with the variable.  __4__ are not allowed in variable names, but
                    underscores can be used to separate words.'''
                    
medium_paragraph = '''A __1__ is a collection of items in a particular order.  You can 
                      access any __2__ of a list by telling Python the position,
                      or __3__, of the item desired.  Index positions start 
                      with __4__.'''
                      
hard_paragraph = '''Add an element to the end of a list by using __1__ .  If you know 
                    the position of the item you want to remove from a list, use
                    the __2__ statement.  The __3__ method removes the last item 
                    in the list.  Find the length of a list by using the 
                    __4__ function.'''
                    
easy_answers = ["html", "css", "value", "spaces"]
medium_answers = ["list", "element", "index", "0"]
hard_answers = ["append", "del", "pop", "len"]

questions = ["__1__", "__2__", "__3__", "__4__"]

#get player name
def get_name():
    player_name = input("What is your name?    ")
    print("Welcome, " + player_name + ".  Fill in the blanks.")
    choose_level()
    
#player choose the level to play
def choose_level():
    level_name = input("Select level:  easy, medium, hard.   ").lower()
    if level_name == "easy":
        play_level(easy_paragraph, questions, easy_answers)
    elif level_name == "medium":
        play_level(medium_paragraph, questions, medium_answers)
    elif level_name == "hard":
        play_level(hard_paragraph, questions, hard_answers)
    else:
        print("Not a choice, try again")
        return choose_level()
        
def play_level(quiz, blanks, answers):
    print(quiz)
    for count_blanks in range(0, len(blanks)):
        answer_input = input("What is " + blanks[count_blanks] +"?")
        attempts = 1
        max_attempts = 3
        while answer_input.lower()!= answers[count_blanks]:
            attempts += 1
            answer_input = input("Try again. What is" + blanks[count_blanks] + "?")
            if attempts == max_attempts:
                print("Incorrect! Try again!")
                get_level()
        else:
            quiz = quiz.replace(blanks[count_blanks], answers[count_blanks])
            print("Correct! " + quiz)
    if len(blanks) == len(answers):
        print("You Win! Play again?")
        choose_level()
    
                
                
    
get_name()
        
        


#I researched Git Hub, Stackoverflow, pythonexample, repl.it, google, udacity, Python crash course, Stack exchange









