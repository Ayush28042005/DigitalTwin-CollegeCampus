from campus import Campus
from datetime import datetime

def main():
    college_name = input("Enter your college name: ").strip()
    campus = Campus(college_name)

    while True:
        print(f"\n=== Digital Twin - {campus.college_name} ===")
        print("1. Add Classroom")
        print("2. Add Laboratory")
        print("3. Add Student")
        print("4. Add Faculty")
        print("5. Assign Student to Classroom")
        print("6. Mark Attendance")
        print("7. View All Buildings")
        print("8. View All People")
        print("9. View Campus Summary")
        print("10. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            entity_id = input("Enter classroom ID (e.g. C001): ").strip()
            name = input("Enter classroom name: ").strip()
            try:
                capacity = int(input("Enter capacity: ").strip())
            except ValueError:
                print("❌ Invalid capacity!")
                continue
            subject = input("Enter subject: ").strip()
            campus.add_classroom(entity_id, name, capacity, subject)

        elif choice == "2":
            entity_id = input("Enter lab ID (e.g. L001): ").strip()
            name = input("Enter lab name: ").strip()
            try:
                capacity = int(input("Enter capacity: ").strip())
            except ValueError:
                print("❌ Invalid capacity!")
                continue
            lab_type = input("Enter lab type (Computer/Chemistry/Physics): ").strip()
            campus.add_laboratory(entity_id, name, capacity, lab_type)

        elif choice == "3":
            entity_id = input("Enter student ID (e.g. S001): ").strip()
            name = input("Enter student name: ").strip()
            try:
                age = int(input("Enter age: ").strip())
            except ValueError:
                print("❌ Invalid age!")
                continue
            email = input("Enter email: ").strip()
            roll_number = input("Enter roll number: ").strip()
            try:
                semester = int(input("Enter semester: ").strip())
            except ValueError:
                print("❌ Invalid semester!")
                continue
            campus.add_student(entity_id, name, age, email, roll_number, semester)

        elif choice == "4":
            entity_id = input("Enter faculty ID (e.g. F001): ").strip()
            name = input("Enter faculty name: ").strip()
            try:
                age = int(input("Enter age: ").strip())
            except ValueError:
                print("❌ Invalid age!")
                continue
            email = input("Enter email: ").strip()
            employee_id = input("Enter employee ID: ").strip()
            department = input("Enter department: ").strip()
            campus.add_faculty(entity_id, name, age, email, employee_id, department)

        elif choice == "5":
            student_id = input("Enter student ID: ").strip()
            classroom_id = input("Enter classroom ID: ").strip()
            campus.assign_student_to_classroom(student_id, classroom_id)

        elif choice == "6":
            classroom_id = input("Enter classroom ID: ").strip()
            date = datetime.now().strftime("%d-%m-%Y")
            print(f"Marking attendance for {date}")
            student_ids_input = input("Enter present student IDs (comma separated): ").strip()
            student_ids = [s.strip() for s in student_ids_input.split(",")]
            campus.mark_attendance(classroom_id, date, student_ids)

        elif choice == "7":
            campus.view_all_buildings()

        elif choice == "8":
            campus.view_all_persons()

        elif choice == "9":
            campus.view_campus_summary()

        elif choice == "10":
            print(f"👋 Goodbye! {campus.college_name} Digital Twin closed!")
            break

        else:
            print("❌ Invalid choice! Please enter 1-10.")

if __name__ == "__main__":
    main()
    