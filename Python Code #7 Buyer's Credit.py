#Example: Buyer Credit
    
price = 1000000

buyer_credit = input("Is the Buyer's credit good? True or False? ")
    
if buyer_credit == "True":
        
        put_down = .1 * price
        print(f'You need to put down: ${put_down}')
    
elif buyer_credit == "False":
        
        put_down = .2 * price
        print(f'You need to put down: ${put_down}')
        
else:
        print("Invalid Input")
        