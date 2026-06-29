from abc import ABC, abstractmethod
from campus_entity import CampusEntity

class Person(CampusEntity, ABC):
    def __init__(self, entity_id, name, age, email):
        super().__init__(entity_id, name)
        self.age = age                  # Person's age
        self.email = email              # Person's email

    @abstractmethod
    def get_role(self):
        pass                            # Every subclass must define their role

    def get_info(self):
        return f"{self.get_role()}: {self.name} | Age: {self.age} | Email: {self.email}"

    def to_dict(self):
        return {
            "entity_id": self.entity_id,
            "name": self.name,
            "age": self.age,
            "email": self.email
        }


class Student(Person):
    def __init__(self, entity_id, name, age, email, roll_number, semester):
        super().__init__(entity_id, name, age, email)
        self.roll_number = roll_number      # Student roll number
        self.semester = semester            # Current semester
        self.enrolled_classrooms = []       # List of classroom IDs
        self.attendance_record = {}         # {date: [classroom_ids present]}

    def get_role(self):
        return "🎓 Student"

    def mark_present(self, date, classroom_id):
        if date not in self.attendance_record:
            self.attendance_record[date] = []
        if classroom_id not in self.attendance_record[date]:
            self.attendance_record[date].append(classroom_id)

    def get_attendance_percentage(self, classroom_id, total_days):
        if total_days == 0:
            return 0
        days_present = sum(
            1 for classes in self.attendance_record.values()
            if classroom_id in classes
        )
        return round((days_present / total_days) * 100, 2)

    def get_info(self):
        return f"🎓 Student: {self.name} | Roll: {self.roll_number} | Semester: {self.semester} | Email: {self.email}"

    def to_dict(self):
        data = super().to_dict()
        data["roll_number"] = self.roll_number
        data["semester"] = self.semester
        data["enrolled_classrooms"] = self.enrolled_classrooms
        data["attendance_record"] = self.attendance_record
        data["type"] = "student"
        return data

    @classmethod
    def from_dict(cls, data):
        obj = cls(data["entity_id"], data["name"], data["age"],
                  data["email"], data["roll_number"], data["semester"])
        obj.enrolled_classrooms = data.get("enrolled_classrooms", [])
        obj.attendance_record = data.get("attendance_record", {})
        return obj


class Faculty(Person):
    def __init__(self, entity_id, name, age, email, employee_id, department):
        super().__init__(entity_id, name, age, email)
        self.employee_id = employee_id      # Faculty employee ID
        self.department = department        # Department name
        self.assigned_classrooms = []       # List of classroom IDs

    def get_role(self):
        return "👨‍🏫 Faculty"

    def assign_classroom(self, classroom_id):
        if classroom_id not in self.assigned_classrooms:
            self.assigned_classrooms.append(classroom_id)
            print(f"✅ {self.name} assigned to classroom {classroom_id}")

    def get_info(self):
        return f"👨‍🏫 Faculty: {self.name} | Emp ID: {self.employee_id} | Dept: {self.department} | Email: {self.email}"

    def to_dict(self):
        data = super().to_dict()
        data["employee_id"] = self.employee_id
        data["department"] = self.department
        data["assigned_classrooms"] = self.assigned_classrooms
        data["type"] = "faculty"
        return data

    @classmethod
    def from_dict(cls, data):
        obj = cls(data["entity_id"], data["name"], data["age"],
                  data["email"], data["employee_id"], data["department"])
        obj.assigned_classrooms = data.get("assigned_classrooms", [])
        return obj