def fuctorial(n):
    for i in range(0,n):
        fact_n=n*(n-i)
        return fact_n


#calling the fuction
fuctorial(3)
print(fuctorial(3))


#write a factorial to calculate simple interest
def simple_interest(principle,rate,time):
    p=float(input("enter the principle"))
    r=float(input("enter the rate"))
    t=float(input("enter the time in years"))
    simple_interest =p*r*t
    print(simple_interest)
   
    