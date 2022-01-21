n = int(input())

student_list= dict()

for i in range(n):
    # tmp = []
    name, score = input().split()
    student_list[name] = score

sorted_list = sorted(student_list.items(),reverse=False)

for i in sorted_list:
    print(i[0])