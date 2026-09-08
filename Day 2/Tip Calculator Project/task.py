print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip=(bill*tip)/100
bill+=tip

bill_pp = bill / people
print(f"Each person should pay {bill_pp}")
share=round((bill_pp), 2)
print(f"round of value {share}")