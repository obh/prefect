from abc import ABC, abstractmethod
import json
from models import models
import mysql.connector
import os
from multiprocessing.pool import ThreadPool


class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def add_client(self, client: models.CredEntry):
        pass


class MySqlDatabase(Database):
    def __init__(self):
        pool_size = 10
        self.pool = ThreadPool(pool_size)
        self.config = {
            "host": "localhost",
            "user": "root",
            "password": os.environ.get("MYSQL_DB_PASSWORD"),
            "database": "prefect"
        }

    def connect(self):
        conn = mysql.connector.connect(**self.config)
        return conn

    def add_client(self, client: models.CredEntry):
        conn = self.pool.apply(self.connect)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO clients (provider, client_id, credentials, status, added_on, updated_on) '
                       'VALUES (%s, %s, %s, %s, %s, %s)',
                       (str(client.provider), client.client_id, json.dumps(client.credentials), str(client.status),
                        client.added_on, client.updated_on))
        conn.commit()
        conn.close()

