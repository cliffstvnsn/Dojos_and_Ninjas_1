from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja_model import Ninja


class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_one(cls, data):
        query = '''
                SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojos_id = dojos.id
                WHERE dojos.id = %(id)s;
                '''
        results = connectToMySQL("dojos_and_ninjas").query_db(query, data)
        if results:
            dojo = cls( results[0] )
            for row_from_db in results:

                ninja_data = {
                    "id" : row_from_db["ninjas.id"],
                    "first_name" : row_from_db["first_name"],
                    "last_name" : row_from_db["last_name"],
                    "age" : row_from_db["age"],
                    "created_at" : row_from_db["ninjas.created_at"],
                    "updated_at" : row_from_db["ninjas.updated_at"],
                    "dojo_id" : row_from_db["dojos_id"]
                }
                dojo.ninjas.append( Ninja(ninja_data) )
            return dojo

    @classmethod
    def get_all(cls):
        query = '''
                SELECT * FROM dojos;
                '''
        results = connectToMySQL("dojos_and_ninjas").query_db(query)
        all_dojos = []
        for row in results:
            all_dojos.append(cls(row))
        return all_dojos

    @classmethod
    def create(cls, data):
        query = '''
                INSERT INTO dojos(name) 
                VALUES (%(name)s); 
                '''
        connectToMySQL("dojos_and_ninjas").query_db(query, data)


