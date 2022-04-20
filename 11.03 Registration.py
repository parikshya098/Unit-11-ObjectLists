from prettytable import PrettyTable

class Course:
    def __init__(self, department="", number="", name="", room="", meetingtimes=""):
        self.department = department
        self.number = number
        self.name = name
        self.room = room
        self.meetingtimes = meetingtimes

class CourseList:
    def __init__(self, courseList=None):
        if courseList is None:
            courseList = []
        self.courseList = courseList
    def add_course(self, department, number, name, room, meetingtimes):
        temp = Course(department, number, name, room, meetingtimes)
        self.courseList.append(temp)
    def find_course(self, departmenttofind, numbertofind):
        for c in range(len(self.courseList)):
            if self.courseList[c].department == departmenttofind and self.courseList[c].number == numbertofind:
                return c
    def add_course_from_file(self, filename):
        file = open(filename, "r")
        for x in file:
            courseInformation = x.split(",")
            self.add_course(courseInformation[0], courseInformation[1], courseInformation[2], courseInformation[3],
                            courseInformation[4].strip())
    def print_course_list(self):
        for tempCoursee in self.courseList:
            print(tempCoursee)

class Student:
    def __init__(self, firstname="", lastname="", tnumber=""):
        self.enrolledCourses = []
        self.firstname = firstname
        self.lastname = lastname
        self.tnumber = tnumber

class StudentList:
    def __init__(self, studentList=None):
        if studentList is None:
            studentList = []
        self.studentList = studentList

    def add_student(self, firstName, lastName, tnumber):
        temp = Student(firstName, lastName, tnumber)
        self.studentList.append(temp)
    def find_student(self, studenttofind):
        for studentIndex in range(len(self.studentList)):
            if self.studentList[studentIndex].tnumber == studenttofind:
                return studentIndex
    def print_student_list(self):
        t = PrettyTable(['First Name', 'Last Name', 'T-Number', 'Course', '', 'Name', ' Room', 'Meeting Times'])
        t.border = False
        t.align = "l"
        for z in range(len(self.studentList)):
            studentCourse = self.studentList[z].enrolledCourses
            courses = "\n"
            numbers = "\n"
            names = "\n"
            room = "\n"
            meetingtimes = "\n"
            for q in range(len(studentCourse)):
                courses = courses + studentCourse[q].department
                numbers = numbers + studentCourse[q].number
                names = names + studentCourse[q].name
                room = room + studentCourse[q].room
                meetingtimes = meetingtimes + studentCourse[q].meetingtimes
                if q != len(studentCourse) - 1:
                    courses = courses + "\n"
                    numbers = numbers + "\n"
                    names = names + "\n"
                    room = room + "\n"
                    meetingtimes = meetingtimes + "\n"
            t.add_row(
                [self.studentList[z].firstname, self.studentList[z].lastname, self.studentList[z].tnumber, courses,
                 numbers, names, room, meetingtimes])
        print(t)
    def add_student_from_file(self, filename):
        file = open(filename, "r")
        for f in file:
            studentInformation = f.split(",")
            self.add_student(studentInformation[0], studentInformation[1], studentInformation[2].strip())

courseList1 = CourseList()
courseList1.add_course_from_file("11.03 Courses.txt")
studentList1 = StudentList()
studentList1.add_student_from_file("11.03 Students.txt")
regFile = open("11.03 Registration.txt", "r")
for i in regFile:
    line = i.split(",")
    tempCourse = courseList1.courseList[courseList1.find_course(line[1], line[2].strip())]
    studentList1.studentList[studentList1.find_student(str(line[0]))].enrolledCourses.append(tempCourse)
studentList1.print_student_list()