# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(H):
    num_of_bricks = 0  
    last_hight = -1
    min_hight_stack = []
    for hight in H:
        if hight > last_hight:
            num_of_bricks += 1
            min_hight_stack.append(hight)
        elif hight < last_hight:
            close_min = min_hight_stack.pop()
            while len(min_hight_stack) and hight < close_min:
                close_min = min_hight_stack.pop()
            if hight != close_min:
                if hight > close_min:
                    min_hight_stack.append(close_min)
                num_of_bricks += 1
            min_hight_stack.append(hight)
           
        
        last_hight = hight
        print(num_of_bricks, min_hight_stack)

    return num_of_bricks
