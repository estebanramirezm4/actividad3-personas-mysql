"""Actividad 3"""
import os
from dotenv import load_dotenv
from sqlalchemy import Column, Date, Integer, MetaData, String, Table, create_engine
from sqlalchemy.engine import URL

NOMBRE_TABLA = "personas_esteban"  
metadata = MetaData()
personas = Table(
    NOMBRE_TABLA,
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("nombre", String(100), nullable=False),
    Column("apellido", String(100), nullable=False),
    Column("correo", String(150)),
    Column("telefono", Integer),
    Column("fecha_de_nacimiento", Date),
    Column("ciudad", String(100)),
    Column("direccion", String(255)),
    Column("oficio", String(150)),
)
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
    metadata.create_all(engine)
    print(f"Tabla {NOMBRE_TABLA} lista")


if __name__ == "__main__":
    main()