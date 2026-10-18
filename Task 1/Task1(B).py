def calculate_salary():
    # Inputs with validation
    employee_name = input("Enter Employee Name: ")
    
    try:
        basic_salary = float(input("Enter Basic Salary: "))
        allowance = float(input("Enter Allowance: "))
    except ValueError:
        print("Error: Please enter valid numeric values for salary and allowance.")
        return

    # Check for negative values (Robustness)
    if basic_salary < 0 or allowance < 0:
        print("Error: Salary and allowance cannot be negative.")
        return

    # Calculations
    gross_salary = basic_salary + allowance
    tax = 0.05 * gross_salary
    net_salary = gross_salary - tax

    # Output
    print("\n--- Salary Details ---")
    print(f"Employee Name: {employee_name}")
    print(f"Gross Salary: {gross_salary}")
    print(f"Tax (5%): {tax}")
    print(f"Net Salary: {net_salary}")

# Run the program
calculate_salary()