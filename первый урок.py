grades = {
    'Иванов': 4,
    'Петров': 5,
    'Сидоров': 3
}


def add_student(name, grade):
    grades[name] = grade
    print(f"Добавлен {name} с оценкой {grade}")


def change_grade(name, new_grade):
    if name in grades:
        grades[name] = new_grade
        print(f"У {name} новая оценка: {new_grade}")
    else:
        print(f"Студент {name} не найден")


def get_average():
    if not grades:
        return 0
    avg = sum(grades.values()) / len(grades)
    print(f"Средний балл: {avg:.2f}")
    return avg


def find_best():
    if not grades:
        return None

    best_name = None
    best_grade = -1

    for name, grade in grades.items():
        if grade > best_grade:
            best_name = name
            best_grade = grade

    print(f"Лучший: {best_name} с оценкой {best_grade}")
    return (best_name, best_grade)


add_student('Смирнов', 5)
change_grade('Иванов', 5)
get_average()
find_best()

print("\nТекущие оценки:")
for name, grade in grades.items():
    print(f"{name}: {grade}")
