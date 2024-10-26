class Activity:
    def __init__(self, id, name, classroomId, dateInit, dateEnd, maxGrade, submissions):
        self._id = id
        self._name = name
        self._classId = classroomId
        self._initialDate = dateInit
        self._finalDate = dateEnd
        self._maxGrade = maxGrade
        self._submisions = submissions