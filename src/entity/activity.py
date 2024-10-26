class Activity:
    def __init__(self, id, name, classroomId, dateInit, dateEnd, maxGrade, submissions):
        self.id = id
        self.name = name
        self.classId = classroomId
        self.initialDate = dateInit
        self.finalDate = dateEnd
        self.maxGrade = maxGrade
        self.submisions = submissions