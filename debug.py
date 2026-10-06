def calculate_average(marks):
    total = sum(marks)
    return total / len(marks)


def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


marks = [85, 78, 92, 88, 76]

average = calculate_average(marks)
grade = get_grade(average)

print("Marks:", marks)
print("Average:", average)
print("Grade:", grade)