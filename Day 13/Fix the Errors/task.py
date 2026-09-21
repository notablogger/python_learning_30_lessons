try:
    age = int(input("How old are you?"))
except ValueError:
    print("Sorry, you entered wrong input, you shall insert your aga in numeric form, ex 12r")
    age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")
