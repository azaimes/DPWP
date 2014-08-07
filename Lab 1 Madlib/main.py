'''
Name: Adam Zaimes
'''
# while loop to make the program continuous

start = 1
while start != 0:

    #variables
    name = raw_input("What is your name? ")
    hours = float(raw_input("How many hours do you spend studying? "))
    job = raw_input("What job do plan to get after graduation? ")
    gpa = float(raw_input("What is your current gpa? "))
    grad_year = raw_input("What year will you graduate? ")
    born_year = raw_input("What year were you born? ")

    #convert to integers for calculation
    grad_year = int(grad_year)
    born_year = int(born_year)

    #calculate age at graduation
    age = grad_year - born_year

    #setup array
    relax = raw_input("What is your favorite video game? ")
    relax2 = raw_input("What is your second favorite video game? ")

    #array to get input from above
    games_played = []

    #add to array
    games_played.append(relax)
    games_played.append(relax2)

    #add 10 years to grad year
    def after_grad(x):
        after = x + 10
        return after

    #set variable for above function
    ag = after_grad(age)
    #dictionary
    life = dict()
    life = {"Family": "kids", "Job": "career"}
    #conver gpa to integer
    gpa = int(gpa)
    hours = int(hours)
    #conditional statement for gpa

    def grades():
        if gpa >= 3:
            great = "great job!"
            return great

        elif gpa <= 2:
            harder = "try harder!"
            return harder
        else:
            not_good = "It's not looking good for you!"
            return not_good
    #conditional for study time

    def study_time():
        if hours >= 15:
            good_student = " you study hard!"
            return good_student
        else:
            bad_student = " you need to study more!"
            return bad_student
    #story
    print "Hello, " + name + "! Your mission is to succeed in class!" + " Based on your answer of spending " \
          + str(hours) + " hours studying," + study_time() + " If you want to be a great " + job + \
          " you need to be successful in school! " + " Your GPA is " + str(gpa) + " " + grades() + \
          " All work and no play isn't good for you." + " Spend some time enjoying " + str(games_played) + ". " \
          + "After graduation " + life["Family"] + " and " + life["Job"] + " can make things difficult! " \
          + " But you will only be " + str(age) + " years old, and in 10 years you will be " + str(ag) + \
          " and successful!"










