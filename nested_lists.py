if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
       
        if (len(students) == 0 or students[0][1] >= score):
            student = [name, score]
            students.insert(0, student)   
        else:
            added = False
            for i in range(1,len(students)):
                if students[i][1] > score:
                    student = [name, score]
                    students.insert(i, student)
                    added = True
                    break
            if not added:
                student = [name, score]
                students.append(student)    
                
    lowest_grade_students =[]
    if (students[1][1] != students[2][1] and students[1][1] != students[0][1]):
        lowest_grade_students.append(students[1][0])
    elif (students[1][1] != students[0][1]):
        score = students[1][1]
        for student in students:
            if student[1] == score:
                lowest_grade_students.append(student[0])
            elif student[1] > score:
                break
    else:
        lowest_score = students[0][1]
        next_score = -100
        for student in students:
            if student[1] > lowest_score:
                if next_score == -100:
                    next_score = student[1]
                elif next_score < student[1]:
                    break
                lowest_grade_students.append(student[0])
     
    lowest_grade_students.sort
    for student in lowest_grade_students:
        print(student)
                    
        
