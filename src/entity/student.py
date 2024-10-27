from src.enum.exam import ExamType
from src.utils.deleteNan import delete_nan
from src.utils.mean import mean
import math

class Student:
    exam_factor = 0.6
    final_exam_factor = 0.6

    submissions_factor = 1 - exam_factor
    midterm_exam_factor = 1 - final_exam_factor

    def __init__(self, id, submissions, grades):
        self.id = id
        self.submissions = submissions
        self.exams = grades

    def _exam_grade(self, type):
        if len(self.exams) == 0:
            return None

        for exam in self.exams:
            if exam.type == type:
                if exam.grade == None or math.isnan(exam.grade):
                    return None
                else:
                    return exam.grade

        return None

    def mean_submission(self):
        if len(self.submissions) == 0:
            return 0
        total = sum([(delete_nan(submission.grade) /submission.activity.maxGrade) * 10 for submission in self.submissions])
        return total / len(self.submissions)

    def mean_tried(self):
        tried_times = [submission.time_tried for submission in self.submissions if
                       submission.time_tried is not None]
        return mean(tried_times) if tried_times else 0

    def final_grade(self):
        exam_midterm = self._exam_grade(ExamType.Midterm)
        exam_final = self._exam_grade(ExamType.Final)
        exam_makeup = self._exam_grade(ExamType.Makeup)

        mean_submissions = self.mean_submission()

        if exam_midterm == None and delete_nan(exam_final) > 0 and exam_final > delete_nan(exam_makeup):
            return exam_final * self.exam_factor + mean_submissions * self.submissions_factor
        elif exam_makeup == None and delete_nan(exam_final) > 0 and delete_nan(exam_final) < delete_nan(exam_makeup):
            return exam_makeup * self.exam_factor + mean_submissions * self.submissions_factor
        elif delete_nan(exam_midterm) > 0 and delete_nan(exam_final) > 0:
            return (exam_midterm * self.midterm_exam_factor + exam_final * self.final_exam_factor) * self.exam_factor + mean_submissions * self.submissions_factor
        elif delete_nan(exam_makeup) > 0:
            return exam_makeup * self.exam_factor + mean_submissions * self.submissions_factor
        else:
            return 0

    def statics(self):

        return {
            'n_submissions': len(self.submissions),
            'mean_submissions': self.mean_submission(),
            'exam_midterm': self._exam_grade(ExamType.Midterm),
            'exam_final': self._exam_grade(ExamType.Final),
            "exam_makeup": self._exam_grade(ExamType.Makeup),
            'n_tried': self.mean_tried(),
            'final_grade': self.final_grade()
        }

    def is_assessable(self):
        return (delete_nan(self._exam_grade(ExamType.Midterm)) > 0 and delete_nan(self._exam_grade(ExamType.Final)) > 0) or (
                delete_nan(self._exam_grade(ExamType.Makeup)) > 0 or (delete_nan(self._exam_grade(ExamType.Final)) > 0)
        )

    def print(self):
        print(self.statics())