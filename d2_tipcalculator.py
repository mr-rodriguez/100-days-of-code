#Prints the greeting
print("Welcome to the tip Calculator!")

#Prompt for inputting bill amount
billq = input("What was the total bill?: $")

#Prompt for inputting given tip amount
tipq = input("What percentage tip would you like to give? 18, 20, or 22?: ")

#Prompt for inputting number of people to split bill with
pplq = input("How many people to split the bill: ")

#Converting above inputs from strings to integers/float. Can also simply put int() in the variables above for less code
num_ppl = int(pplq)
bill_amt = float(billq)
tip_amt = int(tipq) / 100 + 1

#Formatting variable to round the output upto 2 decimal places
pmt_per_person = format((bill_amt * tip_amt) / num_ppl,".2f")

#f-String, which converts data types within a string
result = (f"Each person should pay: ${pmt_per_person}")

print(result)
