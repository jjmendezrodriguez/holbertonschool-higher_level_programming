-- Este script imprime la descripción de la tabla first_table en la base de datos especificada
SELECT 
    COLUMN_NAME, 
    COLUMN_TYPE, 
    IS_NULLABLE, 
    COLUMN_KEY, 
    COLUMN_DEFAULT, 
    EXTRA 
FROM 
    information_schema.COLUMNS 
WHERE 
    TABLE_SCHEMA = DATABASE() AND TABLE_NAME = 'first_table';
