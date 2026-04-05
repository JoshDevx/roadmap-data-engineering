# Operaciones de Resumen
MIN(): devuelve el valor más pequeño de una columna
MAX(): devuelve el valor más grande
AVG(): devuelve el promedio (la media aritmética)

COUNT(): Cuenta
SELECT COUNT(order_id) AS order_count
FROM orders;

* conteo único o COUNT DISTINCT. Esta función:

Primero elimina los valores duplicados
Luego cuenta solo los valores únicos que quedan

SELECT COUNT(DISTINCT user_id) AS user_count
FROM orders;

* Multiples consultas en una sola
SELECT COUNT(trip_id) AS total_viajes,
      COUNT(DISTINCT rider_id) AS pasajeros_unicos,
      COUNT(DISTINCT driver_id) AS conductores_unicos,
      SUM(fare) AS tarifa_total,
      AVG(fare) AS promedio_tarifa
FROM trips;

Las bases de datos tienen una estructura jerárquica: en el nivel superior, una base de datos contiene múltiples esquemas (o conjuntos de datos). Cada esquema contiene múltiples tablas. Y cada tabla consiste en filas y columnas con tipos de datos definidos.

En BigQuery específicamente, esta jerarquía usa la terminología: proyecto → conjunto de datos → tabla.

# Jerarquia
Normalmente, las tablas se referencian con un formato completo como proyecto.dataset.tabla. Por ejemplo, data-manipulation.ecommerce.orders se refiere a la tabla orders en el dataset ecommerce dentro del proyecto data-manipulation.

# REPASO
* Fundamentos de las consultas SQL

Una consulta SQL recupera datos de una base de datos utilizando las palabras clave SELECT y FROM.
SELECT column_1,
       column_2
FROM table_name;

SELECT especifica qué columnas se deben recuperar (* para todas las columnas).
FROM especifica qué tabla se va a consultar.
; es el terminador de sentencia que marca el final de una consulta.

* Agregación de datos

La agregación de datos es la operación de resumir datos aplicando funciones (como SUM, AVG, COUNT) a las columnas para producir valores únicos.
La agregación de datos revela información y patrones que son difíciles de reconocer al examinar únicamente los datos en bruto.

* Resumir datos en SQL

Para aplicar operaciones de resumen en SQL, utiliza funciones de agregación dentro de una sentencia SELECT:
SELECT COUNT(column_1) AS metric_1,
       SUM(column_2)   AS metric_2
FROM table_name;

La palabra clave AS asigna un nombre temporal (alias) a una columna, lo que hace que el resultado sea más legible.
Calcula múltiples valores de resumen en una sola consulta enumerando las funciones de agregación separadas por comas.
También puedes calcular un solo valor de resumen utilizando una única función de agregación.

* Operaciones de resumen

SUM(): Calcula el total de todos los valores de una columna.
AVG(): Calcula el valor promedio de una columna.
MIN(): Encuentra el valor mínimo de una columna.
MAX(): Encuentra el valor máximo de una columna.
COUNT(): Cuenta el número de filas o valores.
COUNT(DISTINCT column): Cuenta el número de valores únicos.

# ORDEN DE EJECUCION 
FROM
SELECT
LIMIT

# Filtrando (WHERE)

* orden 
FROM
WHERE
SELECT
LIMIT

# Varios CRITERIOS 
OR
AND
BETWEEN

-- Select the title and release_year for all German-language films released before 2000
SELECT title, release_year
FROM films
WHERE language = 'German' AND release_year < 2000;

SELECT *
FROM films
WHERE language = 'German' AND (release_year > 2000 AND release_year < 2010)

-- Find the title and year of films from the 1990 or 1999
SELECT title, release_year
FROM films
WHERE release_year = 1990 OR release_year = 1999;

SELECT title, release_year
FROM films
WHERE (release_year = 1990 OR release_year = 1999)
	AND (language = 'English' OR language = 'Spanish')
-- Filter films with more than $2,000,000 gross
	AND gross > 2000000;

# Usando BETWEEN
-- Select the title and release_year for films released between 1990 and 2000
SELECT title, release_year
FROM films
WHERE release_year BETWEEN 1990 AND 2000;

SELECT title, release_year
FROM films
WHERE release_year BETWEEN 1990 AND 2000
	AND budget > 100000000
-- Amend the query to include Spanish or French-language films
	AND (language = 'Spanish' OR language = 'French') ;

# Filtrar Texto

LIKE 
    %(coincide con cero, uno o muchos caracteres)
    _(coincide con un solo caracter)
    WHERE name LIKE 'Jay%' - inician con Jay
    WHERE name LIKE 'Me_' - un solo caracter despues de 'Me' 
NOT LIKE - Valores que no coincidan
    WHERE name NOT LIKE 'K%' - que no inicien con K
IN
    WHERE año IN (1920,1930,1940)
    WHERE lenguaje IN ('Spanish', 'France')

-- Select the names that start with B
SELECT name 
FROM people
WHERE name LIKE 'B%';

SELECT name
FROM people
-- Select the names that have r as the second letter
WHERE name LIKE '_r%';

SELECT name
FROM people
-- Select names that don't start with A
WHERE name NOT LIKE 'A%'

-- Find the title and release_year for all films over two hours in length released in 1990 and 2000
SELECT title, release_year
FROM films
WHERE release_year IN (1990, 2000)
    AND (duration > 120); 

-- Find the title, certification, and language all films certified NC-17 or R that are in English, Italian, or Greek
SELECT title, certification, language
FROM films
WHERE certification IN ('NC-17', 'R')
    AND language IN ('English', 'Italian', 'Greek')

-- Count the unique titles
SELECT 	COUNT(DISTINCT title) AS nineties_english_films_for_teens
FROM films
-- Filter to release_years to between 1990 and 1999
WHERE release_year BETWEEN 1990 AND 1999
-- Filter to English-language films
	AND language = 'English'
-- Narrow it down to G, PG, and PG-13 certifications
	AND certification IN ('G', 'PG', 'PG-13');

# valores NULOS
NULL
IS NULL

WHERE birthdate IS NULL - Valores nulos
WHERE birthdate IS NOT NULL - Valores no nulos

* COUNT solo cuenta valores NO NULOS

-- List all film titles with missing budgets
SELECT title AS no_budget_info
FROM films
WHERE budget IS NULL;

-- Count the number of films we have language data for
SELECT COUNT(title) AS count_language_known
FROM films
WHERE language IS NOT NULL; 