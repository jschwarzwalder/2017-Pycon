if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    if (query_name in student_marks):
        scores = student_marks[query_name]
        total_score = 0
        for score in scores:
            total_score += score
        
        avg = (total_score)/(len(scores)*1.0)
        print("%.2f" % avg  )