# Write a function that takes a mark
# and returns the grade
# mark >= 85 --> A
# 85 > mark >= 75 --> B
# 75 > Mark >= 65 --> C
# 65 > Mark >= 50 --> D
# else F

# Let's discuss all side cases, handle them via assertions

class Pen():
    def __init__(self):
        pass


def grade(score):
    grade = ''
    assert type(score) == int
    assert score <= 110
    assert score >= 0

    if score >=85:
        grade = 'A'
    elif score >= 75:
        grade = 'B'
    elif score >= 65:
        grade = 'C'
    elif score >= 50:
        grade = 'D'
    elif score >= 0:
        grade = 'F'
    
    return grade

y = grade(20)
    













# def Grade(score):
#     assert type(score) == int
#     print("AYMAN")
#     assert score >= 0

#     grade = ''
#     if score >= 85:
#         grade = "A"

#     elif score >= 75:
#         grade = "B"
    
#     elif score >= 65:
#         grade = "c"

#     elif score >= 50:
#         grade = "d"
    
#     else:
#         grade = "f"

#     print(grade)
#     return grade

# g = Grade('9')







# Write a program that:
# 1- Opens a file called "grade.txt"
# 2- Read its content
# 3- Reads the grade score and calculates the grade Letter
# 4- Displays the grade (A or B or C or D or F)
# 5- Writes the Letter in another file called "Letter.txt"

# HANDLE ALL SIDE CASES via Assert