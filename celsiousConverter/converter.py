
def main():
    print('Detta programet commer convatera celcius till farenhight\n')
    print('Celsius'.ljust(30), 'Fahrenhit')
    print('_ ' * (30 + len(' Fahrenhit')))

    for celsius in range(0, 46, 2):
        fahrenheit = 9/5 * celsius + 32
        print(str(celsius).ljust(30), fahrenheit)

main()