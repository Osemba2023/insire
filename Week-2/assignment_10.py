# write a program that calculates 5% tax on income beloww 100k, 16% tax on income ranging 100k- 150k #19%vtax if income is between 150k-300k  #30% if income is above 300k  #5% if income is than 100k  #print gross income and net income


gross_income=int(input("what is your gross:"))
tax_group_a=gross_income *0.05
tax_group_b=gross_income *0.16
tax_group_c=gross_income *0.19
tax_group_d=gross_income *0.30

if gross_income<100000:
   print("gross income", gross_income)
   print("net income", gross_income -tax_group_a ) 

elif(gross_income > 100000) & (gross_income < 150000):
    print("gross income", gross_income)
    print("net income", gross_income - tax_group_b)

elif(gross_income > 150001) & (gross_income < 300000):
     print("gross income", gross_income)
     print("net income", gross_income - tax_group_c)

else:
    print("gross income",gross_income)
    print("net income",gross_income-tax_group_d)

