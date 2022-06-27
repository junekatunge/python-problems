
# def discount(total_cost):
#     total_cost = number * 100
#     if total_cost > 1000:
#         total_pay = total_cost * 90/100
#         print(total_pay) 
#     else:
#         print (total_cost)
        
# number = int(input("Input the no of units: "))
# discount(number)
    
#alternatively using quantity

def discount(quantity):
    if quantity > 10:
        total_cost = number * 100
        total_pay = total_cost *90/100
        print ("The price is",total_pay)
        
number = int(input("Input the no of units you would like to purchase: "))
discount(number)