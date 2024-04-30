import unittest
class Profesor:
    def __init__(self, nombre, cargo, legajo,antiguedad):
        self.__nombre__ = nombre
        self.__cargo__ = cargo
        self.__legajo__ = legajo
        self.__antiguedad__ = antiguedad
    def obtener_nombre(self):
        return self.__nombre__
    def obtener_cargo(self):
        return self.__cargo__
    def obtener_legajo(self):
        return self.__legajo__
    def obtener_antiguedad(self):
        return self.__antiguedad__
    def cambiar_nombre(self, nombre):
        self.__nombre__ = nombre

class Alumno :
    def __init__(self,nombre,legajo,mail):
        self.__nombre__ = nombre
        self.__legajo__ = legajo
        self.__mail__ = mail
    def obtener_nombre(self):
        return self.__nombre__
    def obtener_alumnos(self):
        return self.obtener_alumnos
    def cambiar_nombre(self, nombre):
        self.__nombre__ = nombre

class Materia:
    def __init__(self, nombre, profesores, alumnos:list[Alumno]):
        self.__nombre__ = nombre
        self.__profesores__ = profesores
        self.__alumnos__ = alumnos
    def obtener_nombre(self):
        return self.__nombre__
    def obtener_profesores(self):
        return self.__profesores__
    def obtener_alumnos(self):
        return self.__alumnos__
    def cambiar_nombre(self, nombre):
        self.__nombre__ = nombre


class TestProfesor(unittest.TestCase):

    def test_obtener_nombre(self):
        profesor = Profesor("Juan", "Profesor", "12345", 5)
        self.assertEqual(profesor.obtener_nombre(), "Juan")
        
    def test_obtener_nombre(self):
        profesor = Profesor("Pedro", "Profesor", "12345", 5)
        self.assertNotEqual(profesor.obtener_nombre(), "Juan")


class TestAlumno(unittest.TestCase):

    def test_obtener_nombre(self):
        alumno = Alumno("Pedro", "67890", "pedro@example.com")
        self.assertEqual(alumno.obtener_nombre(), "Pedro")

    def test_obtener_alumnos(self):
        profesor = Profesor("Juan", "Profesor", "12345", 5)
        alumnos = [Alumno("Pedro", "67890", "pedro@example.com")]
        materia = Materia("Matemáticas", [profesor], alumnos)
        self.assertEqual(materia.obtener_alumnos(), alumnos)
        
class TestMateria(unittest.TestCase):

    def test_obtener_nombre(self):
        profesor = Profesor("Juan", "Profesor", "12345", 5)
        alumnos = [Alumno("Pedro", "67890", "pedro@example.com")]
        materia = Materia("Matemáticas", [profesor], alumnos)
        self.assertEqual(materia.obtener_nombre(), "Matemáticas")




if __name__ == '__main__':
    unittest.main()