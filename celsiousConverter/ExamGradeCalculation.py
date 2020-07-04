
def main():
    run = True
    while run:
        points = int(input("antal poäng i intervallt 0-5: "))

        if 0 <= points <= 5:
            run = False

            if points <= 1:
                print('Betyg: F')

            elif points == 2:
                print('Betyg: D')

            elif points == 3:
                print('Betyg: C')

            elif points == 4:
                print('Betyg: B')

            else:
                print("Betyg: A")

        else:
            print("Du har anget negativa poäng." if points < 0 else 'Du har angett för många poäng')

main()