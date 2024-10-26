from random import gauss, randint
import exam
import student
import submission

class SyntheticData:
    def __init__(trameses, activitats, notes):
        self.trameses = trameses
        self.activitats = activitats
        self.notes = notes

    def generate_gauss(value_list):
                
        average = 0
        for value in value_list:
            average += value
        average /= value_list.len()
        
        desviation = 0
        for value in value_list:
            desviation += value - average
        desviation /= value_list.len()

        random_number = random.gauss(average, desviation)
        return random_number

    
    def generate_exam(notes,type, classroom):
        grade_list = notes[type]
        grade = generate_gauss(grade_list)
        return exam(type, classroom, grade)
    
    def generate_submission(id, trameses):
        date_upload = generate_gauss(trameses[date_upload])
        grade = generate_gauss(trameses[grade])
        date_evaluated = generate_gauss(trameses[date_evaluated])
        time_tried = generate_gauss(trameses[time_tried])

        return submission(id, date_upload, grade, date_evaluated, time_tried)
    
    def generate_student(id,trameses,notes):
        
        submission_ids = []
        ##calculate the next disponible submission id
        next_id = 0
        n = randint(0,3)
        for i in range(0,n):
            submission_ids.append(next_id)
            next_id += 1
        
        exam_ids = []
        ##calculate the next disponible exam id
        next_id = 0
        n = randint(1,3)
        for i in range(0,n):
            exam_ids.append(next_id)
            next_id += 1
        
        submissions = []
        exams = []
        
        for submission in submission_ids:
            submissions.append(generate_submission(submission, trameses))

        for exam in exam_ids:
            exams.append(generate_exam(exam, notes))

        return student(id, submissions, exams)