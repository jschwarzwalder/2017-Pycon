if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    possible_sequence = []
    
    #For i in range x check all possible sets with j and k for sequence != n
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                sum = i + j + k
                if (sum != n):
                    possible_sequence.append([i, j, k])
                    
   
    print(possible_sequence)
    
    #Using list comprehension
    print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n])