import os
# TP Parte 2: Clase de manejo de archivos

class FileManager():
       
       '''
       Esta Clase toma un archivo y, según el método instanciado, se puede editar o abrir el archivo.

       
       '''
       
       def __init__(self, file):
              
              self.file = file
       
       def file_writer(self, contenido):

              try:
                     with open (self.filename, 'w') as file:
   
                      file.write(contenido)

    
                     print(f"Se escribió en {self.filename}: {contenido}")
    
              except Exception as err:
    
                 print(f"Ocurrió un error al escribir en el archivo: {err}")
                 
       
       def file_reader(self, contenido):
              
              try:
                     with open (self.filename, 'r') as file:
   
                      file.read(contenido)

    
                     print(f"Se abrió el archivo {self.filename}: {contenido}")
    
              except Exception as err:
    
                 print(f"Ocurrió un error al abrir el archivo: {err}")
                 
       def FileDeleter(self):
              
           try:  
                     if os.path.exists(self.file):
                     
                            os.remove(self.file)
                     else:
                            print(f"No se encontró el archivo {self.file}")
                            
           except Exception as err:
                  
                     print(f"No se encontró el archivo {self.file}, {err}")