def add_students(name,age,course):
    """
    Adds a new student to the student list.

    Parameters:
    name (str): The name of the student.
    age (int): The age of the student.
    course (str): The course the student is enrolled in.

    Returns:
    dict: A dictionary containing the student's information.
    """
    student = {
        'name': name,
        'age': age,
        'course': course
    }
    return student