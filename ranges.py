#Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
def find():
    numb = range (1500,2701)
    for i in numb:
        if i % 7 == 0  and i % 5 == 0:
            print (i)
    


# num = [int(input("enter a no please: "))]
# numb = [num]
find()

#print()
