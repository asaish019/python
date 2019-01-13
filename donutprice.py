price=int(input("Enter the price of a donut: Rs. "))
quantity=int(input("Enter the no. of donuts: "))
amount=price*quantity

if amount>100:
    print ("yaaa.. a dicount of 10% is applicable!")
    discount=amount*10/100
    amount= amount-discount
print ("yout total amount is: Rs. ",amount)
