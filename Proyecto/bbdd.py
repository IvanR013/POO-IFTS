#TP, Parte 1:

# Ej 1
class Documento:
    
    def __init__(self, id, contenido=None):
        
        self.id = id
        self.contenido = contenido if contenido is not None else {}

    def obtener_valor(self, clave):
       
        """Obtengo el valor correspondiente a una clave usando get()"""
        return self.contenido.get(clave, None)  

    def modificar_valor(self, clave, valor):
        """Modifica o agrega un valor a la clave en el contenido"""
        self.contenido[clave] = valor

    def __str__(self):
        
        return f"Documento (id: {self.id}, contenido: {self.contenido})"
        
        
# Ej 2

class Coleccion:
   
    def __init__(self, nombre: str):
        
        self.nombre = nombre
        
        self.documentos = {}
    
    def añadir_documento(self, documento: int):
        
        self.documentos[documento.id] = documento
        
    def eliminar_documento(self, id_documento: int):
        
        if id_documento in self.documentos:
            
            del self.documentos[id_documento]
            
    def buscar_documento(self, id_documento):
        
        return self.documentos.get(id_documento, None)
    
    
    def __str__(self):
        
        return f'Coleccion {self.nombre} | {len(self.documentos)} Documento/s registrados'



o = Coleccion("Una breve historia del tiempo.")

o.añadir_documento(1)

print(o.buscar_documento(1))


# Ej 3
class Bbddocumental:
    
    
    def __init__(self):
        
        self.colecciones = {}  # diccionaio vacío para guardar los documentos


    def crear_coleccion(self, nombre_coleccion):
        
        if nombre_coleccion not in self.colecciones:
            
            self.colecciones[nombre_coleccion] = Coleccion(nombre_coleccion)
        
   
    def eliminar_colecion(self, nombre_coleccion):
        
        if nombre_coleccion in self.colecciones:
            
            del self.colecciones[nombre_coleccion]


    def recuperar_colecion(self, nombre_coleccion):
        
        return self.colecciones.get(nombre_coleccion, None)


    def __str__(self):

        return f"Colección {self.nombre_coleccion}, con {len(self.colecciones)} documentos."
        
 

 
 