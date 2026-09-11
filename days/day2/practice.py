"""
╔══════════════════════════════════════════════════════════════════╗
║  Day 2 Practice — Build a Student Grade Manager                  ║
║  Uses: OOP, Inheritance, Error Handling, Modules, File I/O       ║
║  Run: python practice.py                                         ║
╚══════════════════════════════════════════════════════════════════╝

Your mission: Build a system to manage student grades.
This uses EVERYTHING from Day 1 + Day 2.
"""

import json
import datetime
import os


# ── Custom Exceptions ──────────────────────────────────────────
class StudentError(Exception):
    """Base exception for student-related errors"""
    pass

class InvalidGradeError(StudentError):
    """Raised when a grade is not between 0 and 100"""
    pass

class StudentNotFoundError(StudentError):
    """Raised when a student is not found"""
    pass


# ── Base Class: Person ─────────────────────────────────────────
class Person:
    """Base class for any person in the system"""

    def __init__(self, name, age):
        if not name.strip():
            raise ValueError("Name cannot be empty!")
        if age < 0 or age > 150:
            raise ValueError(f"Invalid age: {age}")
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} (age {self.age})"

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"


# ── Child Class: Student ───────────────────────────────────────
class Student(Person):
    """A student with grades — inherits from Person"""

    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.grades = {}       # {"Math": [85, 90], "Science": [78]}
        self.enrolled_date = datetime.datetime.now().strftime("%Y-%m-%d")

    def add_grade(self, subject, score):
        """Add a grade for a subject (0-100)"""
        if not isinstance(score, (int, float)):
            raise InvalidGradeError(f"Grade must be a number, got {type(score).__name__}")
        if score < 0 or score > 100:
            raise InvalidGradeError(f"Grade must be 0-100, got {score}")

        if subject not in self.grades:
            self.grades[subject] = []
        self.grades[subject].append(score)

    def get_average(self, subject=None):
        """Get average grade — for one subject or overall"""
        if subject:
            if subject not in self.grades:
                return 0
            scores = self.grades[subject]
            return round(sum(scores) / len(scores), 1) if scores else 0

        # Overall average across all subjects
        all_scores = []
        for scores in self.grades.values():
            all_scores.extend(scores)
        return round(sum(all_scores) / len(all_scores), 1) if all_scores else 0

    def get_letter_grade(self):
        """Convert average to letter grade"""
        avg = self.get_average()
        if avg >= 90: return "A"
        if avg >= 80: return "B"
        if avg >= 70: return "C"
        if avg >= 60: return "D"
        return "F"

    def to_dict(self):
        """Convert student to dictionary (for saving to JSON)"""
        return {
            "name": self.name,
            "age": self.age,
            "student_id": self.student_id,
            "enrolled_date": self.enrolled_date,
            "grades": self.grades,
            "average": self.get_average(),
            "letter_grade": self.get_letter_grade(),
        }

    def __str__(self):
        return (f"Student: {self.name} (ID: {self.student_id}) | "
                f"Avg: {self.get_average()} ({self.get_letter_grade()})")

    def __len__(self):
        """Total number of grades across all subjects"""
        return sum(len(scores) for scores in self.grades.values())


