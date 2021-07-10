from typing import Optional


class Garden:
    PLANT_NAMES = {
        "G": "Grass",
        "C": "Clover",
        "R": "Radishes",
        "V": "Violets",
    }
    DEFAULT_STUDENTS = [
        "Alice",
        "Bob",
        "Charlie",
        "David",
        "Eve",
        "Fred",
        "Ginny",
        "Harriet",
        "Ileana",
        "Joseph",
        "Kincaid",
        "Larry",
    ]

    def __init__(
        self, diagram: str, students: Optional[list[str]] = None
    ) -> None:
        self.rows = diagram.split("\n")
        self.students = sorted(students) if students else self.DEFAULT_STUDENTS
        self.student_ids = {name: i for i, name in enumerate(self.students)}

    def plants(self, student: str) -> list[str]:
        result = []
        student_id = self.student_ids[student]

        for row in self.rows:
            for i in range(2 * student_id, 2 * student_id + 2):
                plant_key = row[i]
                result.append(self.PLANT_NAMES[plant_key])

        return result
