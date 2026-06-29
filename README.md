# Digital Twin of a College Campus

A Python-based command-line application that creates a Digital Twin of a college campus. It models buildings, classrooms, laboratories, students, and faculty using all 4 pillars of Object Oriented Programming.

---

## Features

- Add classrooms with subject and capacity
- Add laboratories with type and equipment
- Add students with roll number and semester
- Add faculty with employee ID and department
- Assign students to classrooms
- Mark daily attendance for each classroom
- View all buildings and people on campus
- View complete campus summary
- Persistent storage using JSON

---

## Class Hierarchy

```
CampusEntity (Abstract Base Class)
    │
    ├── Building
    │     ├── Classroom  → subject, attendance
    │     └── Laboratory → lab_type, equipment
    │
    └── Person (Abstract)
          ├── Student    → roll_number, semester, attendance_record
          └── Faculty    → employee_id, department
```

---

## OOP Pillars Used

| Pillar | Where Used |
|---|---|
| **Abstraction** | `CampusEntity` and `Person` are Abstract Base Classes |
| **Inheritance** | `Student` and `Faculty` inherit `Person`; `Classroom` and `Laboratory` inherit `Building` |
| **Polymorphism** | `get_occupancy()` and `get_role()` behave differently per subclass |
| **Encapsulation** | Attendance and capacity stored privately inside classes |

---

## Project Structure

```
Digital-Twin-College-Campus/
│
├── campus_entity.py    → Abstract base class (CampusEntity)
├── building.py         → Building, Classroom, Laboratory classes
├── person.py           → Person, Student, Faculty classes
├── campus.py           → Campus manager class
├── main.py             → Entry point and menu
└── data.json           → Persistent JSON storage
```

---

## How To Run

```bash
python main.py
```

No external libraries required. Just Python 3.x!

---

## Menu Options

```
=== Digital Twin - College Campus ===
1.  Add Classroom
2.  Add Laboratory
3.  Add Student
4.  Add Faculty
5.  Assign Student to Classroom
6.  Mark Attendance
7.  View All Buildings
8.  View All People
9.  View Campus Summary
10. Exit
```

---

## Polymorphism Example

```python
# Same method name, different behaviour!
classroom.get_occupancy()   # Returns: 25
laboratory.get_occupancy()  # Returns: "10/30 (Safe limit: 15)"

student.get_role()          # Returns: "Student"
faculty.get_role()          # Returns: "Faculty"
```

---

## Author

**Ayush Saini**

