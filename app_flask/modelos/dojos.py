from app_flask.configuracion.mysqlconecction import connectToMySQL

class Dojo:
    def __init__(self, datos):
        self.id = datos["id"]
        self.nombre = datos["nombre_dojo"]
        self.created_at = datos["created_at"]
        self.updated_at = datos["updated_at"]

    @classmethod
    def seleccionar_todo(cls):
        query = """ 
                SELECT *
                FROM dojos;
                """
        resultado = connectToMySQL("esquema_dojos_y_ninjas").query_db(query)
        
        lista_dojos = []
        
        for renglon in resultado:
            dojo = Dojo(renglon)
            lista_dojos.append(dojo)
        return lista_dojos
    
    @classmethod
    def agregar_uno(cls,datos):
        query = """
                Insert INTO dojos (nombre_dojo) 
                VALUES(%(nombre_dojo)s);
                """
        resultado = connectToMySQL('esquema_dojos_y_ninjas').query_db(query,datos)
        return resultado
    
    @classmethod
    def seleccionar_uno(cls, datos):
        query = """ 
                SELECT *
                FROM dojos
                WHERE id = %(id)s;
                """
        resultado = connectToMySQL("esquema_dojos_y_ninjas").query_db(query, datos)
        print(resultado)
        if len(resultado) != 0:
            dojo = Dojo(resultado[0])
            return dojo
        return None