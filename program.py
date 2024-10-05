class Libro:

    def __init__(self, titulo: str, autor: str):
        self.titulo = titulo
        self.autor = autor

        

o = Libro("Breve historia del tiempo", "Stephen Hawking")
o2= Libro("El tejido del cosmos", "Brian Greene")
o3 = Libro("La estructura del tiempo", "Stephen Hawking")
o4 = Libro("El origen de las especies", "Charles Darwin")


class Biblioteca:
    
    def __init__(self):
        
        self.libros = []  # Lista para almacenar libros

    def agregar_libro(self, *libro: Libro):
        
        # Agrega un libro a la biblioteca
        for i in libro:
            
            self.libros.append(i)

    def listar_libros(self):
        
        # Muestra todos los libros en la biblioteca en formato diccionario
        
        return {libro.titulo : libro.autor for libro in self.libros}


ins = Biblioteca()

ins.agregar_libro(o,o2,o3,o4)


print(ins.listar_libros())

# Prueba de las clases
# Crea algunos libros
# Crea una biblioteca
# Agrega los libros a la biblioteca
# Lista los libros almacenados
