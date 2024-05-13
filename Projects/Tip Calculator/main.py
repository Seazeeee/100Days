#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calc!")

total_bill = float(input("What was the total bill? $"))

tip_percent = int(input("How much would you like to tip? (12, 15, 20) ")) / 100

amount_people = int(input("How many people to split the bill? "))

total_amount = ( total_bill / amount_people) * (1 + tip_percent)

total = f"Each person should pay: ${total_amount:.2f}"

print(total)