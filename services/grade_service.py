from models.grade_model import calculate_grade

def process_result(marks):
    """Process subject marks and return total, percentage and grade."""
    return calculate_grade(marks)
