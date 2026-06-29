from campus_entity import CampusEntity

class Building(CampusEntity):
    def __init__(self, entity_id, name, capacity):
        super().__init__(entity_id, name)
        self.capacity = capacity            # Max number of people
        self.current_occupants = []         # List of person IDs inside

    def get_occupancy(self):
        return len(self.current_occupants)

    def is_full(self):
        return len(self.current_occupants) >= self.capacity

    def add_occupant(self, person_id):
        if self.is_full():
            print(f"❌ {self.name} is full!")
            return False
        if person_id not in self.current_occupants:
            self.current_occupants.append(person_id)
            return True
        return False

    def get_info(self):
        return f"{self.name} | Capacity: {self.capacity} | Occupancy: {self.get_occupancy()}"

    def to_dict(self):
        return {
            "entity_id": self.entity_id,
            "name": self.name,
            "capacity": self.capacity,
            "current_occupants": self.current_occupants,
            "type": "building"
        }

    @classmethod
    def from_dict(cls, data):
        obj = cls(data["entity_id"], data["name"], data["capacity"])
        obj.current_occupants = data.get("current_occupants", [])
        return obj


class Classroom(Building):
    def __init__(self, entity_id, name, capacity, subject):
        super().__init__(entity_id, name, capacity)
        self.subject = subject              # Subject taught here
        self.attendance = {}                # {date: [student_ids present]}

    def mark_attendance(self, date, student_ids):
        self.attendance[date] = student_ids
        print(f"✅ Attendance marked for {self.name} on {date}")

    def get_occupancy(self):
        # Polymorphism — Classroom counts enrolled students
        return len(self.current_occupants)

    def get_info(self):
        return f"📚 Classroom: {self.name} | Subject: {self.subject} | Capacity: {self.capacity} | Enrolled: {self.get_occupancy()}"

    def to_dict(self):
        data = super().to_dict()
        data["subject"] = self.subject
        data["attendance"] = self.attendance
        data["type"] = "classroom"
        return data

    @classmethod
    def from_dict(cls, data):
        obj = cls(data["entity_id"], data["name"], data["capacity"], data["subject"])
        obj.current_occupants = data.get("current_occupants", [])
        obj.attendance = data.get("attendance", {})
        return obj


class Laboratory(Building):
    def __init__(self, entity_id, name, capacity, lab_type):
        super().__init__(entity_id, name, capacity)
        self.lab_type = lab_type            # e.g. Computer, Chemistry, Physics
        self.equipment = []                 # List of equipment in lab

    def add_equipment(self, item):
        self.equipment.append(item)
        print(f"✅ Equipment '{item}' added to {self.name}")

    def get_occupancy(self):
        # Polymorphism — Laboratory counts at 50% safe capacity
        return f"{len(self.current_occupants)}/{self.capacity} (Safe limit: {self.capacity // 2})"

    def get_info(self):
        return f"🔬 Laboratory: {self.name} | Type: {self.lab_type} | Capacity: {self.capacity} | Equipment: {len(self.equipment)}"

    def to_dict(self):
        data = super().to_dict()
        data["lab_type"] = self.lab_type
        data["equipment"] = self.equipment
        data["type"] = "laboratory"
        return data

    @classmethod
    def from_dict(cls, data):
        obj = cls(data["entity_id"], data["name"], data["capacity"], data["lab_type"])
        obj.current_occupants = data.get("current_occupants", [])
        obj.equipment = data.get("equipment", [])
        return obj
