def main():
    run = True
    while run:
        points = int(input("Ange antal poäng i intervallet 0 till 100: "))

        if 0 <= points <= 100:
            run = False

            if points < 60:
                print('Betyg: F')

            if 60 <= points < 70:
                print('Betyg: D')

            if 70 <= points < 80:
                print('Betyg: C')

            if 80 <= points < 90:
                print('Betyg: B')

            else:
                print('Betyg: A')


        else:
            print("Du har anget negativa poäng." if points < 0 else 'Du har angett för många poäng')


main()
