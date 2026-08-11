def get_marks(number_of_subjects):
    marks = []

    for i in range(number_of_subjects):
        mark = int(input(f"Enter marks of Subject {i + 1}: "))
        marks.append(mark)

    return marks
