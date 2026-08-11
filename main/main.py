from models.grade_model import calculate_grade
from utils.input_utils import get_marks

def main():
    marks = get_marks(5)
    total, percentage, grade = calculate_grade(marks)

    print("\n --Result-- ")
    print("Total marks:", total)
    print("percentage:", percentage)
    print("Grade:", grade)

if __name__ == "__main__":
    main()
