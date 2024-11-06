from ecole.business.school import School
from ecole.models.course import Course
from ecole.models.teacher import Teacher
from ecole.models.student import Student
from datetime import date

def test_add_course():
    # Création d'une école et d'un cours
    school = School()
    course = Course("Mathématiques", date(2024, 2, 12), date(2024, 3, 8))

    # Ajoute le cours à l'école
    school.add_course(course)

    # Vérifie que le cours est bien ajouté à la liste des cours de l'école
    assert course in school.courses

def test_add_teacher():
    # Création d'une école et d'un enseignant
    school = School()
    teacher = Teacher("Marie", "Curie", 38, date(2023, 9, 4))

    # Ajoute l'enseignant à l'école
    school.add_teacher(teacher)

    # Vérifie que l'enseignant est bien ajouté à la liste des enseignants de l'école
    assert teacher in school.teachers

def test_add_student():
    # Création d'une école et d'un étudiant
    school = School()
    student = Student("Paul", "Dubois", 12)

    # Ajoute l'étudiant à l'école
    school.add_student(student)

    # Vérifie que l'étudiant est bien ajouté à la liste des élèves de l'école
    assert student in school.students

def test_display_courses_list(mocker):
    # Création d'une école, d'un cours, d'un enseignant et d'un étudiant
    school = School()
    course = Course("Physique", date(2024, 2, 19), date(2024, 3, 8))
    teacher = Teacher("Albert", "Einstein", 45, date(2023, 9, 4))
    student = Student("Isaac", "Newton", 18)

    # Assignations
    course.set_teacher(teacher)
    course.add_student(student)
    school.add_course(course)

    # Mock de la fonction print pour capturer la sortie
    mock_print = mocker.patch("builtins.print")

    # Appel de la méthode
    school.display_courses_list()

    # Vérifie que l'affichage est correct
    mock_print.assert_any_call(f"cours de {course}")
    mock_print.assert_any_call(f"- {student}")
