import sqlite3

class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
        self.cursor = None
        self.connect()

    def connect(self):
        #Establece la conexión a la base de datos
        try:
            self.connection = sqlite3.connect(self.db_name)
            self.cursor = self.connection.cursor()
            print(f"Conectado a la BD: {self.db_name}")
        except sqlite3.Error as e:
            print(f"Ocurrió un error al conectarse a la BD: {e}")

    def create_table(self, table_name, columns):
        try:
            col_definitions = ', '.join([f"{col_name} {data_type}" for col_name, data_type in columns.items()])
            self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({col_definitions})")
            self.connection.commit()
            print(f"Tabla '{table_name}' creada correctamente.")
        except sqlite3.Error as e:
            print(f"Ocurrió un error al crear la tabla {e}")

    def insert_data(self, table_name, data):
        try:
            columns = ', '.join(data.keys())
            placeholders = ', '.join('?' for _ in data)
            values = tuple(data.values())
            self.cursor.execute(f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})", values)
            self.connection.commit()
            print("Datos insertados correctamente")
        except sqlite3.Error as e:
            print(f"Ocurrió un error: {e}")

    def query_data(self, table_name, columns='*', conditions=None):
        #Consultar en la BD
        try:
            condition_str = f"WHERE {conditions}" if conditions else ''
            self.cursor.execute(f"SELECT {columns} FROM {table_name} {condition_str}")
            rows = self.cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            print(f"Ocurrió un error en la consulta {e}")
            return []

    def close(self):
        #Importante cerrar la conexión para liberar espacio en memoria
        if self.connection:
            self.connection.close()
            print(f"Conexión a: {self.db_name} cerrada.")