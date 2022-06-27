celsius = float(input("Enter temperature in celsius: ")) 
fahren = float(input("Enter temperature in Fahrenheit : "))

def change_temp_fahren(temp):
    if celsius:
        temp = (celsius * 9/5) + 32
        print ("Temperature in Fahrenheit is ",temp,"Fahr")
    

change_temp_fahren(celsius)

def change_temp_celsius(temp):
    if fahren:
        temp = (fahren - 32) * 5/9
        print ("Temperature in Celsius is ",temp,"C")
    
        
change_temp_celsius(fahren)
        