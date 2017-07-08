if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    highest = -101
    second_highest = -101
    
    for x in arr:
        if x > highest:
            second_highest = highest
            highest = x
        elif x > second_highest and x != highest :
            second_highest = x
            
    print(second_highest)
            