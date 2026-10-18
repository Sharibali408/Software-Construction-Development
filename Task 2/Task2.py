# 1. Calculation Logic
def calculate_total(marks):
    return sum(marks)

def calculate_average(marks):
    total = calculate_total(marks)
    return total / len(marks) if marks else 0

def determine_grade(average):
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    else:
        return "F"

# 2. Presentation & Output Logic (Side Effects separated)
def display_result(name, total, average, grade):
    print(f"Student Name: {name}")
    print(f"Total Marks: {total}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")

def save_result_to_file(name, grade):
    with open("results.txt", "a") as file:
        file.write(f"{name},{grade}\n")

# Main execution function
def process_student_result(name, marks):
    # Call calculation functions
    total = calculate_total(marks)
    average = calculate_average(marks)
    grade = determine_grade(average)
    
    # Call output functions
    display_result(name, total, average, grade)
    save_result_to_file(name, grade)
    
    return grade

# --- Testing the code ---
if __name__ == "__main__":
    student_marks = [85, 92, 78]
    process_student_result("Ali", student_marks)