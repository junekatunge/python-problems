# Write a function to accept rate, principle and time to calculate,  simple_interest
rate = float(input("Enter the rate: "))
principle = float(input("Enter the principle: "))
time = float(input("Enter the time: "))

def simple(rate,principle,time):
    simple_interest = principle*1+rate*time
    print("The Total amount is:",simple_interest)
    
simple(rate,principle,time)
 