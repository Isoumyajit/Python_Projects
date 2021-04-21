class student:
    marks = {}

    def __init__(self, name, given_number):
        self.__name = name
        student.marks[name] = given_number

    @staticmethod
    def display_data():
        for data in student.marks:
            print(data)


if __name__ == "__main__":
    number = int(input("Enter the number of students ::"))
    for i in range(0, number):
        student_name = input(f"Enter name of student{i + 1}")
        mark = float(input(f"Enter the marks of {student_name}"))
        obj = student(student_name, mark)
    print(student.marks)
