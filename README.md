# Multiplechoicequiz
To run the program, run "python3 runthis.py"

The goal of the program is to finish the quiz and get a score. 
To finish the quiz, you need to complete all 10 questions asked by the program. It is possible to pause the quiz by inputting pause and anytime during the quiz.

There are multiple components within runthis.py but the user does not have to worry about. For explanation purposes:
        The user will be prompted to start a new quiz or pick up from a previous quiz.
        If the input is ‘start’, start.py is imported and that is the primary python file that is being run.
        If the input is ‘pickup’ pickup.py is imported and that is the primary python file that is being run.
        ‘thecurrent.txt’ is the text file that stores all the paused data like this per line:
        Name, Current Question, and Current Score
        ‘thecurrent.txt’ can be opened and used to pickup a quiz from where the user left off
        ‘Thefinishedquizes.txt’ is the file that stores all the finished quizes data like this per line:
            Name, Score
            If the user wants to pause the quiz, they can simply input ‘pause’ (only after their name is taken’ 
            If the user wants to resume the quiz, they will be prompted to give the same name they previously used and the quiz will pickup from where it left out
            It is possible to run  a pause the same user multiple times. The most recent (bottom-most line of that name on the file 'thecurrent.txt') will be used for the file to run through.

There are 7 end-to-end tests. To run the test, run the following:

python3 runthis.py < testit1.txt
    If you want to run this test more than once, go into 'thefinishedquizes.txt' and delete the line that starts with "Bella," before you run the test again.
    The program will run, using the orignal name to the program, "Bella '', and will complete the quiz without any pauses. The program will run entirely, finishing with no pause. The name and score is written into the file 'thefinishedquizes.txt'.
    
 
python3 runthis.py < testit2.txt
    If you want to run this test more than once, go into 'thefinishedquizes.txt' and delete the line that starts with "Emma," before you run the test again.
    
    At first, the name that is inputted to the program will return to the user; they are not allowed to use it since we have that name in our records, so it will ask the user to give another name. That name is original to the program, so it will run entirely, finishing the quiz with no pauses. The name and score is written into the file 'thefinishedquizes.txt'.
    
python3 runthis.py < testit3.txt
    If you want to run this test more than once, go into 'thefinishedquizes.txt' and delete the line that starts with "James," before you run the test again.
    
    The name that is inputted exists in the 'thecurrent.txt' file. The program is running as a pickup file so the program runs. The program will run to its entirety, finishing without any additional pauses. The name and score is written into the file 'thefinishedquizes.txt'.
    

python3 runthis.py < testit4.txt
    The program runs as a paused file, however the name that is given by the user does not exist in the 'thecurrent.txt'. Therefore the program exists.

python3 runthis.py < testit5.txt
    If you want to run this test more than once, go into 'thefinishedquizes.txt' and delete the line that starts with "Nancy," before you run the test again.
    
    The name that is inputted exists in the 'thecurrent.txt' file. The program is running as a pickup filed so the program runs. The program will run to its entirety, finishing without any additional pauses.

python3 runthis.py < testit6.txt
    If you want to run this test more than once, go into 'thecurrent.txt' and delete the latest line(bottom-most) line that starts with "Peter," before you run the test again, if you want the same result. Otherwise, you can run the test 2 more times before the user by the name "Peter" is added to 'thefinishedquizes.txt' which will exit the program if run again.
    The name that is inputted exists in the 'thecurrent.txt' file. The program is running as a pickup file. While the program is running, one of the inputs is "pause" and the name, question number, and score will be recorded to the 'thecurrent.txt' file. If you end up running this program once without clearing the 'thecurrent.txt', eventually the pickup file will finish and the name and score will be input into 'thefinishedquizes.txt'.

python3 runthis.py < testit7.txt
    If you want to run this test more than once, go into 'thefinishedquizes.txt' and delete the line that starts with "Mike," before you run the test again.
    
     The program is running as a pickup file so the program runs. The name that is inputted exists in the 'thecurrent.txt' file. The program will run to its entirety, finishing without any additional pauses.

python3 runthis.py < testit8.txt
    If you want to run this test more than once, go into 'thecurrent.txt' and delete the line that starts with "Sally," before you run the test again.
    This program starts in the original program until 'pause' is inputted. The name, the question number and score will be recorded in 'thecurrent.txt'.
 
 In text files 'thecurrent.txt' and 'thefinishedquizes.txt', there is a line that states "DO NOT EDIT ABOVE THIS LINE", do not edit above that line. But anything under that line, you may delete.




