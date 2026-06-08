print("-----Income Expenditure App-----")

def main():
    # Get user input
    month = input("Enter the month: ")
    year = input("Enter the year: ")
    monthly_income = float(input("Enter your monthly income: "))
    days = float(input("Enter the number of expenditure days: "))
    daily_expenditure = float(input("Enter your average daily expenditure: "))
    
    # Calculate total monthly expenditure
    total_expenditure = daily_expenditure * days  
    
    # Calculate savings
    savings = monthly_income - total_expenditure
    
    # Display results
    print("\n--- Income & Expenditure Report ---")
    print(f"Month: {month}, Year: {year}")
    print(f"Total Monthly Income: {monthly_income:.2f} cedis")
    print(f"Total Monthly Expenditure: {total_expenditure:.2f} cedis")
    print(f"Savings: {savings:.2f} cedis")
    
    # Determine financial status
    if savings > 0:
        print("Great! You are saving money this month.")
    elif savings < 0:
        print("Warning! You are overspending this month.")
    else:
        print("You have exactly balanced your income and expenditure.")

if __name__ == "__main__":
    main()