# ── Grade Manager — manages multiple students ─────────────────
class GradeManager:
    """Manages a collection of students and their grades"""

    def __init__(self, filename="students.json"):
        self.students = {}     # {student_id: Student}
        self.filename = filename

    def add_student(self, name, age, student_id):
        """Add a new student"""
        if student_id in self.students:
            raise StudentError(f"Student ID '{student_id}' already exists!")
        student = Student(name, age, student_id)
        self.students[student_id] = student
        return student

    def get_student(self, student_id):
        """Find a student by ID"""
        if student_id not in self.students:
            raise StudentNotFoundError(f"No student with ID '{student_id}'")
        return self.students[student_id]

    def get_top_students(self, n=3):
        """Get top N students by average grade"""
        ranked = sorted(
            self.students.values(),
            key=lambda s: s.get_average(),
            reverse=True
        )
        return ranked[:n]

    def class_average(self):
        """Get the overall class average"""
        if not self.students:
            return 0
        averages = [s.get_average() for s in self.students.values()]
        return round(sum(averages) / len(averages), 1)

    def save(self):
        """Save all students to a JSON file"""
        data = {sid: s.to_dict() for sid, s in self.students.items()}
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=2)
        print(f"  💾 Saved {len(self.students)} students to {self.filename}")

    def display_all(self):
        """Display all students in a formatted table"""
        if not self.students:
            print("  No students yet!")
            return

        print(f"  {'Name':<15} {'ID':<10} {'Avg':<8} {'Grade':<6} {'Subjects'}")
        print(f"  {'─'*15} {'─'*10} {'─'*8} {'─'*6} {'─'*20}")
        for student in self.students.values():
            subjects = ", ".join(student.grades.keys()) if student.grades else "None"
            print(f"  {student.name:<15} {student.student_id:<10} "
                  f"{student.get_average():<8} {student.get_letter_grade():<6} {subjects}")

    def __str__(self):
        return f"GradeManager({len(self.students)} students)"

    def __len__(self):
        return len(self.students)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# RUN THE PRACTICE PROJECT
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
if __name__ == "__main__":
    print("🎓 Student Grade Manager")
    print("━" * 55)

    manager = GradeManager("day2_students.json")

    # ── Add students ──
    print("\n📝 Adding students...")
    s1 = manager.add_student("Lucky", 21, "STU001")
    s2 = manager.add_student("Rahul", 22, "STU002")
    s3 = manager.add_student("Priya", 20, "STU003")
    s4 = manager.add_student("Amit", 23, "STU004")
    print(f"  Added {len(manager)} students")

    # ── Add grades ──
    print("\n📊 Adding grades...")
    s1.add_grade("Python", 92)
    s1.add_grade("Python", 88)
    s1.add_grade("Math", 85)
    s1.add_grade("AI", 95)

    s2.add_grade("Python", 78)
    s2.add_grade("Math", 82)
    s2.add_grade("AI", 70)

    s3.add_grade("Python", 95)
    s3.add_grade("Python", 98)
    s3.add_grade("Math", 90)
    s3.add_grade("AI", 88)

    s4.add_grade("Python", 65)
    s4.add_grade("Math", 72)
    s4.add_grade("AI", 60)

    # ── Display all ──
    print("\n📋 All Students:")
    manager.display_all()

    # ── Individual stats ──
    print(f"\n📈 Lucky's Details:")
    print(f"  Overall average: {s1.get_average()}")
    print(f"  Python average: {s1.get_average('Python')}")
    print(f"  Letter grade: {s1.get_letter_grade()}")
    print(f"  Total grades: {len(s1)}")

    # ── Top students ──
    print(f"\n🏆 Top 3 Students:")
    for i, student in enumerate(manager.get_top_students(3), 1):
        print(f"  {i}. {student.name} — {student.get_average()} ({student.get_letter_grade()})")

    # ── Class average ──
    print(f"\n📊 Class Average: {manager.class_average()}")

    # ── Error handling demo ──
    print("\n⚠️  Error Handling:")

    # Invalid grade
    try:
        s1.add_grade("Math", 150)
    except InvalidGradeError as e:
        print(f"  Caught: {e}")

    # Student not found
    try:
        manager.get_student("STU999")
    except StudentNotFoundError as e:
        print(f"  Caught: {e}")

    # Duplicate student
    try:
        manager.add_student("Clone", 20, "STU001")
    except StudentError as e:
        print(f"  Caught: {e}")

    # ── Save to file ──
    print()
    manager.save()

    # Show saved file
    print(f"\n📄 Saved file preview:")
    with open("day2_students.json", "r") as f:
        content = f.read()
    lines = content.split("\n")
    for line in lines[:15]:
        print(f"  {line}")
    if len(lines) > 15:
        print(f"  ... ({len(lines) - 15} more lines)")

    # Clean up
    os.remove("day2_students.json")

    print("\n" + "━" * 55)
    print("🎉 Practice Complete!")
    print("━" * 55)
    print("""
    What you practiced:
    ✅ Classes & Objects (Person, Student, GradeManager)
    ✅ Inheritance (Student inherits from Person)
    ✅ Dunder methods (__str__, __len__, __repr__)
    ✅ Custom Exceptions (InvalidGradeError, StudentNotFoundError)
    ✅ Error handling (try/except with specific error types)
    ✅ Modules (json, datetime, os)
    ✅ File I/O with JSON (save/load)
    ✅ Day 1 concepts (lists, dicts, f-strings, loops, functions)
    """)
