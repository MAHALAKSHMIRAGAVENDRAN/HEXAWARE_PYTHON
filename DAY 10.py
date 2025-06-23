class StudentManager:
    def __init__(self):
        self.students = {}

    def addStudent(self, rollnumber, studentname, marks):
        if rollnumber in self.students:
            print(f"Roll number {rollnumber} already exists.")
        else:
            self.students[rollnumber] = {"studentname": studentname, "marks": marks}
            print(f"{rollnumber} for the student {studentname} has been added.")

    def getStudent(self, rollnumber):
        if rollnumber in self.students:
            return self.students[rollnumber]
        else:
            return f"No student with roll number {rollnumber}"

    def getTopStudents(self, criteria):
        topstudents = [
            {"rollnumber": rollnumber, "studentname": data["studentname"], "marks": data["marks"]}
            for rollnumber, data in self.students.items()
            if data["marks"] > criteria
        ]
        return topstudents

result = StudentManager()

students_data = [
    {"rollnumber": 1234, "studentname": "Job", "marks": 85},
    {"rollnumber": 2345, "studentname": "Raj", "marks": 75},
    {"rollnumber": 3454, "studentname": "Alice", "marks": 91},
    {"rollnumber": 4567, "studentname": "Hari", "marks": 92}
]

for s in students_data:
    result.addStudent(s["rollnumber"], s["studentname"], s["marks"])


print(result.getStudent(1234))


print(result.getTopStudents(80))