def get_colors(prompt):
    colour = input(prompt)
    colours = {}
    while colour:
        for c in colour:
            if not c.isalpha() and colour:
                print("Buuuh! This is not a colour")
                #get_colors(prompt)
                colour = input(prompt)

        colour = colour.lower()
        if colour in colours:
            colours[colour] += 1
        else:
            colours[colour] = 1

        colour = input(prompt)

    return colours

def print_numbers_of_colors(colours):
    print(colours)


def main():
    prompt = "Give me a color in your rainbow, please."
    colours = get_colors(prompt)
    print_numbers_of_colors(colours)


if __name__ == '__main__':
    main()
