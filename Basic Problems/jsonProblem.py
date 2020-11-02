Student1 = '{"english": 90, "maths": 50,"science": 80}'

Student2 = '{"english": 70,"maths": 70,"science": 70}'

import json


def average_marks(stud1, stud2):
    student_1 = json.loads(stud1)
    student_2 = json.loads(stud2)
    total = {}
    for keys in student_1.keys():
        total[keys] = int((student_1[keys] + student_2[keys]) / 2)
    return json.dumps(total)


print(average_marks(Student1, Student2))

# # Output:
#
# Total = {
#     "english": 80,
#     "maths": 60,
#     "science": 75
# }
