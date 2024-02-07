# If the bill was $150.00, split between 5 people, with 12% tip. 

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇
print("Welcome to the Tip Calculator!")
bill = float(input("Enter the total bill amount: $"))
persons = int(input("Enter the total number of persons to share the bill: "))
tip = int(input("Enter the percentage of tip would you like to give? 10, 12, or 15?: "))

tip_percentage = tip/100
total_tip = bill * tip_percentage
total_bill = bill + total_tip
bill_share = total_bill/persons
final_amount = round(bill_share, 2)
print(f"Each person has to pay: ${final_amount}")
