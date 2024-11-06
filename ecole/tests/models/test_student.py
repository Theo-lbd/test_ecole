from ecole.models.student import Student
from ecole.models.course import Course


def test_student_initialization():
    # Initialisation d'un étudiant
    student = Student("Paul", "Dubois", 12)

    # Vérifie le numéro de l'étudiant et l'initialisation de la liste des cours
    assert student.student_nbr == Student.students_nb
    assert student.courses_taken == []


def test_add_course(mocker):
    # Création d'un étudiant et d'un cours
    student = Student("Valérie", "Dumont", 13)
    course = Course("Français", "2024-01-29", "2024-02-16")

    # Mock de la liste des étudiants prenant le cours pour isoler le test
    mocker.patch.object(course, 'students_taking_it', [])

    # Ajoute le cours à l'étudiant
    student.add_course(course)

    # Vérifie que le cours est bien ajouté dans la liste des cours de l'étudiant
    assert course in student.courses_taken
    # Vérifie que l'étudiant est bien ajouté dans la liste des étudiants du cours
    assert student in course.students_taking_it


def test_student_str():
    # Création d'un étudiant
    student = Student("Louis", "Berthot", 11)

    # Vérifie que la représentation en chaîne de caractères est correcte
    assert str(
        student) == f"{student.first_name} {student.last_name} ({student.age} ans), n° étudiant : {student.student_nbr}"
