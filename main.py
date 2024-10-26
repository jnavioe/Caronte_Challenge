from src.modules.StudentProcessor import StudentProcessor

if __name__ == "__main__":
    students = StudentProcessor().process()
    for student in students:
        student.print()
