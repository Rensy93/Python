# Economy.py

def Main():
    command = 'f'
    while command != 'e':
        command = str(input("What du you want to do?\nyearly salary incrice (y)\nRemains on salary (r)\nExit (e)\n"))
        if command == 'y':
            newSallary = SallaryYearIncrese()
            print(newSallary)
        elif command == 'r':
            print("you don't have much money left\n")
        elif command != 'e':
            print("choose ether y, r or e\n")


def SallaryYearIncrese():
    salary = int(input("What is your salary?"))
    incriment = int(input("your raise in %?"))
    years = int(input("how many years?"))
    for year in range(1, years+1):
        salary = salary * (1 + incriment / 100)
    return salary


def SallaryRimender():
    pass

Main()

