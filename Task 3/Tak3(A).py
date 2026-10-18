# --- BEFORE (Complex Boolean Logic) ---
def check_bonus_before(employee):
    # Assumes employee is a dictionary or object with these attributes
    if (employee.active == True and 
        employee.months >= 12 and 
        employee.rating >= 4 and 
        employee.disciplinary == False and 
        employee.attendance >= 90):
        return "Bonus Approved"
    else:
        return "Bonus Denied"

# --- AFTER (Refactored & Readable) ---
def is_eligible_for_bonus(employee):
    """Encapsulates the complex business rule into a meaningful name."""
    has_min_experience = employee.months >= 12
    has_good_rating = employee.rating >= 4
    has_clean_record = employee.disciplinary == False
    has_good_attendance = employee.attendance >= 90
    
    return (employee.active and 
            has_min_experience and 
            has_good_rating and 
            has_clean_record and 
            has_good_attendance)

def check_bonus_after(employee):
    if is_eligible_for_bonus(employee):
        return "Bonus Approved"
    return "Bonus Denied"

# --- TESTING (Boundary Cases) ---
class Employee:
    def __init__(self, active, months, rating, disciplinary, attendance):
        self.active = active
        self.months = months
        self.rating = rating
        self.disciplinary = disciplinary
        self.attendance = attendance

# Normal Case (Pass)
emp1 = Employee(True, 15, 5, False, 95)
# Boundary Case (Pass exactly at limits)
emp2 = Employee(True, 12, 4, False, 90) 
# Failing Case (Low attendance)
emp3 = Employee(True, 20, 5, False, 85) 

print(f"Emp1: {check_bonus_after(emp1)}") # Bonus Approved
print(f"Emp2: {check_bonus_after(emp2)}") # Bonus Approved
print(f"Emp3: {check_bonus_after(emp3)}") # Bonus Denied