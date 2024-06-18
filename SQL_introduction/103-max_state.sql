-- Este script muestra la temperatura máxima de cada estado, ordenada por el nombre del estado
SELECT state, MAX(temperature) AS max_temperature
FROM temperatures
GROUP BY state
ORDER BY state;
