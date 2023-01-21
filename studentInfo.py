class StudentInfo:
  def __init__(self, id_num, name, grade, roll, sec):
    self.id_num = id_num
    self.name = name
    self.grade = grade
    self.roll = roll
    self.sec = sec
  
  def check(self):
    print(self.name + " " + self.roll + " " + self.sec + " " + self.grade)
    

student_id_num = input("Student's ID num: ")
student_name = input("Student's name: ")
student_roll = input("Student's roll: ")
student_sec = input("Student's sec: ")
student_grade = input("Student's grade: ")

student_object = StudentInfo(student_id_num, student_name, student_grade, student_roll, student_sec)
student_object.check()
print(student_object)
