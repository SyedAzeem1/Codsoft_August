#Task 4: To develop a quiz game that asks users multiple-choice or fill-in-the-blanks questions on a specified topic.
print("Welcome to the quiz game\n",
    "Selct a topic to continue\n",
    "Based on your topic questions will be asked and you will get a score according to the number of correct answers")
Topic = input("Select a topic for the quiz: Science or Maths or English:\n ")
if Topic == "Science":  
    questions = ("How many bones are there in a human body: ?",
                 "Animals that lay eggs are called: ?",
                 "Which is the most abundant gas on Earth: ?")
    options = (("A.106","B.206","C.209","D.207"),
               ("A.Viviparous","B.Oviparous","C.Both A and B","D.None of the above"),
               ("A.Nitrogen","B.Oxygen","C.Carbondioxide","D.Hydrogen"))
    answers = ("B","B","A")
    guesses = []
    score = 0
    question_num = 0

    for question in questions:
        print("-------------------")
        print(question)
        for option in options[question_num]:
            print(option)
        guess = input("Enter A,B,C,D: ").upper()
        guesses.append(guess)
        if guess == answers[question_num]:
            print("Correct")
            score += 1
        else:
            print("Incorrect, Try again")
        question_num +=1 
    print("--------------")
    print("   resulsts   ")
    print("--------------")
    score = int((score/len(questions)) * 100)        
    print("Score = ",score,"%")
    print("Hope  you enjoyed ,if you enjoyed play again")
elif Topic == "Maths":
    questions  = ("A Traingle with no equal sides is called: ",
                 "Angle which is less than  90 degree is called: ",
                 "Formula to find Lateral Surface Area of cuboid is: ")
    options = (("A.Isosceles","B.Scalene","C.Equilateral","D.None of these"),
               ("A.Obtuse Angle","B.Acute Angle","C.Complimentary Angle","D.Adjacent Angle"),
               ("A.2h(l+b)","B.l*b*h","C.2(lb+bh+hl)","D.a*3"))
    answers = ("C","B","A")
    guesses = []
    score = 0
    question_num = 0
    for question in questions:
        print("-------------------")
        print(question)
        for option in options[question_num]:
            print(option)
        guess = input("Enter A,B,C,D: ").upper()
        guesses.append(guess)
        if guess == answers[question_num]:
            print("Correct")
            score += 1
        else:
            print("Incorrect, Try again")
        question_num +=1 
    print("--------------")
    print("   resulsts   ")
    print("--------------")
    score = int(score/len(questions)*100)
    print("Score = ",score,"%")
    print("Hope  you enjoyed ,if you enjoyed play again")
elif Topic == "English":
    questions = ("Synonyms of brood is: ",
                 "Who is the author of Merchant of Venice?",
                 "What is the meaning of cheugy?")
    options = (("A.Bedec","B.Muse","C.Accommodate","D.None of these"),
               ("A.William Shakespeare","B.Charlotte Brontë","C.Agatha Christie","D.Charles Dickens"),
               ("A.Cool","B.Angry","C.Anxious","D.Uncool"))
    answers = ("B","A","D")
    guesses = []
    score = 0
    question_num = 0
    for question in questions:
        print("-------------------")
        print(question)
        for option in options[question_num]:
            print(option)
        guess = input("Enter A,B,C,D: ").upper()
        guesses.append(guess)
        if guess == answers[question_num]:
            print("Correct")
            score += 1
        else:
            print("Incorrect, Try again")
        question_num +=1 
    print("--------------")
    print("   resulsts   ")
    print("--------------")
    score = int(score/len(questions)*100)
    print("Score = ",score,"%")
    print("Hope  you enjoyed ,if you enjoyed play again")