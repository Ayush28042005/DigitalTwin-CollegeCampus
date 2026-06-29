import json
from building import Classroom, Laboratory
from person import Student, Faculty
from datetime import datetime

class Campus:
    def __init__(self, college_name, filename="data.json"):
        self.college_name = college_name
        self.buildings = []
        self.persons = []
        self.filename = filename
        self.load_data()

    def load_data(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                for b in data.get("buildings", []):
                    if b["type"] == "classroom":
                        self.buildings.append(Classroom.from_dict(b))
                    elif b["type"] == "laboratory":
                        self.buildings.append(Laboratory.from_dict(b))
                for p in data.get("persons", []):
                    if p["type"] == "student":
                        self.persons.append(Student.from_dict(p))
                    elif p["type"] == "faculty":
                        self.persons.append(Faculty.from_dict(p))
        except (FileNotFoundError, json.JSONDecodeError):
            self.buildings = []
            self.persons = []

    def save_data(self):
        with open(self.filename, "w") as f:
            json.dump({
                "buildings": [b.to_dict() for b in self.buildings],
                "persons": [p.to_dict() for p in self.persons]
            }, f, indent=4)

    def add_classroom(self, entity_id, name, capacity, subject):
        for b in self.buildings:
            if b.entity_id == entity_id:
                print(f"❌ ID '{entity_id}' already exists!")
                return
        classroom = Classroom(entity_id, name, capacity, subject)
        self.buildings.append(classroom)
        self.save_data()
        print(f"✅ Classroom '{name}' added!")

    def add_laboratory(self, entity_id, name, capacity, lab_type):
        for b in self.buildings:
            if b.entity_id == entity_id:
                print(f"❌ ID '{entity_id}' already exists!")
                return
        lab = Laboratory(entity_id, name, capacity, lab_type)
        self.buildings.append(lab)
        self.save_data()
        print(f"✅ Laboratory '{name}' added!")

    def add_student(self, entity_id, name, age, email, roll_number, semester):
        for p in self.persons:
            if p.entity_id == entity_id:
                print(f"❌ ID '{entity_id}' already exists!")
                return
        student = Student(entity_id, name, age, email, roll_number, semester)
        self.persons.append(student)
        self.save_data()
        print(f"✅ Student '{name}' added!")

    def add_faculty(self, entity_id, name, age, email, employee_id, department):
        for p in self.persons:
            if p.entity_id == entity_id:
                print(f"❌ ID '{entity_id}' already exists!")
                return
        faculty = Faculty(entity_id, name, age, email, employee_id, department)
        self.persons.append(faculty)
        self.save_data()
        print(f"✅ Faculty '{name}' added!")

    def get_building(self, entity_id):
        for b in self.buildings:
            if b.entity_id == entity_id:
                return b
        return None

    def get_person(self, entity_id):
        for p in self.persons:
            if p.entity_id == entity_id:
                return p
        return None

    def assign_student_to_classroom(self, student_id, classroom_id):
        student = self.get_person(student_id)
        classroom = self.get_building(classroom_id)
        if not student:
            print(f"❌ Student '{student_id}' not found!")
            return
        if not classroom:
            print(f"❌ Classroom '{classroom_id}' not found!")
            return
        if not isinstance(classroom, Classroom):
            print(f"❌ '{classroom_id}' is not a classroom!")
            return
        if classroom.add_occupant(student_id):
            student.enrolled_classrooms.append(classroom_id)
            self.save_data()
            print(f"✅ {student.name} assigned to {classroom.name}!")

    def mark_attendance(self, classroom_id, date, student_ids):
        classroom = self.get_building(classroom_id)
        if not classroom or not isinstance(classroom, Classroom):
            print(f"❌ Classroom '{classroom_id}' not found!")
            return
        classroom.mark_attendance(date, student_ids)
        for sid in student_ids:
            student = self.get_person(sid)
            if student and isinstance(student, Student):
                student.mark_present(date, classroom_id)
        self.save_data()

    def view_all_buildings(self):
        if not self.buildings:
            print("❌ No buildings found!")
            return
        print(f"\n=== Buildings in {self.college_name} ===")
        for b in self.buildings:
            print(b.get_info())

    def view_all_persons(self):
        if not self.persons:
            print("❌ No persons found!")
            return
        print(f"\n=== People in {self.college_name} ===")
        for p in self.persons:
            print(p.get_info())

    def view_campus_summary(self):
        students = [p for p in self.persons if isinstance(p, Student)]
        faculty = [p for p in self.persons if isinstance(p, Faculty)]
        classrooms = [b for b in self.buildings if isinstance(b, Classroom)]
        labs = [b for b in self.buildings if isinstance(b, Laboratory)]
        print(f"\n=== Campus Summary: {self.college_name} ===")
        print(f"🏢 Total Buildings : {len(self.buildings)}")
        print(f"📚 Classrooms      : {len(classrooms)}")
        print(f"🔬 Laboratories    : {len(labs)}")
        print(f"👥 Total People    : {len(self.persons)}")
        print(f"🎓 Students        : {len(students)}")
        print(f"👨‍🏫 Faculty         : {len(faculty)}")