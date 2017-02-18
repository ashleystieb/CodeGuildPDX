
class Student:

    def __init__(self,name,year,*args,**kwargs):

        self.name = name
        self.year = int(year)
        self.grade = float(0.0)
        self.scores = [100]

    def get_name(self):
        return self.name


    def get_year(self):
        return self.year

    def get_scores(self):
        score_sum = 0
        for i in self.scores:
            score_sum = score_sum + i
        return (score_sum / (100 * len(self.scores))) * 100


    def add_score(self,score,*args,**kwargs):
        self.scores.append(score)

    def get_grade(self):
        # set grade to be equal to the get_scores function
        self.grade = self.get_scores()
        if self.grade <= 100 and self.grade >= 90:
            return "A"
        elif self.grade <= 89 and self.grade >= 80:
            return "B"
        elif self.grade <= 79 and self.grade >= 70:
            return "C"
        elif self.grade <= 69 and self.grade >= 60:
            return 'D'
        elif self.grade <= 59:
            return 'F'
        print(self.grade)