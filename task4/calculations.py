def calculate_total(marks):
    total = sum(marks)
    return total


def calculate_average(marks):
    total = calculate_total(marks)
    average = total / len(marks)
    return average


def calculate_grade(average):
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"