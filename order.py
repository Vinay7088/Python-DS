amount=float(input("Enter your expense amount : "))
choice=input("Do you wants to pay with credit card: ")
if amount>1000:
    amount=amount-(amount*3/100)
if choice=='yes':
    amount-=100
    #amount=amount-100
amount=amount+ amount*.18
print("Total payable amount:",amount)