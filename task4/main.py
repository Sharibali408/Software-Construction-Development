from validation import validate_mark
from calculations import calculate_total, calculate_average, calculate_grade
from display import display_result


def main():
    name = input("Enter student name: ")

    marks = []

    for i in range(3):
        while True:
            mark = float(input("Enter marks for subject " + str(i + 1) + ": "))

            if validate_mark(mark):
                marks.append(mark)
                break
            else:
                print("Invalid marks. Enter 0-100.")

    total = calculate_total(marks)
    average = calculate_average(marks)
    grade = calculate_grade(average)

    display_result(name, total, average, grade)


main()