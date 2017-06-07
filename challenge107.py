x = 2
x_sum = 0

while (x_sum < 1000000):
    x_sum = x * x 
    if (x_sum < 1000000):
        x += 1
    else:
        perfect_square = (x-1) * (x-1)
        print( perfect_square )
        break
    