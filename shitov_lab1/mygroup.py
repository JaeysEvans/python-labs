# Список студентов
groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван", 
        "surname": "Петров",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов", 
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    }
]

# Функция для вывода студентов в виде таблицы
def print_students(students):
    print("Имя".ljust(15), "Фамилия".ljust(10), "Экзамены".ljust(30), "Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15), student["surname"].ljust(10), 
              str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))

# Функция для фильтрации по среднему баллу
def filter_students_by_average(students, min_average):
    filtered_students = []
    for student in students:
        # Считаем средний балл
        average = sum(student["marks"]) / len(student["marks"])
        if average >= min_average:
            filtered_students.append(student)
    return filtered_students

# Основная программа
print("Все студенты:")
print_students(groupmates)
    
print("\n" + "="*50)
    
try:
    # Запрашиваем у пользователя минимальный балл
    min_avg = float(input("Введите минимальный средний балл для фильтрации: "))
    
    # Фильтруем студентов
    filtered = filter_students_by_average(groupmates, min_avg)
    
    # Выводим результат
    print(f"\nСтуденты со средним баллом >= {min_avg}:")
    if filtered:
        print_students(filtered)
    else:
        print("Нет студентов с таким средним баллом")
except ValueError:
    print("Ошибка! Введите число для среднего балла")