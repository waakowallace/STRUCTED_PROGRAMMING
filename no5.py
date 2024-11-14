# amke as letter  to represnt a number 
n = 2
while n < 20:
    # set a flag
    prime_no=True
    for i in range (2,int(n**0.5)+1):
        if n ==0:
            prime_no=False
            print(n)

