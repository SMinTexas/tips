#Prompt the user for two things:
# The total bill amount
# The level of service
#    Good
#    Fair
#    Bad
#Calculate the tip amount and the total amount
#(bill amount + tip amount).
#The tip percentage based on the level of service is based on:
# Good -> 20%
# Fair -> 15%
# Bad -> 10%

bill_amount = float(input('Total Bill Amount? '))
total_bill_amount = "${:.2f}".format(bill_amount)
service = input('Level of Service? ')
tip = 0
tip_amount = 0

if service == 'Good' or service == 'good':
    tip = bill_amount * .20
    print(f'Tip amount: {"${:.2f}".format(tip)}')
elif service == 'Fair' or service == 'fair':
    tip = bill_amount * .15
    print(f'Tip amount: {"${:.2f}".format(tip)}')
elif service == 'Bad' or service == 'bad':
    tip = bill_amount * .10
    print(f'Tip amount: {"${:.2f}".format(tip)}')

total_amount = bill_amount + tip
print(f'Total amount: {"${:.2f}".format(total_amount)}')
