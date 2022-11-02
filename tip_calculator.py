# A simple tip calculator that helps remove any guess work.
#Splits the bill evenly across all party members.

print("Welcome to the tip calculator.")
bill_question = input("What was the total bill? $")
tip_question = input("What percentage tip would you like to give? 10, 12, or 15? ")
people_question = input("How many people to split the bill? ")
tip_percent = float(tip_question)
bill_val = float(bill_question)
split_val = int(people_question)
bill_total = ((tip_percent/100)+1) * (bill_val)
indv_bill = round(bill_total/split_val, 2)
final_amount = "{:.2f}".format(indv_bill)
print(f"Each person should pay: ${final_amount}")