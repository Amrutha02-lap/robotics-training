student = {
    "name": "Amrutha",
    "course": "MSc Data Science",
    "mark": 85
}


def display_student(data):
    for key, value in data.items():
        print(key, ":", value)


display_student(student)
