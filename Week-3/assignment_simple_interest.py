#write a factorial to calculate simple interest

def simple_interest(principle,rate,time):
    p=float(input("enter the principle"))
    r=float(input("enter the rate"))
    t=float(input("enter the time in years"))
    simple_interest =p*r*t
    print(simple_interest)
