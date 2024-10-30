import json
class Str2Dic():
   
    def __init__(self, schema: str, separator = ','):
        
        self.separator = separator
        
        self.schema = schema.split(separator)
   
    def convert(self, row):
   
        tmp = row.split(self.separator)
   
        if len(tmp) == len(self.schema):

            return {key:value for key, value in zip(self.schema, tmp)}
        
        else:
            
            raise ValueError("La longitud de los datos no coincide con el schema.")

        



