"""solution for 3.11 miles per gallon"""


result=[] 

#while loop
while True:  
    gallons = float(input("Enter the gallons used(-1 to end): ")) 
    if gallons < 0 : break 
    miles=float(input("enter the miles: ")) 
    m=miles/gallons   
    print('The miles/gallon for this tank is: ',m) 
    result.append(m)   
print("The overall average miles/gallon was: ",sum(result)/len(result)) 

