#write a program to list all odd numbers from 1-100
    
print("***The values below are odd numbers***")
for odd_numbers in range(1,101):
    if(odd_numbers%2 != 0):
        print(odd_numbers)