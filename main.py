#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
bill_start = float(input("What was the total bill? "))
tip_pct = int(input("How much tip would you like to give? 10, 12, or 15? "))
split_it = int(input("How many people to split the bill? "))
split_total = bill_start + (bill_start * (tip_pct/100))
final_share =  '{:.2f}'.format(split_total/split_it)
print(f"Each person should pay: ${final_share}")