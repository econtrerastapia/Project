
class Logic:
    # This class contains all the logic
    def student_score(self, student_scores:list[str], students: int, focusing_student: int) -> str:
        '''
        Calculates the students grade based on their score compared to other student's scores

        :param student_scores: A list of the students scores
        :param students: The number of students
        :param focusing_student: The score of the student that's grade is being calculated
        :return: The score and grade for the specified student
        '''
        # Student_scores is converted to a list of integers
        self.scores = [int(num) for num in student_scores]


        list_of_scores = self.scores[0:students]

        # Sorts the scores in ascending order
        list_sorted = sorted(list_of_scores)

        # Gets us the highest score
        highest_score = list_sorted[-1]
        highest_score = int(highest_score)

        # Returns the correct final result
        if int(focusing_student) >= highest_score - 10:
            return f'Student score is {focusing_student} and grade is A'

        elif int(focusing_student) >= highest_score - 20:
            return f'Student score is {focusing_student} and grade is B'

        elif int(focusing_student) >= highest_score - 30:
            return f'Student score is {focusing_student} and grade is C'

        elif int(focusing_student) >= highest_score - 40:
            return f'Student score is {focusing_student} and grade is D'

        else:
            return f'Student score is {focusing_student} and grade is F'

