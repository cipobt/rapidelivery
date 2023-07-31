#This program helps a courier company to calculate the cost of sending a parcel

#Adding colours to Xmas gift message later on
RED = '\033[91m'
WHITE = '\033[0m'

#Greeting the user and requesting initial input values
print("Welcome to RapiDelivery!")
original_price = float(input("What's the price of the package you wish to purchase today? "))
distance = float(input("What's the total distance to the recipient's address in kms please? "))

#Getting the user's preferences towards delivery costs
print("Choose one of the following please")

transportation_charge = int(input("Delivery options: \n1. By Air (R0.36) \n2. Other freight (R0.25) \n "))

insurance_charge = int(input("1. Full insurance (R50.00) \n2. Limited insurance (R25.00) \n "))

gift_charge = input(f"We can wrap your package as a {RED}Xmas present for just R15.00 extra! {WHITE}(Y/N)\n ").upper()

priority_charge = input("Is this a priority delivery? (Y/N)\nPriority R100.00\nStandard delivery R20.00 \n ").upper()

#Adding on the delivery costs to get the ﬁnal cost of the product in the order we requested them
if transportation_charge == 1:
    total_price = original_price + 0.36
else:
    total_price = original_price + 0.25

if insurance_charge == 1:
    total_price += 50
else:
    total_price += 25

if gift_charge == 'Y':
    total_price += 15

if priority_charge == 'Y':
    total_price += 100
else:
    total_price += 20

#Giving the user the final price
print("The total amount to pay to send your package today is " + str(total_price))