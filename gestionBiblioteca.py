class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    def mostrar_info(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"Título: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}, Estado: {estado}"

    def prestar(self):
        if self.disponible:
            self.disponible = False
            return "Libro prestado exitosamente."
        return "El libro ya está prestado."

    def devolver(self):
        self.disponible = True
        return "Libro devuelto exitosamente."

class Revista(Libro):
    def __init__(self, titulo, autor, isbn, numero_edicion):
        super().__init__(titulo, autor, isbn)
        self.numero_edicion = numero_edicion

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Edición: {self.numero_edicion}"

class Usuario:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def prestar(self, libro):
        return libro.prestar()

    def devolver(self, libro):
        return libro.devolver()

class Estudiante(Usuario):
    def __init__(self, nombre):
        super().__init__(nombre, "Estudiante")

    def prestar(self, libro):
        if libro.disponible:
            return f"{self.nombre} (Estudiante) ha prestado: {libro.titulo}."
        return "El libro no está disponible."

class Profesor(Usuario):
    def __init__(self, nombre):
        super().__init__(nombre, "Profesor")

    def prestar(self, libro):
        if libro.disponible:
            return f"{self.nombre} (Profesor) ha prestado: {libro.titulo}. Tiene prioridad sobre estudiantes."
        return "El libro no está disponible."
