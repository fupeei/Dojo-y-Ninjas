from app_flask.configuracion.mysqlconecction import connectToMySQL

class Ninja:
    def __init__(self, datos):
        self.id = datos["id"]
        self.first_name = datos["first_name"]
        self.last_name = datos["last_name"]
        self.age = datos["age"]
        self.created_at = datos["created_at"]
        self.updated_at = datos["updated_at"]
        self.dojo_id = datos["dojo_id"]

    @classmethod
    def seleccionar_algunos(cls, datos):
        query = """ 
                SELECT *
                FROM ninjas
                WHERE dojo_id = %(id)s;
                """
        resultado = connectToMySQL("esquema_dojos_y_ninjas").query_db(query,datos)
        
        lista_ninjas = []
        
        for renglon in resultado:
            ninja = Ninja(renglon)
            lista_ninjas.append(ninja)
        return lista_ninjas
    
    @classmethod
    def agregar_uno(cls,datos):
        query = """
                Insert INTO ninjas (first_name,last_name,age,dojo_id) 
                VALUES(%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s);
                """
        resultado = connectToMySQL('esquema_dojos_y_ninjas').query_db(query,datos)
        return resultado