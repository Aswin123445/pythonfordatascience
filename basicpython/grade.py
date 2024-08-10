#python program to find the grade in the academic year 
class GradeCalculator:
    written_m=70
    lab_m=20
    ass_m=10
    def __init__(self,mark_w,mark_l,mark_a):
        self.mark_w=mark_w
        self.mark_l=mark_l
        self.mark_a=mark_a
    def calculate_grade(self):
        percetage=(self.mark_w*70/100)+(self.mark_l*20/100)+(self.mark_a*10/100)
        print(percetage)
aswin=GradeCalculator(100,80,100)
aswin.calculate_grade()