-- Este script lista todos los registros de la tabla second_table con un score >= 10, mostrando score y name, ordenados por score de mayor a menor
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
