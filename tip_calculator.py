print("Welcome to the tip calculator!")
total_bill = input("What was the total bill?: $")
tip = input("""How much of a tip would you like to give? 
10%, 12%, or 15%? *just type the number*: """)
people = input("How many people to split the bill?: ")
payper_person = ((float(total_bill) * (float(tip)/100) + float(total_bill))) / float(people)
print(f"Each person should pay: ${round(payper_person, 2)}")

