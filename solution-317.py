#nested loops, use for loops 


#display the triangle patterns separately
 
n=11;
for i in range(0,n):
    for j in range(0,10-i):
        print ('* ', end=" ")
    print('')

for i in range(0,n):
    for j in range(10-i-1):
        print('* ', end=" ")
    print('')

for i in range(0,n):
    for j in range(n-1):
        print('* ', end=" ")
    print('')
#separate with a blank line in between 

