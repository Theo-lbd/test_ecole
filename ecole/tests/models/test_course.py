from ecole.models.course import Course
from ecole.models.teacher import Teacher
from ecole.models.student import Student
from datetime import date


def test_course_initialization():
    # Initialisation d'un cours
    course = Course("Mathématiques", date(2024, 2, 12), date(2024, 3, 8))

    # Vérifie les attributs d'initialisation
    assert course.name == "Mathématiques"
    assert course.start_date == date(2024, 2, 12)
    assert course.end_date == date(2024, 3, 8)
    assert course.teacher is None
    assert course.students_taking_it == []


def test_set_teacher(mocker):
    # Création d'un cours et d'un enseignant
    course = Course("Physique", date(2024, 2, 19), date(2024, 3, 8))
    teacher = Teacher("Marie", "Curie", 38, date(2023, 9, 4))

    # Mock de la liste des cours enseignés par l'enseignant pour isoler le test
    mocker.patch.object(teacher, 'courses_teached', [])

    # Assigne l'enseignant au cours
    course.set_teacher(teacher)

    # Vérifie que le cours est bien assigné à l'enseignant
    assert course.teacher == teacher
    # Vérifie que le cours est bien ajouté à la liste des cours de l'enseignant
    assert course in teacher.courses_teached


def test_add_student(mocker):
    # Création d'un cours et d'un étudiant
    course = Course("Chimie", date(2024, 2, 26), date(2024, 3, 15))
    student = Student("Paul", "Dubois", 12)

    # Mock de la liste des cours suivis par l'étudiant pour isoler le test
    mocker.patch.object(student, 'courses_taken', [])

    # Ajoute l'étudiant au cours
    course.add_student(student)

    # Vérifie que l'étudiant est bien ajouté à la liste des étudiants du cours
    assert student in course.students_taking_it
    # Vérifie que le cours est bien ajouté à la liste des cours de l'étudiant
    assert course in student.courses_taken


def test_course_str(mocker):
    # Création d'un cours sans enseignant
    course = Course("Histoire", date(2024, 2, 5), date(2024, 2, 16))

    # Mock de l'enseignant
    teacher = Teacher("Jules", "Michelet", 32, date(2023, 9, 4))
    mocker.patch.object(course, 'teacher', teacher)

    # Vérifie que la représentation en chaîne de caractères est correcte avec et sans enseignant
    assert str(course) == f"{course.name} ({course.start_date} – {course.end_date}),\nenseigné par {teacher}"
