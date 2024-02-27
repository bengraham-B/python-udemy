import math
def paint_calc(height, width, cover):
    
    #area 
    area = width * height
    amount_of_paint_cans = area / cover
    rounded_num = math.ceil(amount_of_paint_cans)
    return print(f"You'll will need {rounded_num} cans of paint.")



test_h = int(input())
test_w = int(input())
coverage = 5

paint_calc(height=test_h, width=test_w, cover=coverage)
    