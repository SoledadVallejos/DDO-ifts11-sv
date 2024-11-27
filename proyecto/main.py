from .clases.db import *

def mostrar_menu():
    print("\n--- Base de Datos Documental ---")
    print("1. Crear coleccion")
    print("2. Importar CSV a coleccion")
    print("3. Consultar documento en coleccion")
    print("4. Eliminar documento de coleccion")
    print("5. Listar los documentos en coleccion")
    print("6. Salir")
    return input("Debe selecionar una opcion: ")

def main():
    db = Database("MiBaseDeDatos")

    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            nombre_coleccion = input("Ingrese el nombre de la colección: ")
            db.create_collection(nombre_coleccion)
            print(f"Coleccion '{nombre_coleccion}' creada!")
        
        elif opcion == "2":
            nombre_coleccion = input("Ingrese el nombre de la coleccion: ")
            ruta_csv = input("Ingrese la ruta del archivo CSV: ")
            db.import_csv(nombre_coleccion, ruta_csv)
        
        elif opcion == "3":
            nombre_coleccion = input("Ingrese el nombre de la coleccion: ")
            doc_id = int(input("Ingrese el ID del documento: "))
            coleccion = db.get_collection(nombre_coleccion)
            if coleccion:
                documento = coleccion.get_document(doc_id)
                if documento:
                    print("Doc encontrado:")
                    print(documento)
                else:
                    print("Doc no encontrado.")
            else:
                print(f"Coleccion '{nombre_coleccion}' no encontrada.")
        
        elif opcion == "4":
            nombre_coleccion = input("Ingrese el nombre de la coleccion: ")
            doc_id = int(input("Ingrese el ID del documento a eliminar: "))
            coleccion = db.get_collection(nombre_coleccion)
            if coleccion:
                coleccion.delete_document(doc_id)
        
        elif opcion == "5":
            nombre_coleccion = input("Ingrese el nombre de la coleccion: ")
            coleccion = db.get_collection(nombre_coleccion)
            if coleccion:
                documentos = coleccion.list_documents()
                if documentos:
                    print("\n--- Lista de Documentos ---")
                    for doc in documentos:
                        print(doc)
                        print("-----------")
                else:
                    print("No hay documentos.")
        
        elif opcion == "6":
            print("Saliendo.")
            break
        
        else:
            print("Error, vuelva a intentar.")

if __name__ == "__main__":
    main()