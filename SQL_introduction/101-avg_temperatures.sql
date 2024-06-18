-- Este script muestra la temperatura media (Fahrenheit) por ciudad, ordenada por temperatura de forma descendente
SELECT city, AVG(temperature) AS average_temperature
FROM temperatures
GROUP BY city
ORDER BY average_temperature DESC;
