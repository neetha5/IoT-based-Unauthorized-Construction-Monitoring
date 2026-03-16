import json
import os

class Student:
    def __init__(self, sid, name, age, branch, marks):
        self.sid = sid
        self.name = name
        self.age = age
        self.branch = branch
        self.marks = marks

    def to_dict(self):
        return {
            "sid": self.sid,
            "name": self.name,
            "age": self.age,
            "branch": self.branch,
            "marks": self.marks
        }


class StudentManagementSystem:

    def __init__(self):
        self.students = []
        self.file = "students.json"
        self.load_students()

    def load_students(self):
        if os.path.exists(self.file):
            with open(self.file, "r") as f:
                data = json.load(f)
                for s in data:
                    student = Student(
                        s["sid"], s["name"], s["age"], s["branch"], s["marks"]
                    )
                    self.students.append(student)

    def save_students(self):
        data = [s.to_dict() for s in self.students]
        with open(self.file, "w") as f:
            json.dump(data, f, indent=4)

    def add_student(self):
        sid = input("Enter Student ID: ")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        branch = input("Enter Branch: ")

        marks = []
        for i in range(3):
            m = int(input(f"Enter mark {i+1}: "))
            marks.append(m)

        student = Student(sid, name, age, branch, marks)
        self.students.append(student)
        self.save_students()

        print("Student added successfully")

    def view_students(self):
        if not self.students:
            print("No student records")
            return

        for s in self.students:
            print("\n-----------------------")
            print("ID:", s.sid)
            print("Name:", s.name)
            print("Age:", s.age)
            print("Branch:", s.branch)
            print("Marks:", s.marks)

    def delete_student(self):
        sid = input("Enter student ID to delete: ")

        for s in self.students:
            if s.sid == sid:
                self.students.remove(s)
                self.save_students()
                print("Student deleted")
                return

        print("Student not found")

    def update_student(self):
        sid = input("Enter student ID to update: ")

        for s in self.students:
            if s.sid == sid:
                s.name = input("Enter new name: ")
                s.age = int(input("Enter new age: "))
                s.branch = input("Enter new branch: ")

                marks = []
                for i in range(3):
                    m = int(input(f"Enter new mark {i+1}: "))
                    marks.append(m)

                s.marks = marks

                self.save_students()
                print("Student updated")
                return

        print("Student not found")

    def calculate_average(self, marks):
        return sum(marks) / len(marks)

    def show_averages(self):
        for s in self.students:
            avg = self.calculate_average(s.marks)
            print(f"{s.name} average marks: {avg:.2f}")

    def find_topper(self):
        if not self.students:
            print("No students available")
            return

        topper = None
        highest = 0

        for s in self.students:
            avg = self.calculate_average(s.marks)

            if avg > highest:
                highest = avg
                topper = s

        print("\nTopper Details")
        print("Name:", topper.name)
        print("Branch:", topper.branch)
        print("Average:", highest)

    def branch_statistics(self):
        stats = {}

        for s in self.students:
            if s.branch not in stats:
                stats[s.branch] = []

            avg = self.calculate_average(s.marks)
            stats[s.branch].append(avg)

        for branch, values in stats.items():
            avg = sum(values) / len(values)
            print(f"Branch {branch} Average Marks: {avg:.2f}")

    def menu(self):
        while True:
            print("\n====== Student Management System ======")
            print("1. Add Student")
            print("2. View Students")
            print("3. Update Student")
            print("4. Delete Student")
            print("5. Show Average Marks")
            print("6. Find Topper")
            print("7. Branch Statistics")
            print("8. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                self.add_student()

            elif choice == "2":
                self.view_students()

            elif choice == "3":
                self.update_student()

            elif choice == "4":
                self.delete_student()

            elif choice == "5":
                self.show_averages()

            elif choice == "6":
                self.find_topper()

            elif choice == "7":
                self.branch_statistics()

            elif choice == "8":
                print("Exiting system...")
                break

            else:
                print("Invalid choice")


def main():
    system = StudentManagementSystem()
    system.menu()


if __name__ == "__main__":
    main()