import json

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    def letter_grade(self):
        avg = self.average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    def to_dict(self):
        return {"name": self.name, "grades": self.grades, "average": self.average()}


def add_student(students, name, grades):
    students.append(Student(name, grades))
    return students


def get_top_student(students):
    if not students:
        return None
    top = students[0]
    for s in students:
        if s.average() > top.average():
            top = s
    return top


def class_stats(students):
    averages = [s.average() for s in students]
    stats = {}
    stats["class_size"] = len(students)
    stats["class_average"] = sum(averages) / len(averages) if averages else 0
    stats["highest"] = max(averages) if averages else 0
    stats["lowest"] = min(averages) if averages else 0
    return stats


def divide_grades(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("You can't divide by zero, returning 0 instead")
        return 0
    except TypeError:
        print("Grades must be numbers")
        return None


def save_to_file(students, filename):
    data = [s.to_dict() for s in students]
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)


def load_from_file(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("File not found, starting with empty list")
        return []


def main():
    students = []
    students = add_student(students, "Ana", [88, 92, 79])
    students = add_student(students, "Mihai", [65, 70, 72])
    students = add_student(students, "Ioana", [95, 91, 99])

    for s in students:
        print(s.name, "-> average:", round(s.average(), 2), "grade:", s.letter_grade())

    top = get_top_student(students)
    print("\nTop student:", top.name)

    stats = class_stats(students)
    print("\nClass stats:")
    for key, value in stats.items():
        print(key, ":", value)

    numbers = [10, 20, 0, 5]
    for n in numbers:
        result = divide_grades(100, n)
        print("100 /", n, "=", result)

    grade_lookup = {}
    for s in students:
        grade_lookup[s.name] = s.letter_grade()
    print("\nGrade lookup dictionary:", grade_lookup)

    save_to_file(students, "students.json")
    loaded = load_from_file("students.json")
    print("\nLoaded back from file:", loaded)


if __name__ == "__main__":
    main()
