def round_to_half_int(hours):
    hours = round(hours * 2) / 2
    return hours


def main():
    overtime, overtime_factor = 40, 1.5
    print("\nDetta pårogram kommer att beräkna din lön för förra veckans arbete.")
    hours = float(input("Vänligen skriv in hur många timmar du jobbade föra veckan"))

    if hours > 0:
        # Vi antar vi kan räkna halvtimmar som arbete
        hours = round_to_half_int(hours)
        print("Antal tillgodoräknade timmar är:", hours, "h.")

        # Timlön brukar vanligen  anges som heltal.
        hourly_wage = int(input("skriv in din timmlön: "))

        # Om vi inte jobbar overtid får vi betalla som vanligt.
        if hours < overtime:
            wage = hourly_wage * hours

        elif hours > overtime:
            wage = ((hours - overtime) * overtime_factor + overtime) * hourly_wage

        wage = round(wage)
        print('Din lön föra Veckan: ', wage, 'kr.')

    else:
        print('Du har inte arbetat denna veckan')


main()
