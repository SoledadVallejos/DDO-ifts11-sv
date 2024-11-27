from .str2dic import Str2Dic
from .custom_exceptions import *
import json

#Document
class Document:
    def __init__(self, id: int, contenido: dict = None):
        self.id = id
        self.contenido = contenido if contenido is not None else {} #otra forma de escribir if, si hay contenido sera el contenido, si es none sera vacio
        
    def get_value(self, clave: str) -> str:
        return self.contenido.get(clave, None)
    
    def modify_value(self, clave: str, valor: str) -> None:
        self.contenido[clave] = valor
        
    def __str__(self) -> str:
        return f'Documento | ID {self.id}\n{self.contenido}'

 #Collection   
class Collection:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.documentos = {} #type:ignore
    
    def add_document(self, documento: Document) -> None:
        if (type(documento) != Document):
            raise TypeError('Documento invalido')
        self.documentos[documento.id] = documento
        
    def delete_document(self, id_documento: int) -> None:
        doc = self.documentos.get(id_documento, None)
        if doc is None:
            raise NotFoundError('No se encontro el documento')
        del self.documentos[id_documento]
            
    def get_document(self, id_documento: int) -> Document | None:
        return self.documentos.get(id_documento, None)
    
    def list_documents(self) -> list[Document]:
        total = []
        for i in self.documentos:
            total.append(self.documentos[i])
        return total
        
    
    def __str__(self):
        return f'Coleccion {self.nombre} | {len(self.documentos)} Documento registrado'

#DB    
class Database:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.colecciones = {}
        
    def create_collection(self, nombre_coleccion: str) -> None:
        if nombre_coleccion not in self.colecciones:
            self.colecciones[nombre_coleccion] = Collection(nombre_coleccion)
            
    def delete_collection(self, nombre_coleccion: str) -> None:
        if nombre_coleccion in self.colecciones:
            del self.colecciones[nombre_coleccion]
            
    def get_collection(self, nombre_coleccion: str) -> Collection | None:
        return self.colecciones.get(nombre_coleccion, None)
    
    def import_csv(self, name: str, path: str) -> None:
        if (type(path) != str):
            raise AttributeError("Ruta inexistente.")
        with open(path) as f:
            schema = f.readline().replace("\n", "")
            rows = f.readlines()
            parser = Str2Dic(schema)
            col = self.get_collection(name)
            if (col == None):
                raise NonExistentCollectionError("El documento no existe")
            doc_id = 0
            for row in rows:
                item = parser.convert(row.replace("\n", ""))
                col.add_document(Document(doc_id, item))
                doc_id += 1
                
    
    def __str__(self):
        return f'Base de datos con {len(self.documentos)} colecciones'
    