if __name__ == '__main__':
    N = int(input())
    list = []
    for i in range (N):
        command = (input())
       
        if command == "print":
            print(list)
            
        if command == "sort":
            list.sort()
            
        if command == "pop":
            list.pop(-1)
            
        if command == "reverse":
            list.reverse()
            
        command = command.split(" ")
        #print(command)
        
        if command[0] == "insert":
            index = int(command[1])
            value = int(command[2])
            
            list.insert(index, value)
            
        if command[0] == "remove":  
            value = int(command[1])
            list.remove(value)
            
        if command[0] == "append":  
            value = int(command[1])
            list.append(value)