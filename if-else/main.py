# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird
# Input Format

# A single line containing a positive integer, .

n = int(input().strip())

if (n%2 == 1):
    print('Weird')
else:
    if (n>=2 and n<=5):
        print('Not Weird')
    elif (n>=6 and n<=20):
        print('Weird')
    if (n>20):
        print('Not Weird')
        
    