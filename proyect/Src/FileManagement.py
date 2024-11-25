import os
# TP Parte 2: Clase de manejo de archivos

class FileManager():
       
       '''
       Esta Clase toma un archivo y, según el método instanciado, se puede editar o abrir el archivo.
       
       - Con file_writer(), podemos editar un archivo pasando como parámetro el contenido que deseamos aregarle.
       - Al llamar a file_reader() lo abrimos.
       - Y al usar FileDeleter() eliminamos el archivo referenciado. 

       
       '''
       
       def __init__(self, file):
              
              self.file = file
       
       def file_writer(self, contenido):

              try:
                     with open (self.file, 'w') as file:
   
                      file.write(contenido)

    
                     print(f"Se escribió en {self.file}: {contenido}")
    
              except Exception as err:
    
                 print(f"Ocurrió un error al escribir en el archivo: {err}")
                 
       
       def file_reader(self):
              
              try:
                     with open (self.file, 'r') as file:
   
                      file.read()

    
                     print(f"Se abrió el archivo {self.file}")
    
              except Exception as err:
    
                 print(f"Ocurrió un error al abrir el archivo: {err}")
                 
       def FileDeleter(self):
              
           try:  
                     if os.path.exists(self.file):
                     
                            os.remove(self.file)
                            print(f"El archivo {self.file} fué eliminado correctamente.")
                     else:
                            print(f"No se encontró el archivo {self.file}")
                            
           except Exception as err:
                  
                     print(f"Error: {err}. No se pudo eliminar el archivo {self.file}.")
