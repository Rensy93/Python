def calculate_sum_of_cube(n):
    cube_sum = 0
    for number in range(1, n + 1):
        cube_sum += number ** 3
    return cube_sum


def main():
    n = int(input("Vad vill du ha för n?"))
    cube_sum = calculate_sum_of_cube(n)
    print(cube_sum)


main()
