try:
    n=int(input("enter number:"))
except ValueError:
    print("Enter only numbers")
else:
    temp=n
    rev=0
    while(n>0):
        rev=(rev*10)+(n%10)
        n=n//10
    if(temp==rev):
        print('palidrome')
    else:
        print('not a palindrome')
