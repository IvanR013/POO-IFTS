# TP Parte 2: Clase de manejo de archivos

class FileManager():
       
       def __init__(self, file):
              
              self.file = file
       
       def file_writer(self, contenido):

              try:
                     with open (self.filename, 'w') as file:
   
                      file.write(contenido)

    
                     print(f"Se escribió en {self.filename}: {contenido}")
    
              except Exception as err:
    
                 print(f"Ocurrió un error al escribir en el archivo: {err}")