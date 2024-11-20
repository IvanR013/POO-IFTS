import json
from Src.stringtodic import *
#TP, Parte 1:

class Documento:
    
    def __init__(self, id, contenido=None):
        
        self.id = id
        self.contenido = contenido if contenido is not None else {}

    def obtener_valor(self, clave):
       
        """Obtengo el valor correspondiente a una clave usando get()"""
        
        return self.contenido.get(clave, None)  
    
    def aJson(self):
        '''
        :Traspaso a Json:
        
        Primero, genera la estructura del diccionario con su título y contenido,
        
        Luego, inicializa la clave (El título) con el ID de cada documento.
        
        Hace lo mismo con el contenido del documento.
        
        '''
    
        diccio = {'Título':'', 'contenido': {}}
        diccio['Título'] = f'Dcoumento con ID: {self.id}'
        diccio['contenido'] = f'{self.contenido}'
        
        return json.dumps(diccio)
    

    def modificar_valor(self, clave, valor):
        
        """Modifica o agrega un valor a la clave en el contenido"""
        self.contenido[clave] = valor

    def __str__(self):
        
        return f"Documento (id: {self.id}, contenido: {self.contenido})"
        
    

class Coleccion:
   
    def __init__(self, nombre: str):
        
        self.nombre = nombre
        
        self.documentos = {}
    
    def añadir_documento(self, documento):
        '''
        :Añadir Documento:
        
       El método añadir_documento recibe un parámetro llamado documento. Este parámetro debe ser un objeto de la clase Documento. Si el documento que se pasa al método no es una instancia de la clase Documento, se lanza una excepción con el mensaje "Doc incorrecto.".
       
       Esto es una forma de asegurarse de que solo se están añadiendo objetos del tipo correcto.
        
        '''
        
        if not isinstance(documento, Documento):
            
            raise Exception("Doc incorrecto. Probá con otro.")
        
        self.documentos[documento.id] = documento # Asume que documento es una instancia de Coleccion y agarra la key del diccionario como id.
        
    def eliminar_documento(self, id_documento: int):
        
        if id_documento in self.documentos:
            
            del self.documentos[id_documento]
            
    def buscar_documento(self, id_documento):
        
        return self.documentos.get(id_documento, None)
    
    
    def __str__(self):
        
        return f'Coleccion {self.nombre} | {len(self.documentos)} Documento/s registrados'





# Ej 3
class Bbddocumental:
    '''
    Una representación de cómo una base de datos puede funcionar pero con objetos en python.
    
    Permite crear, eliminar o mostrar las colecciones generadas.
    
    '''
    
    def __init__(self):
        
        self.colecciones = {}  # diccionaio vacío para guardar los documentos


    def crear_coleccion(self, nombre_coleccion):
        
        '''
        :Crear Colección:
        
        Revisa el diccionario de colecciones y, si ya no existe una colección idéntica a la que se quiere crear,
        
        se permite implementarla. 
        
        '''
        
       
        if nombre_coleccion not in self.colecciones: # Si no habías creado antes una colección con el mismo nombre, podés crear otra como una instancia de la clase Colección.
            
            self.colecciones[nombre_coleccion] = Coleccion(nombre_coleccion)
        

    def eliminar_colecion(self, nombre_coleccion):
        
        '''
        :Eliminar Colección:
        
        Busca la colección en el diccionario de colecciones
        
        
        y, si lo encuentra, lo elimina. Si no, Lanza un error.
        
        '''
        
     
        if nombre_coleccion in self.colecciones:
         
            del self.colecciones[nombre_coleccion]
        else:
                 
            print(f"Error: No se pudo borrar la colección '{nombre_coleccion}' porque no la encontré.")


    def recuperar_colecion(self, nombre_coleccion):
        
        '''
        :Recuperar Colección:
        
        Devuelve los elementos del diccionario colecciones. Es como tirar un SELECT en SQL.  
        
        '''
        
        return self.colecciones.get(nombre_coleccion, None)
    
    def importCSV(self, file_path, nombre_coleccion, schema, separator=','):
        """
        :Importar CSV:
        
        Importa datos de un archivo CSV y los agrega a una colección específica,
        usando una instancia de Str2Dic para convertir cada fila en un diccionario.

        :param file_path: Ruta del archivo CSV.
        :param nombre_coleccion: Nombre de la colección donde se importarán los datos.
        :param schema: Esquema para el parser de CSV.
        :param separator: Separador de las columnas en el CSV (por defecto es coma).
        """
        parseador = Str2Dic(schema, separator)
        
        try: # Este try tiene 2 except que manejan los posibles errores al abrir el archivo. Los marco abajo con un "*".

            with open(file_path, mode='r', encoding = 'utf-8') as file:
                
            
             for line in file:
                 
                try: # Este otro maneja los posibles errores una vez abierto el archivo.
                      
                       if line.strip(): # Se fija si hay líneas vacías.
                            
                            # Convertir la línea en diccionario usando el parser     
                            documento = parseador.convert(line.strip())
                       
                        # Agregar el documento a la colección
                       
                            self.colecciones[nombre_coleccion].añadir_documento(documento)
                
                except ValueError as e:
                
                        print(f"Error al procesar la línea '{line.strip()}': {e}")
                        
            print(f"Datos importados a la colección '{nombre_coleccion}' exitosamente.")
      
        except FileNotFoundError: # *
        
            print(f"Error: El archivo {file_path} no existe.")
        
        except Exception as error: # *
        
            print(f"Se produjo un error al importar el archivo: {error}")    




    def __str__(self):

        return f"Esta Base de datos: {self.nombre_coleccion}, tiene {len(self.colecciones)} colecciones."
        


 
 