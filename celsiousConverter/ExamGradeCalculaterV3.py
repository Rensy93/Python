def main():
    run = True
    while run:
        points = int(input("Ange antal poäng i intervallet 0 till 100: "))

        if 0 <= points <= 100:
            run = False

            if points < 60:
                print('Betyg: F')

            elif 90 <= points <= 100:
                print("Betyg: A")

            grade = ['D', 'C', 'B']
            for i in range(len(grade)):
                grade_lower_limit = 60 + 10 * i
                if grade_lower_limit <= points < grade_lower_limit + 10:
                    print('Betyg: ', grade[i])
                    break

        else:
            print("Du har anget negativa poäng." if points < 0 else 'Du har angett för många poäng')


main()
