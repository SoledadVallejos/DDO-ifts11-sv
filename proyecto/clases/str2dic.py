from .custom_exceptions import *

class Str2Dic():
    def __init__(self, schema: str, separator=','):
        if (len(schema)) == 0:
            raise SchemaError("Schema vacio")
        self.schema = schema.split(separator)
        self.separator = separator
    def convert(self, row: list[str]) -> dict:
        linea = row.split(self.separator)
        if len(linea) == len(self.schema):
            i = 0
            d = {}
            while i < len(linea):
                d[self.schema[i]] = linea[i]
                i += 1
            return d
        else:
            raise SchemaError("Los campos no coinciden con el schema")
