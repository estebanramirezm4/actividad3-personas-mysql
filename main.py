"""Actividad 3"""
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL
def crear_conexion():
    load_dotenv()
    url = URL.create(
        drivername="mysql+pymysql",
        username=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", "3306")),
        database=os.getenv("DB_NAME"),
    )
    return create_engine(url)
def main():
    engine = crear_conexion()
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    print("Conexión exitosa a MySQL")

if __name__ == "__main__":
    main()