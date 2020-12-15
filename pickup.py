import random
import json

NAME_DOESNT = "Sorry, that name does not exist in our records. We cannot continue."
WHAT_NAME = "What is your name?"

IN_A_PAUSE = "You have resumed your quiz."

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


def run_quiz():
    
    print(IN_A_PAUSE)
    
    givequestions = get_questions()
    giveallanswers = dictcreate()
    getcorrect = get_correct_answers()
    possibilities = "abcd"
    score = 0
    questions_number = 0
    
    finish = False
    paused = False
    
    print(WHAT_NAME)
    find_name = input("")
    
    def find_if_finished():
        finished_list = []
        with open ('thefinishedquizes.txt' , 'r') as finished_file_handle:
            for finished_item in finished_file_handle:
                if len(finished_item) > 1:
                    finished_list.append(finished_item.strip())
                    # print(finished_list)
        return finished_list
    finished_list = find_if_finished()
    
    
    a_paused_list_finished = []
    for paused_num_finish in range(len(finished_list)):
        splitedpaused_fin = finished_list[paused_num_finish].split(',')
        a_paused_list_finished.append(splitedpaused_fin)
    
    
        
    for finish_each_thing in range(len(a_paused_list_finished)):
       
        other_placeholder_pause = []
        
        if a_paused_list_finished[finish_each_thing][0].strip() == find_name:
            print("You have already played and finished the quiz. Goodbye.")
            exit()
    
    def return_paused():
    
        paused_list = []

        with open ('thecurrent.txt', 'r') as pasued_file_handle:
            for each_intem in pasued_file_handle:
                if len(each_intem) > 1:
                    paused_list.append(each_intem.strip())
                
        return paused_list
    paused_list = return_paused()
    
    a_paused_list = []
    for paused_num in range(len(paused_list)):
        splitedpaused = paused_list[paused_num].split(',')
        a_paused_list.append(splitedpaused) 
        
    for each_thing in range(len(a_paused_list)):
       
        placeholder_pause = []
        
        if a_paused_list[each_thing][0].strip() == find_name:
            placeholder_pause = (a_paused_list[each_thing])
            break
        if each_thing == len(paused_list)-1:
            print (NAME_DOESNT)
            exit()

    def desired_name():
    
        desired_name = placeholder_pause[0]
        latest = ''
        for items_forname in a_paused_list:
            if items_forname[0] == desired_name:
                latest = items_forname
        return latest
    desired_name()
    latest = desired_name()
    
    placeholder_pause = latest 

    new_question_num = int((placeholder_pause[1]))
    the_paused_score = int(placeholder_pause[2])
    
    score = the_paused_score
    questions_number = new_question_num -1
    given_name = find_name
    
    if new_question_num == 0:
        
        new_question_num = new_question_num + 1 

    print(IN_A_PAUSE)
        
    while not finish and not paused:
        
        for index_num in range(len(givequestions)):
            real_index_place = index_num + new_question_num -1
            
            print(str(givequestions[real_index_place]))
            [print(the_key,the_val) for the_key, the_val in giveallanswers[real_index_place].items()]
            guess = input("Your answer: ")
            if guess in possibilities and guess != "":
                guess = str(guess) + (": ")

                valofguess = giveallanswers[real_index_place][str(guess)]
                print(valofguess)
                if valofguess == getcorrect[real_index_place]:
                    score = score + 1
                    print("Correct!")
                else:
                    print ("Incorrect!" + " The correct answer is " + str(getcorrect[real_index_place]) + ".")    
                    
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
                    print ("Incorrect!" + " The correct answer is " + str(getcorrect[real_index_place]) + ".")        
                    
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
        
run_quiz()

