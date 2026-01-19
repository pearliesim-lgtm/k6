def tip_calculator(bill,tip):
    tip_amount=bill*(tip/100)
    total_amount=bill + tip_amount
    print("Tip:",total_amount)
    print("Total amount:",total_amount)

bill=float(input("Enter the bill amount:"))
tip=float(input("Enter the tip percentage:"))
tip_calculator(bill,tip)