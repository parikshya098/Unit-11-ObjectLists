class Employee:
    def __init__(self,firstname,lastname,id,hours,wage):
        self.FirstName = firstname
        self.LastName = lastname
        self.IDNumber = id
        self.HoursWorked = 0
        self.Wage = wage
    def WeeklyPay(self):
        if self.HoursWorked <= 40:
            return self.HoursWorked*self.Wage
        return (40*self.Wage)+((self.HoursWorked-40)*1.5*self.Wage)

print("   First    Last      ID   Hours  Hourly  Weekly\n    Name    Name  Number  Worked    Wage     Pay""")

file = open("11.02 Employees.txt", "r")

for line in file.readlines():
    e = line.split(',')
    e = Employee(e[0].strip(),e[1].strip(),int(e[2]),float(e[3]), float(e[4]))

file1 = open("11.02 Hours.txt", "r")

for line1 in file1.readlines():
        f = line1.split(',')
        f = Employee(int(f[0]), float(f[1])) 

    # print employee details
print("%8s%8s%8d%8.2f%8.2f%8.2f"%(e.FirstName,e.LastName,e.IDNumber,f.HoursWorked,e.Wage,e.WeeklyPay()))

# close file
file.close()