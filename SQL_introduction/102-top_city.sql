-- Este script muestra las 3 ciudades con la temperatura más alta durante julio y agosto, ordenadas de forma descendente por temperatura
SELECT city, temperature
FROM temperatures
WHERE MONTH(date) IN (7, 8)
ORDER BY temperature DESC
LIMIT 3;
