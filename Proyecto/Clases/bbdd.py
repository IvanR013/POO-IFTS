import json
from Clases.stringtodic import *
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
        
        Verifica que el tipo de dato correspondiente al documento sea correcto.
        
        Si es así, "documento" pasa a ser id.
        
        '''
        
        if (type(documento)) != Documento:
            
            raise Exception("Doc incorrecto.")
        
        self.documentos[documento.id] = documento
        
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
        
       
        if nombre_coleccion not in self.colecciones:
            
            self.colecciones[nombre_coleccion] = Coleccion(nombre_coleccion)
        

    def eliminar_colecion(self, nombre_coleccion):
        
        '''
        :Eliminar Colección:
        
        Busca la colección en el diccionario de colecciones
        
        
        y, si lo encuentra, lo elimina. Si no, Lanza un error.
        
        '''
        
        try: 
            if nombre_coleccion in self.colecciones:
         
                del self.colecciones[nombre_coleccion]
            
            
        except FileNotFoundError as err:
            
            print(f"No se encontró el archivo {err}") 



    def recuperar_colecion(self, nombre_coleccion):
        
        '''
        :Recuperar Colección:
        
        Devuelve los elementos del diccionario colecciones.  
        
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
        
        try:

            with open(file_path, mode='r', encoding = 'utf-8') as file:
                
             next(file)
            
            for line in file:
                try:
                      # Convertir la línea en diccionario usando el parser
                       
                        documento = parseador.convert(line.strip())
                       
                        # Agregar el documento a la colección
                       
                        Coleccion.agregar_documento(documento)
                
                except ValueError as e:
                
                        print(f"Error al procesar la línea '{line.strip()}': {e}")
                        
            print(f"Datos importados a la colección '{nombre_coleccion}' exitosamente.")
      
        except FileNotFoundError:
        
            print(f"Error: El archivo {file_path} no existe.")
        
        except Exception as error:
        
            print(f"Se produjo un error al importar el archivo: {error}")    


        except Exception as err:
           
            raise f'No se pudo abrir el archivo debido a: {err}.'



    def __str__(self):

        return f"Colección {self.nombre_coleccion}, con {len(self.colecciones)} documentos."
        
'''
   -- INDEV --
   
- Solucionar y matchear file_path con el nombre del metodo que esta en string to dicc
- matchear las f strings restantes
- Verificar funcionalidad de las clases y métodos.

''' 

 
 