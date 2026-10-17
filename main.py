"""Actividad 3 insertar registros"""
import os
from dotenv import load_dotenv
from faker import Faker
from sqlalchemy import (
    Column,
    Date,
    Integer,
    MetaData,
    String,
    Table,
    create_engine,
    func,
    insert,
    select,
    text,
)
from sqlalchemy.engine import URL

NOMBRE_TABLA = "personas_esteban"
TOTAL_REGISTROS = 100000
TAMANO_LOTE = 5000

metadata = MetaData()

personas = Table(
    NOMBRE_TABLA,
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("nombre", String(100), nullable=False),
    Column("apellido", String(100), nullable=False),
    Column("correo", String(150)),
    Column("telefono", String(50)),
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

def generar_personas(fake, cantidad):
    return [
        {
            "nombre": fake.first_name(),
            "apellido": fake.last_name(),
            "correo": fake.email(),
            "telefono": fake.phone_number(),
            "fecha_de_nacimiento": fake.date_of_birth(minimum_age=18, maximum_age=90),
            "ciudad": fake.city(),
            "direccion": fake.street_address(),
            "oficio": fake.job(),
        }
        for _ in range(cantidad)
    ]

def insertar_por_lotes(engine, fake):
    with engine.begin() as conn:
        conn.execute(text(f"TRUNCATE TABLE {NOMBRE_TABLA}")) 
        for inicio in range(0, TOTAL_REGISTROS, TAMANO_LOTE):
            lote = generar_personas(fake, TAMANO_LOTE)
            conn.execute(insert(personas), lote)
            print(f"Insertados {inicio + TAMANO_LOTE:,} / {TOTAL_REGISTROS:,}")

def contar_registros(engine):
    with engine.connect() as conn:
        return conn.execute(select(func.count()).select_from(personas)).scalar()

def main():
    engine = crear_conexion()
    metadata.create_all(engine) 
    print(f"Tabla {NOMBRE_TABLA} lista")
    fake = Faker("es_CO")
    insertar_por_lotes(engine, fake)
    print(f"Total de registros en {NOMBRE_TABLA}: {contar_registros(engine):,}")
if __name__ == "__main__":
    main()