year=int(input(" input year to check is it is a Leap-year: "))

if (year%100==0)and(year%400==0):
    print("This year is a leap year")

elif (year%4==0):
    print(" it is leap year")

else:
    print("it is not a leap year")
    
        
    
