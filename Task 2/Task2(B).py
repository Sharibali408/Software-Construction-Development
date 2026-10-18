# 1. Required Calculation Functions
def calculate_gross_salary(basic_salary, allowance):
    """Calculates gross salary by adding basic salary and allowance."""
    return basic_salary + allowance

def calculate_tax(gross_salary, tax_rate):
    """Calculates tax based on gross salary and tax rate percentage."""
    return gross_salary * (tax_rate / 100)

def calculate_net_salary(gross_salary, tax_amount):
    """Calculates net salary after deducting tax from gross salary."""
    return gross_salary - tax_amount

# 2. Main Function (Input and Display)
def run_salary_calculator():
    print("--- Employee Salary Calculator ---")
    
    try:
        # Inputs
        name = input("Enter Employee Name: ")
        basic_salary = float(input("Enter Basic Salary: "))
        allowance = float(input("Enter Allowance: "))
        tax_rate = float(input("Enter Tax Rate (%): "))
        
        # Validation check (Robustness)
        if basic_salary < 0 or allowance < 0 or tax_rate < 0:
            print("Error: Values cannot be negative.")
            return

        # Calling the required functions
        gross_salary = calculate_gross_salary(basic_salary, allowance)
        tax_amount = calculate_tax(gross_salary, tax_rate)
        net_salary = calculate_net_salary(gross_salary, tax_amount)

        # Displaying the Output
        print("\n--- Salary Breakdown ---")
        print(f"Employee Name: {name}")
        print(f"Gross Salary:  {gross_salary:.2f}")
        print(f"Tax Amount:    {tax_amount:.2f}")
        print(f"Net Salary:    {net_salary:.2f}")

    except ValueError:
        print("Invalid input! Please enter numeric values where required.")

# Run the program
if __name__ == "__main__":
    run_salary_calculator()