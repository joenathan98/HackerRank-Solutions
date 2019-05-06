if __name__ == '__main__':
    studentsAndScores = []
    scores = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        studentsAndScores.append([])
        for j in range(1):
            studentsAndScores[i].append(name)
            studentsAndScores[i].append(score)

    studentsAndScores.sort(key = lambda x: x[1])
    sec_Low = studentsAndScores[0][1]
    for i in range(len(studentsAndScores)):
        if sec_Low < studentsAndScores[i][1]:
            sec_Low = studentsAndScores[i][1]
            break
        
    studentNames = []
    for i in range(len(studentsAndScores)):
        if studentsAndScores[i][1] == sec_Low:
            studentNames.append(studentsAndScores[i][0]) 

    studentNames.sort()

    for i in studentNames:
        print(i)