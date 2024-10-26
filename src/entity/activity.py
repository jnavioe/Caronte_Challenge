class Activity:
    def __init__(self, activity, submits):
        self._id = activity['activitat_id']
        self._name = activity['activitat']
        self._classId = activity['aula_id']
        self._initialDate = activity['startdate']
        self._finalDate = activity['duedate']
        self._maxGrade = activity['grade']
        self._submisions = submits