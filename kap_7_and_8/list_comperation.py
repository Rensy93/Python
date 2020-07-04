def main():
    l = [x for x in range(100)]
    l2 = [x ** 5 - 7 for x in range(10)]
    l3 = [x ** 5 - 7 for x in range(10) if x % 2 == 0]

    print(l, "\n")
    print(l2, "\n")
    print(l3, "\n")


main()
