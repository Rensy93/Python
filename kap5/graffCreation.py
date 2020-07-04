# uppgift:15 kap.5
import sys


def main():
    filename = sys.argv[1]
    file = open(filename)
    number_of_students = eval(file.readline())
    # students_and_scores = file.read()
    students = []
    for i in range(number_of_students):
        students.append(file.readline())
    file.close()


main()
