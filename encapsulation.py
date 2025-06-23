class EmployeeManager:
    def __init__(self):
        self.__employees = {}  # private dictionary

    def addEmployee(self, emp_id, emp_name, salary):
        if emp_id in self.__employees:
            print(f"Employee ID {emp_id} already exists.")
        else:
            self.__employees[emp_id] = {"emp_name": emp_name, "salary": salary}
            print(f"{emp_id} - {emp_name} added successfully.")

    def getEmployee(self, emp_id):
        if emp_id in self.__employees:
            return self.__employees[emp_id]
        else:
            return f"No employee with ID {emp_id}"

    def getTopEarners(self, threshold):
        top_earners = [
            {"emp_id": emp_id, "emp_name": data["emp_name"], "salary": data["salary"]}
            for emp_id, data in self.__employees.items()
            if data["salary"] > threshold
        ]
        return top_earners


# Object Creation
manager = EmployeeManager()

# Employee Data
employee_data = [
    {"emp_id": 101, "emp_name": "Maha", "salary": 55000},
    {"emp_id": 102, "emp_name": "John", "salary": 62000},
    {"emp_id": 103, "emp_name": "Sara", "salary": 48000},
    {"emp_id": 104, "emp_name": "Raj", "salary": 75000}
]

# Add Employees
for e in employee_data:
    manager.addEmployee(e["emp_id"], e["emp_name"], e["salary"])

# Get Single Employee
print(manager.getEmployee(102))

# Get Employees Earning More Than 60000
print(manager.getTopEarners(60000))

