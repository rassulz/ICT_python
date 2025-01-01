# Функция для вычисления среднего балла
def calculate_average(grades):
    grades_sum = sum(grades)
    grades_lenth = len(grades)
    total = grades_sum/grades_lenth
    return total
grades = []

for i in range(5):
    grade = int(input(f"Enter grade for student:  { i+1}"))
    grades.append(grade)


# Вычисляем средний балл и выводим его
average = calculate_average(grades)
print(f"Средний балл группы: {average:.1f}")
