import random
import json


IN_A_NEW = "You have begun a new quiz."

HELLO_NAME = "Hello, "

PERIOD = "."

WHAT_NAME = "What is your name?"

HAVE_PAUSED = "You have paused the quiz. When you want to resume, just remember to use the same exact name as you inputed when you began the quiz. See you later!"


def get_questions():

    questions = []
    with open('questionsforquiz.txt', 'r') as finalquest_handle:
        for line in finalquest_handle:
                if len(line) > 1:
                    questions.append(line.strip())
    return questions
    
questions = get_questions()

def get_all_anwers():
    
    theanswers = []
    all_answers = []
     
    with open('allanswersforquiz.txt' , 'r') as allanswers_handle:
        for edge in allanswers_handle:
            if len(edge) > 1:
                theanswers.append(edge.strip())
                
        for each_index in theanswers:
            new_index = each_index.split(";")

            all_answers.append(new_index)
          
    return all_answers
    
all_answers = get_all_anwers()


def get_correct_answers():
    
    correct_answers = []
    with open ('correctanswersforquiz.txt', 'r') as finalanswer_handle:
        for other_line in finalanswer_handle:
            if len(other_line) > 1:
                correct_answers.append(other_line.strip())
                
    return correct_answers
    
correct_answers = get_correct_answers()

def dictcreate():
    giveans = get_all_anwers()
    ans_list_real = []
    for ans in giveans:
        dictforans = {}
        random.shuffle(ans)
        keysforanswer = ["a: ", "b: " ,"c: " , "d: "]
        for el in range(len(ans)):
            dictforans[keysforanswer[el]] = ans[el]
        ans_list_real.append(dictforans)
    return(ans_list_real)
ans_list_real = dictcreate()



def first_run_quiz():
    
    print(IN_A_NEW)
    print (WHAT_NAME)
    given_name = input("")
    
    
    def checking_name():
    
        name_list = []

        with open ('thecurrent.txt', 'r') as pasued_file_handle:
            for each_intem in pasued_file_handle:
                if len(each_intem) > 1:
                    name_list.append(each_intem.strip())
                    
        with open ('thefinishedquizes.txt' ,'r') as read_finished_handle:
            for each_other_item in read_finished_handle:
                if len(each_intem) > 1:
                    name_list.append(each_other_item.strip())
                
        return name_list
    name_list = checking_name()

    newname_list = []
    for nameindex in range(len(name_list)):
        splitednamepaused = name_list[nameindex].split(',')
        newname_list.append(splitednamepaused) 
        

    for each_thing in range(len(newname_list)):
        if newname_list[each_thing][0] == given_name:
            print("We already have that name in our records. We will have to start over again. Please give a new name.")
            first_run_quiz()
            continue
        elif newname_list[each_thing][0] != given_name:
            continue
    
    print(HELLO_NAME + given_name + PERIOD)
    
    givequestions = get_questions()
    giveallanswers = dictcreate()
    getcorrect = get_correct_answers()
    possibilities = "abcd"
    score = 0
    questions_number = 0
    
    finish = False
    paused = False
    
    while not finish and not paused:
        for index_num in range(len(givequestions)):
            print(str(givequestions[index_num]))
            [print(the_key,the_val) for the_key, the_val in giveallanswers[index_num].items()]
            guess = input("Your answer: ")
            print(guess)
            if guess in possibilities and guess != "":
                guess = str(guess) + (": ")
                valofguess = giveallanswers[index_num][str(guess)]
                if valofguess == getcorrect[index_num]:
                    score = score + 1
                    print("Correct!")
                else:
                    print ("Incorrect!" + " The correct answer is " + str(getcorrect[index_num]) + ".")
            elif guess not in possibilities or guess == "":
                if guess == "pause":
                    
                    def make_the_pause(their_name, theirquest_number, their_score):
    
                        the_current_place = open('thecurrent.txt', 'a')
                        their_name = given_name
                        theirquest_number = questions_number
                        their_score = score
                        
                        the_return = the_current_place.write("\n" + str(their_name) + "," + str(theirquest_number) + "," + str(their_score))
                        
                        the_current_place.close()
                        
                        return the_return
                    
                    make_the_pause(given_name,questions_number,score)
                    paused == True
                    
                    print(HAVE_PAUSED)
                    
                    exit()
                elif guess == "":
                    print ("Incorrect!" + " The correct answer is " + str(getcorrect[index_num]) + ".")
                else:
                    print ("Incorrect!" + " The correct answer is " + str(getcorrect[index_num]) + ".")
                    
            print("Current score: " + str(score) + " out of 10")
            questions_number = questions_number + 1
            
            if questions_number == 10:
                
                
                def write_final_result(their_name, their_score):
                
                    the_final_place = open('thefinishedquizes.txt' , 'a')
                    their_name = given_name
                    their_score = score
                    
                    final_return = the_final_place.write("\n" + str(their_name) + "," + str(their_score))
                    the_final_place.close()
                
                    return final_return
                write_final_result(given_name,score)
                
                finish = True
                
                print("All done! You scored " + str(score) + " points out of a possible 10 points!")
                exit()

        
        
first_run_quiz()
