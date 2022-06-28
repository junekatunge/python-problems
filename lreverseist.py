rl = ["bananas","watermelon","sugar","whippingcream","donut"]
def reverse(rl):
    start_index = 0
    end_index = len(rl) - 1
    
    while end_index > start_index:
        rl[start_index],rl[end_index] = rl[end_index],rl[start_index]
        start_index += 1
        end_index -= 1
    
    print (rl)

reverse(rl)
    