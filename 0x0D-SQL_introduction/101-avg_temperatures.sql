-- displays the average temperature(Faranheit) by city ordered by temperature
SELECT city, AVG(value) AS avg_temp from temperatures GROUP BY city ORDER BY avg_temp DESC;
