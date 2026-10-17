# Actividad 3 - Base de datos MySQL con Python, SQLAlchemy y Faker

## Descripción

Este proyecto contiene un script en Python que automatiza la creación y el poblado de una base de datos como los que hemos creado en clase con los datos básicos que podría tener sobre una cualquier persona, en MySQL local, usando los programas:
- Python 3.10+
- SQLAlchemy
- PyMySQL
- Faker
- python-dotenv
- MySQL
- Git y GitHub

 Dentro del script s e conecta a MySQL usando *SQLAlchemy* (con el driver PyMySQL); crea automáticamente la tabla `personas_esteban` si esta no existe,luego genera datos falsos con *Faker* configurado los datos en español para después insertar los *100.000 registros* por lotes de 5.000 para optimizar el tiempo y la memoria utilizada y también lee las credenciales desde un archivo `.env` con *python-dotenv*, para no tener en el código información personal.

## Estructura de la tabla `personas_esteban`

| Columna | Tipo | Descripción |
|---|---|---|
| `id` | INTEGER (PK, autoincremental) | Identificador único |
| `nombre` | VARCHAR(100) | Nombre de la persona |
| `apellido` | VARCHAR(100) | Apellido de la persona |
| `correo` | VARCHAR(150) | Correo electrónico |
| `telefono` | VARCHAR(50) | Número de teléfono |
| `fecha_de_nacimiento` | DATE | Fecha de nacimiento (entre 18 y 90 años) |
| `ciudad` | VARCHAR(100) | Ciudad |
| `direccion` | VARCHAR(255) | Dirección |
| `oficio` | VARCHAR(150) | Oficio o profesión |


## Estructura del proyecto

```
.
├── main.py #Donde esta el cript principal
├── requirements.txt #Dependencias del proyecto
├── .env.example # Plantilla de variables de entorno
├── .gitignore #Los archivos que deben ser ignorados por Git
└── README.md  #La documentación de lo que hace el programa
```

## Instalación de dependencias

1. Clona el repositorio del siguiente :

```bash
   git clone https://github.com/estebanramirezm4/actividad3-personas-mysql
```

2. Crea y activa un entorno virtual:
```bash
   python -m venv .venv
   .venv\Scripts\Activate.ps1
  # En MAC o Linux 
   source .venv/bin/activate
   ```


3. Instala las dependencias con :
```bash
   pip install -r requirements.txt
```
## Configuración

1.Primero crea la base de datos desde Dbeaver

```sql
   CREATE DATABASE IF NOT EXISTS actividad3 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

2. Copia la plantilla de variables de entorno:

```bash
    #Windows
   copy .env.example .env

   #Mac ó Linux
   cp .env.example .env
```

3. Abre el archivo `.env` y reemplaza los valores por tus credenciales reales:

```env
   DB_USER=root
   DB_PASSWORD=tu_contraseña
   DB_HOST=localhost
   DB_PORT=3306
   DB_NAME=actividad3
```

 El archivo `.env` está incluido en el `.gitignore`, por lo que nunca se sube al repositorio.

## Forma de ejecución

Con el entorno virtual activado, ejecuta el siguiente comando:

```bash
python main.py
```

El script muestra el progreso de la inserción por lotes y, al finalizar, imprime el total de registros almacenados en la tabla.

## Verificación

Desde DBeaver, ejecuta la siguiente consulta:

```sql
SELECT COUNT(*) FROM personas_esteban;
```

El resultado esperado es `100000`.

Luego de esto podemos visualizar la tabla con el comando 
```sql
select * from actividad3 .personas_esteban pe;
```
