# Prueba de bbdd.

from proyect.Src.bbdd import *

documentito1 = Documento(1, {})
documentito2 = "Documento"

Colección = Coleccion('documentos')

Colección.añadir_documento(documentito1)

print(Colección)

Colección.añadir_documento(documentito2)