questions = { 
    "Python is a snake and programming language.":"True",
    "There are 25 hours in a day.":"False",
    "The boiling temperature of water is 100 degree celsius.":"True",
    "Pluto is a planet.":"True",
    "Group Captian Shubhanshu Shukla is an Indian Air Force Pilot and astronaut.":"True"
}

score = 0

def ask_questions():
    global score
    for q in questions:
        print("\n" + q)
        print("1. True")
        print("2. False")
        opt = input("Enter 1 or 2: ")

        if opt == "1":
            answer = "True"
        elif opt == "2":
            answer = "False"
        else:
            print("Invalid input given")
            continue

        if answer == questions[q]:
            print("Hurray !!")
            score = score + 1
        else:
            print("Wrong answer ")

cal_percent = lambda score, total: (score/total)*100
print("Let's begin the quiz\n")
ask_questions()
total = len(questions)
print("Your score is ",score, "/", total)
print("Percentage: ",cal_percent(score,total))
