-- Este script lista todos los registros de la tabla second_table con valores de name, mostrando score y name, ordenados por score de mayor a menor
SELECT score, name 
FROM second_table 
WHERE name IS NOT NULL AND name != '' 
ORDER BY score DESC;
