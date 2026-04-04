# Base de datos
Almacenar datos de forma fiable
Recuperar información eficientemente
Manipular datos sistemáticamente

Una base de datos es un sistema para gestionar datos, que se usa principalmente para dar soporte a aplicaciones y análisis, y que las bases de datos relacionales se componen de tablas.

Las tablas están compuestas de filas y columnas. Cada fila representa una entidad individual o un evento único y contiene toda la información sobre esa entidad o evento.
Una fila también se conoce como "registro" u "observación".
Cada columna representa un atributo o propiedad específica de la entidad o evento que representa la tabla y tiene un nombre descriptivo.
Una columna también se conoce como "campo" o "atributo".

# Alojamiento
Disco duro de un servidor

# Tipos de datos
numeros(INT, NUMERIC(floats)), texto-cadenas(VARCHAR), fechas

# Esquemas
Planos de la bd

#
SELECT name
FROM products;

SELECT name, year
FROM products;

SELECT * ->(Caracter comodin)
FROM products;

# Alias y Valores unicos
AS
DISTINCT

SELEC name AS name_employer
FROM employees;

SELECT DISTINCT year
FROM employees;

SELECT DISTINCT year, employes
FROM employees;

# Crear vistas
VIEWS 

CREATE VIEW name_vista AS
SELECT id, name, year
FROM employees;

* Consultar la vista
SELECT id, name
FROM name_vista;

-- Your code to create the view:
CREATE VIEW library_authors AS
SELECT DISTINCT author AS unique_author
FROM books;

-- Select all columns from library_authors
SELECT unique_author
FROM library_authors;

# Versiones Populares
Todas las variantes deben cumplir los estandares universales
PosgreSQL - relacional, de codigo abierto
SQL Server - free y empresas, Microsoft - TSQL(variante de Microsoft)

# Usando Limit
-- Select the first 10 genres from books using PostgreSQL
SELECT genre
FROM books
LIMIT 10;