#python quiz program

#provides feedback based upon score 
def scoreFeedback(percentage):
    if (percentage <= 25):
        print("You are dumb")
    
    elif (percentage <= 50): 
        print("You are 50% dumb")
    
    elif (percentage <= 75): 
        print("You are somewhat smart")
    
    else:
        print("You are SMART!!")


#this function marks the quiz
def markQuiz(q1, q2, q3, q4):
    #initliaze the score 
    score = 0

    #check question 1
    if (q1 == "a") or (q1 == "edmonton"):
        score += 1
        print("Question 1 is Correct")
    else:
        print("Question 1 is Wrong")
    
    #check question 2
    if (q2 == "c") or (q2 == "soccer"):
        score += 1
        print("Question 2 is Correct")
    else:
        print("Question 2 is Wrong")
    
    #check question 3
    if (q3 == "b") or (q3 == "systole"):
        score += 1
        print("Question 3 is Correct")
    else:
        print("Question 3 is Wrong")

    #check question 4
    if (q4 == "b") or (q4 == "autumn"):
        score += 1
        print("Question 4 is Correct")
    else:
        print(" Question 4 is wrong")
    
    #calculate the scores
    scoreCalc = int((score/4 * 100))

    #display score
    print("Your score is " + str(scoreCalc) + "%")

    scoreFeedback(scoreCalc)


#this function will ask the questions
def askQuestion():
    #each variable will store the user input
    q1 = input("What is the capital Edmonton? \n A: Edmonton \n B: Calgary \n C: Red Deer \n").lower()
    q2 = input("What is Noor's favorite sport? \n A: Football\n B: Cricket \n C: Soccer \n").lower()
    q3 = input("What is the name of ventricular contraction? \n A: Diastole \n B: Systole\n C: Dilation \n").lower()
    q4 = input("What is my favorite season? \n A: Summer \n B: Autumn \n C: Winter \n").lower()
    markQuiz(q1, q2, q3, q4)
askQuestion()

