print("Tip Calculator")
bill = float( input ( 'What was the total bill? $'))
tip = int(input('What percentage tip would you like to give? 10, 12, or 15?'))
people = int(input('How many people to split the bill?'))

tip_w_bill= tip /100 *bill + bill 

pay = tip_w_bill / people 
payment = "{:.2f}".format(pay)
print(f'Each person should pay {payment}')
