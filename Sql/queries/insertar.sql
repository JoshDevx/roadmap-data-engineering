--INSERT INTO cursos(titulo, descripcion, fecha_creacion, duracion)
--VALUES("SQL", "Aprendiendo SQL", "2025-01-29 00:00:00", 1200);

--INSERT INTO cursos(titulo, descripcion, fecha_creacion, duracion)
--VALUES("Python", "Aprendiendo Python", "2026-04-01 00:00:00", 60),
--        ("ETL-Python", "Aprendiendo ETL", "2026-04-01 00:00:00", 120);

INSERT INTO cursos (titulo, descripcion, fecha_creacion, duracion)
VALUES
    ('Python', 'Aprendiendo Python', '2026-04-01 00:00:00', 60),
    ('ETL-Python', 'Aprendiendo ETL', '2026-04-01 00:00:00', 120),
    ('Manejo de Excepciones', 'Try/Except para evitar caídas en producción', '2026-04-01 00:00:00', 45),
    ('POO Básica', 'Clases y Objetos para estructurar código', '2026-04-01 00:00:00', 90),
    ('PostgreSQL Avanzado', 'Consultas, Window Functions y optimización', '2026-04-01 00:00:00', 150),
    ('Automatización de Excels', 'Extracción de datos desde formularios', '2026-04-01 00:00:00', 75),
    ('Introducción a dbt', 'Transformación de datos en la capa Silver', '2026-04-01 00:00:00', 180),
    ('Arquitectura Medallón', 'Diseño de capas Bronce, Plata y Oro', '2026-04-01 00:00:00', 100),
    ('Snowflake Cloud DW', 'Almacenamiento y modelado dimensional', '2026-04-01 00:00:00', 200),
    ('Apache Airflow', 'Orquestación de pipelines y automatización', '2026-04-01 00:00:00', 160);