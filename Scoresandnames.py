if __name__ == '__main__':
 
    n = int(input())
    students = []
    for _ in range(n):
        name = input()
        grade = float(input())
        students.append([name, grade])
    scores = sorted(set([student[1] for student in students]))
    second_lowest_score = scores[1]
    second_lowest_students = [student[0] for student in students if student[1] == second_lowest_score]
    second_lowest_students.sort()
    for name in second_lowest_students:
        print(name)
