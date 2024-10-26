from src.entity.submission import Submission
from src.entity.activity import Activity
from src.entity.exam import Exam
from src.enum.exam import ExamType
from src.entity.student import Student
import pandas as pd
import csv
from src.utils.csv_paths import SUBMISSION_FILE, ACTIVITY_FILE, EXAM_FILE


class StudentProcessor:
    def __init__(self, submission_file=SUBMISSION_FILE, activity_file=ACTIVITY_FILE, exam_file=EXAM_FILE):
        self._submission_matrix = self._read_csv(submission_file)
        self._activities_matrix = self._read_csv(activity_file)
        self._exams_matrix = self._read_csv(exam_file)
        self._temp_activities = {}

    @staticmethod
    def default_csv_delimiter(file_path):
        with open(file_path, 'r') as file:
            first_line = file.readline()
            file.seek(0)
            dialect = csv.Sniffer().sniff(first_line)
        return dialect.delimiter

    @staticmethod
    def _read_csv(file_path):
        try:
            delimiter = StudentProcessor.default_csv_delimiter(file_path)
            data = pd.read_csv(file_path, delimiter=delimiter)
            if data.empty:
                raise ValueError(f"Error: CSV {file_path} is empty")
            return data
        except FileNotFoundError:
            raise FileNotFoundError(f"Error: file {file_path} not found.")
        except ValueError as e:
            raise ValueError(e)

    def _students_id(self):
        return list(set(self._exams_matrix['userid'].unique()))

    def _load_activities(self):
        activities_dict = {}
        for _, activity in self._activities_matrix.iterrows():
            act = Activity(
                id=activity["activitat_id"],
                name=activity["activitat"],
                classroomId=activity["aula_id"],
                dateInit=activity["startdate"],
                dateEnd=activity["duedate"],
                maxGrade=activity["grade"],
                submissions=[]
            )
            activities_dict[activity["activitat_id"]] = act
        return activities_dict

    def _find_activity_by_id(self, activity_id):
        return self._temp_activities.get(activity_id)

    def _submissions_by_user_id(self, user_id):
        filtered_submissions = self._submission_matrix[self._submission_matrix['userid'] == user_id]

        submissions_list = []
        for _, submission in filtered_submissions.iterrows():
            activity = self._find_activity_by_id(submission['activitat_id'])
            if activity:
                submissions_list.append(Submission(
                    id=submission['id'],
                    data_upload=submission['datesubmitted'],
                    grade=submission['grade'],
                    date_evaluated=submission['dategraded'],
                    time_tried=submission['nevaluations'],
                    activity=activity
                ))
        return submissions_list

    def _exams_by_user_id(self, user_id):
        exams_filtered = self._exams_matrix[self._exams_matrix["userid"] == user_id]
        exams_list = []
        for _, exam in exams_filtered.iterrows():
            if not pd.isna(exam["P_Grade"]):
                exams_list.append(Exam(ExamType.Midterm, exam["aula_id"], exam["P_Grade"]))
            elif not pd.isna(exam["F_Grade"]):
                exams_list.append(Exam(ExamType.Final, exam["aula_id"], exam["F_Grade"]))
            elif not pd.isna(exam["R_Grade"]):
                exams_list.append(Exam(ExamType.Makeup, exam["aula_id"], exam["R_Grade"]))
        return exams_list

    def process(self):
        self._temp_activities = self._load_activities()
        students_ids = self._students_id()
        students_list = []
        for student_id in students_ids:
            students_list.append(Student(
                id=student_id,
                submissions=self._submissions_by_user_id(student_id),
                grades=self._exams_by_user_id(student_id)
            ))
        return students_list