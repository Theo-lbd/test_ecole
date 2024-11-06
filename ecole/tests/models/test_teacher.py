from ecole.models.teacher import Teacher
from ecole.models.course import Course
from datetime import date


def test_teacher_initialization():
    # Initialisation d'un enseignant
    teacher = Teacher("Victor", "Hugo", 45, date(2023, 9, 4))

    # Vérifie les attributs d'initialisation
    assert teacher.hiring_date == date(2023, 9, 4)
    assert teacher.courses_teached == []


def test_add_course(mocker):
    # Création d'un enseignant et d'un cours
    teacher = Teacher("Marie", "Curie", 38, date(2023, 9, 4))
    course = Course("Chimie", date(2024, 2, 26), date(2024, 3, 15))

    # Mock de l'attribut teacher du cours pour isoler le test
    mocker.patch.object(course, 'teacher', None)

    # Assigne le cours à l'enseignant
    teacher.add_course(course)

    # Vérifie que le cours est bien assigné à l'enseignant
    assert course.teacher == teacher
    # Vérifie que le cours est bien dans la liste des cours enseignés
    assert course in teacher.courses_teached


def test_teacher_str():
    # Création d'un enseignant
    teacher = Teacher("Sophie", "Germain", 40, date(2023, 9, 4))

    # Vérifie que la représentation en chaîne de caractères est correcte
    assert str(teacher) == f"{teacher.first_name} {teacher.last_name}, arrivé(e) le {teacher.hiring_date}"
