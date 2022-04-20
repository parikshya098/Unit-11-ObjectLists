class Student():
    def __init__(self,firstname, lastname, tnumber):
      self.firstname = firstname
      self.lastname = lastname
      self.tnumber = tnumber
      self.courses = []

class StudentList():
    def __init__(self):
      self.studentList = []
      def add_student(self, firstname, lastname, tnumber):
        self.studentList.append(Student(firstname,lastname,tnumber))
      def find_student(self, studenttofind):
        for i in range(len(self.studentList)):
            if(self.studentList[i].tnumber == studenttofind):
              return i;
              return -1
      def print_student_list(self):
        print("Name\t\t\tTNumber\t\tCourses")
        for student in self.studentList:
          print(student.firstname,student.lastname,"\t\t",student.tnumber,"\t",end='')
        for course in student.courses:
          print(course.number,' ',end = ' ')
          print()
      def add_student_from_file(self, filename):
          filename = open('11.03 Students.txt')
          lines = filename.readlines()
          for line in lines:
            line = line.strip().split(',')
            self.studentList.append(Student(line[0],line[1],line[2]))

class Course():
    def __init__(self,department, number, name, room, meetingtimes):
      self.department=department
      self.number=number
      self.name=name
      self.room=room
      self.meetingtimes=meetingtimes

class CourseList():
    def __init__(self):
      self.courseList=[]
      def add_course(self, department, number, name, room, meetingtimes):
          self.courseList.append(Course(department, number, name, room, meetingtimes))
      def find_course(self, departmenttofind, numbertofind):
        for i in range(len(self.courseList)):
          if self.courseList[i].department==departmenttofind and self.courseList[i].number==numbertofind:
            return i
            return -1
      def add_course_from_file(self, file):
          file=open("11.03 Courses.txt")
          lines=file.readlines()
          for line in lines:
            line=line.strip().split(',')
            self.courseList.append(Course(line[0],line[1],line[2],line[3],line[4]))

      if __name__ == "__main__":
        courseList = CourseList()
        courseList.CourseList("11.03 Courses.txt")
        studentList = StudentList()
        studentList.StudentList("11.03 Students.txt")
        file = open("11.03 Registration.txt")
        lines = file.readlines()
        for line in lines:
          line = line.strip().split(',')
          index1 = studentList.find_student(line[0])
          index2 = courseList.find_course(line[1],line[2])
          if(index1>= 0 and index2>= 0):
            studentList.studentList[index1].courses.append(Course(courseList.courseList[index2].department,courseList.courseList[index2].number,courseList.courseList[index2].name,courseList.courseList[index2].room,courseList.courseList[index2].meetingtimes))

            studentList.print_student_list()