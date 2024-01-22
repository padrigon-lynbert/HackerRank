n = int(input())

# student_marks = {'mimi': [11.0, 12.0]}
student_marks = {}

import statistics as stats

for i in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

query_name = input()
result = stats.mean(student_marks[query_name])
format_result = format(result, '.2f')
print(format_result)