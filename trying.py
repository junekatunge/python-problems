
def calculate(score):
    if score >= 70 and score <= 100:
        print ("Congratulations you scored an A!! Hongera!")
    elif score >= 60 and score <= 69:
        print ("Congratulations you scored B!")
    elif score >= 50 and score <= 59:
        print ("Congratulations you are almost there! You scored C")
    elif score >= 40 and score <= 49:
        print ("There is still room for improvement you scored D")
    elif score >= 0 and score <= 39:
        print ("There is still room for improvement you scored E")
    else:
        print("Invalid input")
               
marks = int(input("Enter your average score: "))
calculate(marks)
    

            
        