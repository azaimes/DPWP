'''
Name: Adam Zaimes
'''
#while loop to make the program continuous

start = 1
while start !=0:

    #variables
    name = raw_input("What is your name? ")
    hours = raw_input("How many hours do you spend studying? ")
    job = raw_input("What job do plan to get after graduation? ")
    gpa = raw_input("What is your current gpa? ")
    grad_year = raw_input("What year will you graduate? ")
    born_year = raw_input("What year were you born? ")

    #convert to integers for calculation
    grad_year = int(grad_year)
    born_year = int(born_year)

    #calculate age at graduation
    age = grad_year - born_year

    #setup array
    relax = raw_input("What is your favorite video game?")
    relax2 = raw_input("What is your second favorite video game?")

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
    life = {"Family":"Kids", "Job":"Career"}
    












