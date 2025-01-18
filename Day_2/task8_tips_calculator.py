print("Welcome to the tip calculator!")
bill = float(input("what was the total bill?"))
print(bill)
tips = int(input("How much would you like to give? 10, 12, 0r 15?"))
print(tips)
people=int(input("How many people to split the bill?"))
pay= (bill/people)*(1+(tips/100))

print(f"Each person should pay: ${round(pay,2)}")