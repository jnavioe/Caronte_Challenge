class Student:
    def __init__(self, id, submissions, grades):
        self.id = id
        self.submissions = submissions
        self.grades = grades

    def print(self):
        print("ID:", self.id, "; #Submissions:", len(self.submissions), "; #Grades:", len(self.grades))