import psycopg2

class Db_connector:
    def __init__(self, db_params):
        self.db_params = db_params
        self.connection = None
    
    def connect(self):
        if not self.connection:
            self.connection = psycopg2.connect(**self.db_params)
            print('connected succesfully')
        else:
            print('')
            
        
    def disconect(self):
        if self.connection:
            self.connection.close()
            print('connection closed')
        else:
            print('There is no conection to close')

