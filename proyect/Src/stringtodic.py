#TP parte 4: String to Dicc.
class Str2Dic():
    
    '''
  
    Esta clase convierte una fila de datos en formato de texto (como CSV) en un diccionario, 
    usando un esquema proporcionado como claves.

    Args:
        schema (str o list): Esquema que se usará como claves del diccionario. Puede ser un string CSV 
                             o una lista de claves.
        separator (str): Separador que se usa para dividir la fila y el esquema. Por defecto es ','.

    :Ejemplo:
        
       - schema = "id,name,age"
        
       - row = "1,John,30"
        
       - str2dic = Str2Dic(schema)
        
       - dic = str2dic.convert(row)
        
       - print(dic)  # {'id': '1', 'name': 'John', 'age': '30'}
    
    '''
   
    def __init__(self, schema: str, separator = ','):
        
        self.separator = separator
        
        self.schema = schema.split(separator)
   
    def convert(self, row):
   
        tmp = row.split(self.separator)
   
        if len(tmp) == len(self.schema):

            return {key:value for key, value in zip(self.schema, tmp)}
        
        else:
            
            raise ValueError("La longitud de los datos no coincide con el schema.")

        



