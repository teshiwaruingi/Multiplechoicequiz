# from final import *

WELCOME = "Welcome to the quiz. "


START_NEW = "Do you want to start a new quiz or pickup from where you left off? (please input either 'start' or 'pickup', respectively)"


BEGIN = "There will be ten mulitple choice questions. Each question will appear one at a time and you may answer with the following letters that correspond with an answer:\n'a' , 'b' , 'c' , 'd' \n Write them as is (with no spaces after, just hit enter) or your answer will be marked as incorrect.\n Once you answer a question, that answer is final and you will not be allowed to change your answer and the quiz will proceed to the next question.\n Any other inputs not listed will still be marked as incorrect and the quiz will proceed to the next question. \n If at any time you want to pause the quiz while is running (after you have inputed your name), simply input 'pause'  you and your work will be saved for the next time you want to pick up from where you left off."

INPUT_INVALID = "Sorry, that input was invalid. Goodbye."

print(WELCOME)
print(BEGIN)

print(START_NEW)

want_to_start = input("")
if want_to_start == "start":
    from start import *
elif want_to_start == "pickup":
    from pickup import *
else:
    print(INPUT_INVALID)
