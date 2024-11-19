from .Clases.bbdd import *

#T.P. parte final: Uso de las clases.

def mostrar_menu():
  
    print("\n--- Base de Datos Documental ---")
  
    print("1. Crear colección")
  
    print("2. Importar CSV a colección")
  
    print("3. Consultar documento en colección")
  
    print("4. Eliminar documento de colección")
  
    print("5. Listar todos los documentos en colección")
  
    print("6. Salir")
  
    return input("Seleccione una opción: ")


def main():
    
    '''
    Dependiendo la opción elegida en la función anterior, se instancia la clase correspondiente llamando al método correspondiente
    a lo que quiero hacer.
    
    
    Por ej: 
    Si tengo una opcion para crear documento (que es la 1 supongamos), esa opcion pasa por los if's de la funcion main() y 
    
    dentro de ese mismo if, instancio la clase con el método que voy a usar.
    
    :En este caso: 
    
    - nombre_doc = input("Ingrese el nombre del documento a crear: ") # Pido el nombre del doc
    
    - db = Documento() # Instancio la clase, cosa que ya se hace en la línea 46.
    
    - Documento.crear_doc(nombre_doc) # Llamo al método crear_doc pasandole el nombre del input
    
    '''
   
    db = Bbddocumental("MiBaseDeDatos")

    while True: #Bucle principal inifinto
       
        opcion = mostrar_menu()
        
        if opcion == "1":
            
            nombre_coleccion = input("Ingrese el nombre de la colección: ")
            
            db.crear_coleccion(nombre_coleccion)
            
            print(f"Colección '{nombre_coleccion}' creada.")
        
        elif opcion == "2":
          
            nombre_coleccion = input("Ingrese el nombre de la colección: ")
          
            ruta_csv = input("Ingrese la ruta del archivo CSV: ")
          
            db.importCSV(nombre_coleccion, ruta_csv)
        
        elif opcion == "3":
          
            nombre_coleccion = input("Ingrese el nombre de la colección: ")
          
            doc_id = input("Ingrese el ID del documento: ")
          
            coleccion = db.buscar_documento(nombre_coleccion) # Busca el doc por su nombre
          
            if coleccion:
          
                documento = coleccion.buscar_documento(doc_id) # ahora por su id
          
                if documento:# Si encuentra el doc, te lo muestra en formato diccionario, sino, te tira un error
                    print("Documento encontrado:")
                   
                    print(documento.to_json())
          
                else:
                    print("Documento no encontrado.")
          
            else:
                print(f"Colección '{nombre_coleccion}' no encontrada.")
        
        elif opcion == "4":
         
            nombre_coleccion = input("Ingrese el nombre de la colección: ")
         
            doc_id = input("Ingrese el ID del documento a eliminar: ")
         
            coleccion = db.buscar_documento(nombre_coleccion) # Primero lo busca
         
            if coleccion: # y si lo encuentra, lo borra.
         
                coleccion.eliminar_documento(doc_id)
        
        elif opcion == "5":
          
            nombre_coleccion = input("Ingrese el nombre de la colección: ")
          
            coleccion = db.recuperar_colecion(nombre_coleccion)
          
            if coleccion:
             
                documentos = coleccion.buscar_documento() 
          
                if documentos:
          
                    print("\n--- Lista de Documentos ---") 
                    
                    for i in documentos: # Itera en los resultados de buscarDocumento y los pasa a Json.
                        
                        print(i.to_json())
                     
                        print("-----------")
                   
                    print("---------------------------")
                
                else:
                
                    print("No hay documentos en la colección.")
        
        elif opcion == "6": # Imprime un mensaje y sale del bucle.
 
            print("Saliendo del programa.")
 
            break
        
        else:
 
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
 
    main()