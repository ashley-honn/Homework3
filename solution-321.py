#calculate change using fewest number of coins

n=int(input("Enter cost in cents:"))
change=100-(n)

#1 quarter is 25 cents
quarters=int(change//25)

#1 dime is 10 cents
dimes=int((change-25*quarters)//10) 

#1 penny is 1 cent
pennies=int((change-25*quarters-10*dimes))

print(quarters,"Quarters")
print(dimes,"Dimes")
print(pennies,"Pennies")

